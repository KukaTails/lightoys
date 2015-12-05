(define (make-point x y)
  (cons x y))

(define (x-point p) (car p))

(define (y-point p) (cdr p))

(define (add-point p-a p-b)
  (make-point (+ (x-point p-a) (x-point p-b))
              (+ (y-point p-a) (y-point p-b))))

(define (div-point p n)
  (make-point (/ (x-point p) n)
              (/ (y-point p) n)))

(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))

; rectangle
(define (make-rectangle l-point r-point)S
  (cons l-point r-point))

(define (l-point rectangle)
  (car rectangle))

(define (r-point rectangle)
  (cdr rectangle))

(define (circu rectangle)
  (* 2 (+ (abs (- (x-point (l-point rectangle))
                  (x-point (r-point rectangle))))
          (abs (- (y-point (l-point rectangle))
                  (y-point (r-point rectangle)))))))

(define (area rectangle)
  (* (abs (- (x-point (l-point rectangle))
             (x-point (r-point rectangle))))
     (abs (- (y-point (l-point rectangle))
             (y-point (r-point rectangle))))))

; testing for rectangle
(define rect (make-rectangle (make-point 0 0)
                             (make-point 8 8)))

(circu rect)
(area rect)