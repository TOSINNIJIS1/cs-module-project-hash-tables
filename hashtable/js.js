let add = 3 > 4
console.log(add)

function String (string) {
    if(typeof string === 'number') {
        console.log('Syntax Error, Input my be string')
    } else if (typeof string === 'string') {
        console.log(string)
    }
}

String('bang')

function Length(s) {
    return s.length
}

console.log(Length('dfd34'))

let arr = []

function Addition (a, b) {
    const string = typeof a === 'string' || typeof b === 'string' 
    const num = typeof a === 'number' && typeof b === 'number'

    if (num) {
        console.log(a + b, 'This is Number')
    } else if (string) {
        console.log(a + b, 'This is String')
    } else {
        return 'Type Error, parameter a and b must be number or string'
    }
}

(Addition('2', 4))


