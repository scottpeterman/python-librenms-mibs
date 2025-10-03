# SNMP MIB module (PAN-ENTITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\paloaltonetworks\PAN-ENTITY-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:17 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(panModules,) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panModules")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

panEntityMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7)
)
if mibBuilder.loadTexts:
    panEntityMIBModule.setRevisions(
        ("2012-11-05 11:06",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanEntityMIBObjects_ObjectIdentity = ObjectIdentity
panEntityMIBObjects = _PanEntityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1)
)
_PanEntityChassisGroup_ObjectIdentity = ObjectIdentity
panEntityChassisGroup = _PanEntityChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    panEntityChassisGroup.setStatus("current")
_PanEntityTotalPowerAvail_Type = Integer32
_PanEntityTotalPowerAvail_Object = MibScalar
panEntityTotalPowerAvail = _PanEntityTotalPowerAvail_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 1, 1),
    _PanEntityTotalPowerAvail_Type()
)
panEntityTotalPowerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEntityTotalPowerAvail.setStatus("current")
_PanEntityTotalPowerUsed_Type = Integer32
_PanEntityTotalPowerUsed_Object = MibScalar
panEntityTotalPowerUsed = _PanEntityTotalPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 1, 2),
    _PanEntityTotalPowerUsed_Type()
)
panEntityTotalPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEntityTotalPowerUsed.setStatus("current")
_PanEntityFRUModuleGroup_ObjectIdentity = ObjectIdentity
panEntityFRUModuleGroup = _PanEntityFRUModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    panEntityFRUModuleGroup.setStatus("current")
_PanEntityFRUModuleTable_Object = MibTable
panEntityFRUModuleTable = _PanEntityFRUModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    panEntityFRUModuleTable.setStatus("current")
_PanEntityFRUModuleEntry_Object = MibTableRow
panEntityFRUModuleEntry = _PanEntityFRUModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1, 1)
)
panEntityFRUModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    panEntityFRUModuleEntry.setStatus("current")
_PanEntryFRUModulePowerUsed_Type = Integer32
_PanEntryFRUModulePowerUsed_Object = MibTableColumn
panEntryFRUModulePowerUsed = _PanEntryFRUModulePowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1, 1, 1),
    _PanEntryFRUModulePowerUsed_Type()
)
panEntryFRUModulePowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEntryFRUModulePowerUsed.setStatus("current")
_PanEntryFRUModuleNumPorts_Type = Integer32
_PanEntryFRUModuleNumPorts_Object = MibTableColumn
panEntryFRUModuleNumPorts = _PanEntryFRUModuleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1, 1, 2),
    _PanEntryFRUModuleNumPorts_Type()
)
panEntryFRUModuleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEntryFRUModuleNumPorts.setStatus("current")
_PanEntityFanTrayGroup_ObjectIdentity = ObjectIdentity
panEntityFanTrayGroup = _PanEntityFanTrayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    panEntityFanTrayGroup.setStatus("current")
_PanEntityFanTrayTable_Object = MibTable
panEntityFanTrayTable = _PanEntityFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    panEntityFanTrayTable.setStatus("current")
_PanEntityFanTrayEntry_Object = MibTableRow
panEntityFanTrayEntry = _PanEntityFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3, 1, 1)
)
panEntityFanTrayEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    panEntityFanTrayEntry.setStatus("current")
_PanEntryFanTrayPowerUsed_Type = Integer32
_PanEntryFanTrayPowerUsed_Object = MibTableColumn
panEntryFanTrayPowerUsed = _PanEntryFanTrayPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3, 1, 1, 1),
    _PanEntryFanTrayPowerUsed_Type()
)
panEntryFanTrayPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEntryFanTrayPowerUsed.setStatus("current")
_PanEntityPowerSupplyGroup_ObjectIdentity = ObjectIdentity
panEntityPowerSupplyGroup = _PanEntityPowerSupplyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    panEntityPowerSupplyGroup.setStatus("current")
_PanEntityPowerSupplyTable_Object = MibTable
panEntityPowerSupplyTable = _PanEntityPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    panEntityPowerSupplyTable.setStatus("current")
_PanEntityPowerSupplyEntry_Object = MibTableRow
panEntityPowerSupplyEntry = _PanEntityPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4, 1, 1)
)
panEntityPowerSupplyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    panEntityPowerSupplyEntry.setStatus("current")
_PanEntryPowerSupplyPowerCapacity_Type = Integer32
_PanEntryPowerSupplyPowerCapacity_Object = MibTableColumn
panEntryPowerSupplyPowerCapacity = _PanEntryPowerSupplyPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4, 1, 1, 1),
    _PanEntryPowerSupplyPowerCapacity_Type()
)
panEntryPowerSupplyPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEntryPowerSupplyPowerCapacity.setStatus("current")
_PanEntityMIBConformance_ObjectIdentity = ObjectIdentity
panEntityMIBConformance = _PanEntityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2)
)
_PanEntityMIBCompliances_ObjectIdentity = ObjectIdentity
panEntityMIBCompliances = _PanEntityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 1)
)
_PanEntityMIBGroups_ObjectIdentity = ObjectIdentity
panEntityMIBGroups = _PanEntityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2)
)

# Managed Objects groups

panEntityMIBChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 1)
)
panEntityMIBChassisGroup.setObjects(
      *(("PAN-ENTITY-EXT-MIB", "panEntityTotalPowerAvail"),
        ("PAN-ENTITY-EXT-MIB", "panEntityTotalPowerUsed"))
)
if mibBuilder.loadTexts:
    panEntityMIBChassisGroup.setStatus("current")

panEntityMIBFRUModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 2)
)
panEntityMIBFRUModuleGroup.setObjects(
      *(("PAN-ENTITY-EXT-MIB", "panEntryFRUModulePowerUsed"),
        ("PAN-ENTITY-EXT-MIB", "panEntryFRUModuleNumPorts"))
)
if mibBuilder.loadTexts:
    panEntityMIBFRUModuleGroup.setStatus("current")

panEntityMIBFanTrayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 3)
)
panEntityMIBFanTrayGroup.setObjects(
    ("PAN-ENTITY-EXT-MIB", "panEntryFanTrayPowerUsed")
)
if mibBuilder.loadTexts:
    panEntityMIBFanTrayGroup.setStatus("current")

panEntityMIBPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 4)
)
panEntityMIBPowerSupplyGroup.setObjects(
    ("PAN-ENTITY-EXT-MIB", "panEntryPowerSupplyPowerCapacity")
)
if mibBuilder.loadTexts:
    panEntityMIBPowerSupplyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

panEntityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 1, 1)
)
panEntityMIBCompliance.setObjects(
      *(("PAN-ENTITY-EXT-MIB", "panEntityMIBChassisGroup"),
        ("PAN-ENTITY-EXT-MIB", "panEntityMIBFRUModuleGroup"),
        ("PAN-ENTITY-EXT-MIB", "panEntityMIBFanTrayGroup"),
        ("PAN-ENTITY-EXT-MIB", "panEntityMIBPowerSupplyGroup"))
)
if mibBuilder.loadTexts:
    panEntityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-ENTITY-EXT-MIB",
    **{"panEntityMIBModule": panEntityMIBModule,
       "panEntityMIBObjects": panEntityMIBObjects,
       "panEntityChassisGroup": panEntityChassisGroup,
       "panEntityTotalPowerAvail": panEntityTotalPowerAvail,
       "panEntityTotalPowerUsed": panEntityTotalPowerUsed,
       "panEntityFRUModuleGroup": panEntityFRUModuleGroup,
       "panEntityFRUModuleTable": panEntityFRUModuleTable,
       "panEntityFRUModuleEntry": panEntityFRUModuleEntry,
       "panEntryFRUModulePowerUsed": panEntryFRUModulePowerUsed,
       "panEntryFRUModuleNumPorts": panEntryFRUModuleNumPorts,
       "panEntityFanTrayGroup": panEntityFanTrayGroup,
       "panEntityFanTrayTable": panEntityFanTrayTable,
       "panEntityFanTrayEntry": panEntityFanTrayEntry,
       "panEntryFanTrayPowerUsed": panEntryFanTrayPowerUsed,
       "panEntityPowerSupplyGroup": panEntityPowerSupplyGroup,
       "panEntityPowerSupplyTable": panEntityPowerSupplyTable,
       "panEntityPowerSupplyEntry": panEntityPowerSupplyEntry,
       "panEntryPowerSupplyPowerCapacity": panEntryPowerSupplyPowerCapacity,
       "panEntityMIBConformance": panEntityMIBConformance,
       "panEntityMIBCompliances": panEntityMIBCompliances,
       "panEntityMIBCompliance": panEntityMIBCompliance,
       "panEntityMIBGroups": panEntityMIBGroups,
       "panEntityMIBChassisGroup": panEntityMIBChassisGroup,
       "panEntityMIBFRUModuleGroup": panEntityMIBFRUModuleGroup,
       "panEntityMIBFanTrayGroup": panEntityMIBFanTrayGroup,
       "panEntityMIBPowerSupplyGroup": panEntityMIBPowerSupplyGroup}
)
