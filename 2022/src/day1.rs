use std::num::ParseIntError;

// Generator to transform the string to a usable datatype
#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Result<Vec<u32>, ParseIntError> {
    input
        .split("\n\n")
        .map(|l| {
            l.split('\n').map(|s| {
                s.parse::<u32>()
            }).sum()
        }).collect()
}

#[aoc(day1, part1)]
pub fn solve_part1(input: &[u32]) -> u32 {
    *input
        .iter().max().unwrap()
}

#[aoc(day1, part2)]
pub fn solve_part2(input: &Vec<u32>) -> u32 {
    use std::collections::BinaryHeap;
    let mut heap = input.iter().copied().collect::<BinaryHeap<u32>>();
    let mut v = Vec::new();
    for _ in 0..3 {
        if let Some(p) = heap.pop() {
            v.push(p);
        }
    }
    return v.iter().sum();
}


// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     // A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
//     fn example1() {
//         assert_eq!(solve_part1(&input_generator("2x3x4")), 58);
//     }
// }