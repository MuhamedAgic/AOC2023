pub mod utilities { pub mod filereader; }
pub mod y2022d14 { pub mod d14; }

use crate::utilities::filereader;
use crate::y2022d14::d14;


fn main() {
    println!("Hello, world!");

    let input = "D:/git/magic/aoc2023/aoc2023/src/y2022d14/input.txt";
    let input_as_str = filereader::get_file_as_str(input);
    println!("{}", input_as_str);

    d14::d14();
}
