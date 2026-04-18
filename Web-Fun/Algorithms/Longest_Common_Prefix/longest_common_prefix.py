/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    for (let i = 0; i < strs[0].length; i++) {
        let first = strs[0][i];
        for (let j = 0; j < strs.length; j++) {
            if (i === strs[j].length || strs[j][i] !== first) {
                return strs[0].substring(0, i);
            }
        }
    }
};
