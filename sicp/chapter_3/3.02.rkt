(define (make-monitored func)
  (let ((called-count 0))
    (lambda (first . rest)
      (cond ((eq? first 'how-many-calls?) called-count)
            ((eq? first 'reset-count) (set! called-count 0))
            (else (set! called-count (+ called-count 1))
                  (apply func (cons first rest)))))))

;; testing
(define s (make-monitored sqrt))
(s 100)
(s 'how-many-calls?)
(s 'reset-count)
(s 'how-many-calls?)

(define (add x y)
  (+ x y))

(define add-c (make-monitored add))
(add-c 100 300)
(add-c 'how-many-calls?)
