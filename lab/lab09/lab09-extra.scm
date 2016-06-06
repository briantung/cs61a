(define (composed f g)
  (lambda (x)(f (g x)))
)

(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
)

(define (filter f lst)
  (if (null? lst) '()
    (if
       (f (car lst)) 
       (cons (car lst) (filter f (cdr lst)))  
       (filter f (cdr lst))
    ))
)

(define (all-satisfies lst pred)
   (if (null? lst) True 
      (if (pred (car lst)) 
        (all-satisfies (cdr lst) pred) 
        False
      ))
)

(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (accumulate combiner
                            start
                            (- n 1)
                            term)
                (term n))
      ))

