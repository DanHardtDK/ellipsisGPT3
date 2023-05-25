my ($model, $size, $log, $iter) = @ARGV;

$cmd = "python3 code/ellipsisBatch.py data/examples1 $model $size > $log";
print("running $cmd ...\n");
system($cmd);   
while (--$iter) {
    $cmd = "python3 code/ellipsisBatch.py data/examples1 $model $size >> $log";
    print("running $cmd ...\n");    
    system($cmd);
}    
