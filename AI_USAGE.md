# AI Improvement Record

## Original Development

The original version of the application was developed entirely manually using foundational Python concepts learned in class, such as basic control flow (while and if/elif/else), custom functions, standard lists of dictionaries, manual loops for calculations, and explicit file I/O operations with the standard csv module. This ensured the foundational baseline committed to GitHub (v1.0) represented core, student-level logic.

## AI Tools Used

Google Gemini: Used to clean up code, make file saving safer, add date checking, and make the text output look nicer.

## Improvements Requested

Help with saving files safely using with open().
Help with checking dates so users only type them in YYYY-MM-DD format.
Help with printing clean, aligned tables in the console.
Help with saving budget limits so they don't erase when the program closes.

## Changes Accepted

Safer File Opening:
What Changed: Updated file saving so Python automatically closes files even if an error happens.
Why Accepted: Prevents files from getting broken or stuck open.
How Verified: Tested saving and loading files multiple times to make sure data stayed safe.
Date Checking:
What Changed: Added a check to force users to type dates like 2026-03-15.
Why Accepted: Typing dates wrong broke the monthly report feature.
How Verified: Tried typing bad dates like "yesterday" or "12/25" and made sure the program asked again.
Neat Tables:
What Changed: Made transaction outputs line up in neat columns.
Why Accepted: Makes reading long lists of transactions much easier.
How Verified: Ran the function and saw that all the numbers and dates lined up cleanly.

## Changes Rejected or Revised

Rejected Object-Oriented Code: The AI tried to rewrite the program using complex classes. This was rejected to keep the code simple and easy to understand using basic functions, lists, and dictionaries.
Rejected External Packages: The AI tried to use outside libraries. This was rejected so the program only uses basic Python built-ins without extra downloads.

## What I Learned

How with open() makes working with files much safer.
How regular expressions check text patterns like dates.
How formatting strings makes console output look clean.
How to pick helpful AI suggestions while keeping the code simple and easy to read.