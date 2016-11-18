PROGDIRS = prog1 prog2
.PHONY: subdirs cleanall testall

subdirs:
	for dir in $(PROGDIRS); do \
	  $(MAKE) -C $$dir; \
	done

cleanall:
	for dir in $(PROGDIRS); do \
	  $(MAKE) -C $$dir clean; \
	done

testall:
	for dir in $(PROGDIRS); do \
	  $(MAKE) -C $$dir test; \
	done
