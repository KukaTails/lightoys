(define (subsets s)
  (define nil '())
  (if (null? s)
      (list nil)
      (let ((rest (subsets (cdr s))))
        (append rest (map (lambda (items)
                            (cons (car s) items))
                          rest)))))

; testing
(define set (list 1 2 3))

(display (subsets set))