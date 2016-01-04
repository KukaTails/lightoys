(define f (let ((old-state 0)
                (new-state 0))
            (lambda (x)
              (begin (set! old-state new-state)
                     (set! new-state x)
                     old-state))))

;; testing
(+ (f 0) (f 1))