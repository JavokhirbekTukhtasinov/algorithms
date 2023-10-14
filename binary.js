const sample = [1,2,3,4,5,6,7,8,9,9,23,34,43,100]


const binary = (target, arr) => {
    let left = 0
    let right = arr.length - 1
    
    while(left <= right) {
        let mid =  Math.round((left + right ) / 2)
        console.log('test')
        if(target == arr[mid]){
            return mid;
        }else if(target > arr[mid]) {
            left = mid + 1
        }else {
            right = mid -1 
        }
    }
    return -1
}

const result  = binary(100,sample);

if(result == -1) {
    console.log(`Element is not in primary array`)
}else{
    console.log(`Element is present at index ${result}`)
}



