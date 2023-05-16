function computeClosestToZero(ts){
    var m = ts[0];
    for (const element of ts ){
        if (Math.abs(element) < Math.abs(m)){
            m = element
        }

    }
    return m
}

ts = [7, -10, 13 , 8, 4, -7, -12, -3, 3, -9, 6, -1, -6, 7]

r = computeClosestToZero(ts)
console.log(r)

