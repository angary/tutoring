export function drawX(size) {
    let start = 1
    let i = start
    let j = start
    let k = start
    let l = size
    
    let x = '' 
    
    // Loops through each i
    while (i <= size) {    
        // Loops through each j
        while (j <= size) {
            if (j == k) {
                x += "x"
            } else if (j == l) { 
                x += "x"
            } else {
                x += " "
            }            
            j++
        }
        i++
        j = start
        k++
        l-- 
        x = x.trim() + "\n"
    }
    
    if (size % 2 == 0) {
        // Cannot have an even size
        return 'error';
    }
    
    return x.trim()
}

console.log(drawX(11))

