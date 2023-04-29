public class CpuStressTest {
    public static void main(String[] args) {
        int numThreads = Runtime.getRuntime().availableProcessors();
        ExecutorService executorService = Executors.newFixedThreadPool(numThreads);
        
        for (int i = 0; i < numThreads; i++) {
            executorService.execute(new CpuStressTask());
        }
        
        executorService.shutdown();
    }
    
    private static class CpuStressTask implements Runnable {
        @Override
        public void run() {
            while (true) {
            }
        }
    }
}
