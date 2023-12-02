pub mod utilities { pub mod filereader; pub mod stringutils;}
pub mod one {pub mod day_one; }
pub mod two {pub mod day_two; }

use crate::utilities::filereader;
use crate::utilities::stringutils;
use crate::one::day_one;
use crate::two::day_two;



fn main() 
{
    let input = "D:/git/magic/aoc2023/aoc2023/src/two/input.txt";
    
    // let d1p1 = day_one::day_one_part_one(input);
    // println!("{}", d1p1);

    // let d1p2 = day_one::day_one_part_two(input);
    // println!("{}", d1p2);

    let d2p1 = day_two::day_two_part_one(input);
    println!("{}", d2p1);

}
