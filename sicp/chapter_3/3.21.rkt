(define (print-queue queue) (display (car queue)))

;; testing
(define q1 (make-queue))

(insert-queue! q1 'a)

(display q1)
(print-queue q1)

(insert-queue! q1 'b)
(display q1)
(print-queue q1)

(delete-queue! q1)
(display q1)
(print-queue q1)

(delete-queue! q1)
(display q1)
(print-queue q1)