// 1. Parens Valid
function parensValid(str) {
    let left = 0, right = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === '(') {
            left++;
        } else if (str[i] === ')') {
            right++;
        }
        if (right > left) {
            return false;
        }
    }
    return left === right;
}

console.log(parensValid("Y(3(p)p(3)r)s")); // true

// 2. Braces Valid
function bracesValid(str) {
    const stack = [];
    const pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (char === '(' || char === '{' || char === '[') {
            stack.push(char);
        } else if (char === ')' || char === '}' || char === ']') {
            if (stack.length === 0 || stack.pop() !== pairs[char]) {
                return false;
            }
        }
    }
    return stack.length === 0;
}

console.log(bracesValid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!")); // true

// 3. paldindrome
function isPalindrome(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    const reversed = cleaned.split('').reverse().join('');
    return cleaned === reversed;
}

console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(isPalindrome("Able was I, ere I saw Elba")); // true


// 4. Longest Palindrome
function longestPalindrome(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    let longest = '';
    for (let i = 0; i < cleaned.length; i++) {
        for (let j = i + 1; j <= cleaned.length; j++) {
            const substring = cleaned.slice(i, j);
            if (isPalindrome(substring) && substring.length > longest.length) {
                longest = substring;
            }
        }
    }
    return longest;
}

console.log(longestPalindrome("what up, daddy-o?")); // "dad"
console.log(longestPalindrome("Yikes! my favorite racecar erupted!")); // "e racecar e"