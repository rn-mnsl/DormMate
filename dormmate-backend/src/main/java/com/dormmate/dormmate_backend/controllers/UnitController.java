package com.dormmate.dormmate_backend.controllers;

    import com.dormmate.dormmate_backend.entities.Unit;
    import com.dormmate.dormmate_backend.repositories.UnitRepository;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.web.bind.annotation.*;

    import java.util.List;
    import java.util.Optional;

    @RestController
    @RequestMapping("/units")
    public class UnitController {
        @Autowired
        private UnitRepository unitRepository;
        @GetMapping
        public List<Unit> getAllUnits(){
           return unitRepository.findAll();
        }
         @PostMapping
        public Unit createUnit(@RequestBody Unit unit){
            return unitRepository.save(unit);
        }
         @GetMapping("/{id}")
        public Optional<Unit> getUnit(@PathVariable Long id){
           return unitRepository.findById(id);
        }
        @PutMapping("/{id}")
        public Unit updateUnit(@PathVariable Long id, @RequestBody Unit unit){
          Optional<Unit> unitOptional = unitRepository.findById(id);
          if(unitOptional.isPresent()){
            Unit unitToUpdate = unitOptional.get();
            unitToUpdate.setName(unit.getName());
            unitToUpdate.setTenant(unit.getTenant());
            unitToUpdate.setTenantId(unit.getTenantId());
            return unitRepository.save(unitToUpdate);
          }
          return null;
        }

        @DeleteMapping("/{id}")
        public void deleteUnit(@PathVariable Long id){
            unitRepository.deleteById(id);
        }
    }