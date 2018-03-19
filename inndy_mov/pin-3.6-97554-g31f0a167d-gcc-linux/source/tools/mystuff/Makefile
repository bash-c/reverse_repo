CONFIG_ROOT := ../Config
include $(CONFIG_ROOT)/makefile.config
include $(TOOLS_ROOT)/Config/makefile.default.rules
 
all: ia32 intel64
 
ia32:
	mkdir -p obj-ia32
	$(MAKE) TARGET=ia32    obj-ia32/tracer.so
 
intel64:
	mkdir -p obj-intel64
	$(MAKE) TARGET=intel64 obj-intel64/tracer.so
 
clean-all:
	$(MAKE) TARGET=ia32    clean
	$(MAKE) TARGET=intel64 clean
