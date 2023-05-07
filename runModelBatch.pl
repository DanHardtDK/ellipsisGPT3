my ($model, $size, $log, $iter) = @ARGV;

$cmd = "python3 code/ellipsisBatch.py data/examplesYN $model $size > $log";
print("running $cmd ...\n");
system($cmd);
while (--$iter) {
    $cmd = "python3 code/ellipsisBatch.py data/examplesYN $model $size >> $log";
    print("running $cmd ...\n");    
    system($cmd);
}    
