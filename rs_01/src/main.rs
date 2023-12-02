use lazy_static::lazy_static;
use regex::Regex;
use std::fs;

lazy_static! {
    static ref DIGIT_AT_START: Regex = Regex::new(r"^(\d).*?").unwrap();
}

fn read_input() -> Vec<String> {
    fs::read_to_string("../inputs/input01.txt")
        .expect("File Error")
        .split("\n")
        .map(|s| s.trim())
        .map(|s| String::from(s))
        .collect()
}

fn parse_digits(substring: &str, parse_words: bool) -> &str {
    if DIGIT_AT_START.is_match(substring) {
        return &substring[0..1];
    }
    if !parse_words {
        return "";
    }
    if substring.starts_with("one") {
        return "1";
    }
    if substring.starts_with("two") {
        return "2";
    }
    if substring.starts_with("three") {
        return "3";
    }
    if substring.starts_with("four") {
        return "4";
    }
    if substring.starts_with("five") {
        return "5";
    }
    if substring.starts_with("six") {
        return "6";
    }
    if substring.starts_with("seven") {
        return "7";
    }
    if substring.starts_with("eight") {
        return "8";
    }
    if substring.starts_with("nine") {
        return "9";
    }
    ""
}

fn process_line(line: &str, parse_words: bool) -> u32 {
    let mut digits: String = String::new();
    for i in 0..line.len() {
        digits += parse_digits(&line[i..], parse_words)
    }
    let mut first_last: String = String::with_capacity(2);
    first_last += &digits.as_str()[0..1];
    first_last += &digits.chars().rev().into_iter().collect::<String>()[0..1];
    first_last.parse::<u32>().expect("something is wrong")
}

fn main() {
    let lines = read_input();
    let task1: u32 = lines
        .clone()
        .into_iter()
        .filter(|line| line.len() > 0)
        .map(|line| process_line(&line, false))
        .sum();
    let task2: u32 = lines
        .clone()
        .into_iter()
        .filter(|line| line.len() > 0)
        .map(|line| process_line(&line, true))
        .sum();

    println!("{}", task1);
    println!("{}", task2);
}
