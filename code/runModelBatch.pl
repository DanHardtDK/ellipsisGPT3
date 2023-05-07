my ($model, $size, $log, $iter) = @ARGV;

$cmd = "python3 ellipsisBatch.py examplesYN $model $size > $log";
print("running $cmd ...\n");
system($cmd);
while (--$iter) {
    $cmd = "python3 ellipsisBatch.py examplesYN $model $size >> $log";
    print("running $cmd ...\n");    
    system($cmd);
}    
