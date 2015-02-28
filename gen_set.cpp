#include <iostream>
#include <cstring>

using namespace std;

int main ( int argc, char *argv[] ) {
  if ( argc != 2 ) {
    cerr << "No name given" << endl;
    return 1;
    }
  unsigned r, g, b, c = 0;

  unsigned indent_size = ::strlen ( argv[1] ) + 5;
  char* indent = new char[indent_size];
  memset ( indent, ' ', indent_size - 1 );
  indent[indent_size] = 0;

  cout << argv[1] << " = (";
  for ( r = 0; r < 256; ++r ) {
    for ( g = 0; g < 256; ++g ) {
      for ( b = 0; b < 256; ++b ) {
        if ( r + g + b == 255 ) {
          if ( c )
            cout << "," << endl << indent;
          cout << "(" << r << "," << g << "," << b << ")";
          ++c;
          }
        }
      }
    }
  cout << ")" << endl;
  return 0;
  }

