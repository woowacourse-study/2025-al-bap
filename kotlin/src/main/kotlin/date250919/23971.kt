package date250919

fun main() {
    val a = readln().split(" ").map { it.toInt() }
    println(solve(a[0], a[1], a[2], a[3]))
}

fun solve(h: Int, w: Int, n: Int, m: Int): Int {
    return ((w - 1) / (m + 1) + 1) * ((h - 1) / (n + 1) + 1)
}
