all: gen_set run clean

gen_set: gen_set.cpp
	$(CXX) $(CFLAGS) -O2 gen_set.cpp -o gen_set

run:
	./gen_set PIXELSET > pixelset.py
	
clean:
	$(RM) gen_set

