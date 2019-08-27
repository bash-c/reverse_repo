// KoF97.cpp : 定义 DLL 的导出函数。
//

#define _CRT_SECURE_NO_WARNINGS
#include "nsis/plugin-common.h"
#include "Windows.h"
#include "tchar.h"
#include "cstdlib"
#include "wchar.h"

unsigned int delta = 0x9E3779B9;
HINSTANCE g_hInstance;
HWND g_hwndParent;
extra_parameters* g_pluginParms = NULL;


#define NSMETHOD_INIT(parent) {\
        g_pluginParms = extra; \
        g_hwndParent = parent; \
        EXDLL_INIT(); }


BOOL WINAPI DllMain(HANDLE hInst, ULONG ul_reason_for_call, LPVOID lpReserved)
{
	g_hInstance = (HINSTANCE)hInst;

	if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
		//do what you want at init time.
	}

	if (ul_reason_for_call == DLL_THREAD_DETACH || ul_reason_for_call == DLL_PROCESS_DETACH) {
		//clean up code.
	}

	return TRUE;
}

void scramble(unsigned int k[], unsigned int t[])
{
	unsigned int t0 = t[0], t1 = t[1];
	unsigned int n, sum = 0;
	for (n = 0; n < 32; n++) {
		sum += delta;
		t0 += ((t1 << 4) + k[0]) ^ (t1 + sum) ^ ((t1 >> 5) + k[1]);
		t1 += ((t0 << 4) + k[2]) ^ (t0 + sum) ^ ((t0 >> 5) + k[3]);
	}
	t[0] = t0; t[1] = t1;
}


extern "C" __declspec(dllexport) void __cdecl
fnKoF97(HWND hwndParent, int string_size, char* variables, stack_t** stacktop, extra_parameters* extra)
{
	NSMETHOD_INIT(hwndParent);
	{

		HKEY hKEY;
		LPCTSTR data_Set = _T("SOFTWARE\\Test\\");
		long ret = RegOpenKeyEx(HKEY_CURRENT_USER, data_Set, NULL, KEY_READ, &hKEY);

		if (ret != ERROR_SUCCESS)  
		{
			char err[30] = { 0 };
			sprintf_s(err, "error code %d", ret);

			wchar_t w_err[30] = { 0 };
			mbstowcs(w_err, err, strlen(err) + 1);
			LPCWSTR ptr = w_err;


			MessageBox(NULL, ptr, L"#RegOpenKeyEx!!", MB_OK);
			return;

			return;
		}

		DWORD type = 0;
		DWORD size = 0x1337;

		char text[0x160] = { 0 };
		ret = RegQueryValueEx(hKEY, _T("KoF"), NULL, &type, (LPBYTE)text, &size);

		if (ret != ERROR_SUCCESS)  
		{
			char err[30] = { 0 };
			sprintf_s(err, "error code %d", ret);

			wchar_t w_err[30] = { 0 };
			mbstowcs(w_err, err, strlen(err) + 1);
			LPCWSTR ptr = w_err;


			MessageBox(NULL, ptr, L"#RegQueryValueEx !!", MB_OK);
			return;
		}

		//MessageBox(NULL, (LPCWSTR)text, (LPCWSTR)text, MB_OK);

		// char text[256] = "flag{welcome_to_the_good-old-days}";
		int len = sizeof(text);

		const char* key = "wow you find me!";
		for (int i = 0; i < len / 8; i++)
		{
			scramble((unsigned int*)key, (unsigned int*)(text + (i * 8)));
		}

		pushstring(text);

	}
}


extern "C" __declspec(dllexport) void __cdecl
fnCheck(HWND hwndParent, int string_size, char* variables, stack_t** stacktop, extra_parameters* extra)
{
	NSMETHOD_INIT(hwndParent);
	{
		HKEY hKEY;
		LPCTSTR data_Set = _T("SOFTWARE\\Test\\");
		long ret = RegOpenKeyEx(HKEY_CURRENT_USER, data_Set, NULL, KEY_READ, &hKEY);

		if (ret != ERROR_SUCCESS)  
		{
			char err[30] = { 0 };
			sprintf_s(err, "error code %d", ret);

			wchar_t w_err[30] = { 0 };
			mbstowcs(w_err, err, strlen(err) + 1);
			LPCWSTR ptr = w_err;


			MessageBox(NULL, ptr, L"#RegOpenKeyEx!!", MB_OK);
			return;

			return;
		}

		DWORD type = 0;
		DWORD size = 683;

		char text[683] = { 0 };
		ret = RegQueryValueEx(hKEY, _T("KoF"), NULL, &type, (LPBYTE)text, &size);

		if (ret != ERROR_SUCCESS)  
		{
			char err[30] = { 0 };
			sprintf_s(err, "error code %d", ret);

			wchar_t w_err[30] = { 0 };
			mbstowcs(w_err, err, strlen(err) + 1);
			LPCWSTR ptr = w_err;


			MessageBox(NULL, ptr, L"#RegQueryValueEx !!", MB_OK);
			return;
		}

		char flag[683] = { 0 };
		size = 683;
		ret = RegQueryValueEx(hKEY, _T("flag"), NULL, &type, (LPBYTE)flag, &size);

		if (ret != ERROR_SUCCESS)  
		{
			char err[30] = { 0 };
			sprintf_s(err, "error code %d", ret);

			wchar_t w_err[30] = { 0 };
			mbstowcs(w_err, err, strlen(err) + 1);
			LPCWSTR ptr = w_err;


			MessageBox(NULL, ptr, L"#RegQueryValueEx !!", MB_OK);
			return;
		}

		//MessageBox(NULL, (LPCWSTR)flag, (LPCWSTR)flag, MB_OK);
		//MessageBox(NULL, (LPCWSTR)text, (LPCWSTR)text, MB_OK);

		// size_t len = strlen(text);
		WCHAR unistring[683];
		// MultiByteToWideChar(CP_OEMCP, 0, text, -1, unistring, len + 1);
		MultiByteToWideChar(CP_OEMCP, 0, text, -1, unistring, 683);


		// MessageBox(NULL, L"debug", L"debug!!", MB_OK);
		if (!memcmp(flag, unistring, 682))
		{
			MessageBox(NULL, L"right", L"right!!", MB_OK);
		}
		else
		{
			return;
		}
		//else
		//{
		//	MessageBox(NULL, L"wrong", L"wrong!!", MB_OK);
		//}
	}
}

