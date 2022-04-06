let cnt = 0
function dfs(numbers, target, depth, result) {
    if (depth === numbers.length) {
        if (result === target) {
            cnt++;
        }
        return
    }
    
    dfs(numbers, target, depth++, result + numbers[depth])
    dfs(numbers, target, depth++, result + numbers[depth]*(-1))
    return
}

let numbers = [1,1,1,1,1]
let target = 3

dfs(numbers, target, 0, 0);

console.log(cnt);