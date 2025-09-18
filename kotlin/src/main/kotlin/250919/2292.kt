package `250919`

fun main() {
    println(solve(readln().toInt()))
}

fun solve(a: Int): Int {
    var i: Int = 1
    var j: Int = 1
    while (true) {
        if (a <= i) return j
        i = i + (6 * j)
        j++
    }
}

// 1, 6, 12, 18, 24
// 6n
// 1 + 6 + 12 + 18 + 24
// 1 + 6 + 12