void main() {
// Task 1
  int addTwo(int a, int b) {
    return a + b; //output: Addition:8
  }

// Task 2
  int subtractTwo(int a, int b) {
    return a - b; //output: Subtraction:6
  }

// Task 3
  int multiplyTwo(int a, int b) {
    return a * b; // output: Multiplication:14
  }

// Task 4
  double divideTwo(double a, double b) {
    return a / b; //Multiplication: Closure: (double, double) => double(8,4)}
  }

//Task 5
  int stringLength(String str) {
    return str.length; //Output: String Length: &(stringLength("Dart")}
  }

//Task 6
  dynamic getFirstElement(List list) {
    if (list.isEmpty) {
      return null;
    }
    return list[0]; // Output: First Element: 1
  }

  print('Addition: ${addTwo(5, 3)}');
  print('Subtraction: ${subtractTwo(10, 4)}');
  print('Multiplication: ${multiplyTwo(7, 2)}');
  print('Multiplication:$divideTwo(8, 4)}');

  print('String Length: &{stringLength("Dart")}');

  List numbers = [1, 2, 3, 4, 5];
  print('First Element: ${getFirstElement(numbers)}');
}
