# SNMP MIB module (VUTLAN-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vutlan\VUTLAN-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:46 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vutlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39052)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtlUnit_ObjectIdentity = ObjectIdentity
ctlUnit = _CtlUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 1)
)
_CtlUnitModulesTable_Object = MibTable
ctlUnitModulesTable = _CtlUnitModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1)
)
if mibBuilder.loadTexts:
    ctlUnitModulesTable.setStatus("current")
_CtlUnitModulesEntry_Object = MibTableRow
ctlUnitModulesEntry = _CtlUnitModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1)
)
ctlUnitModulesEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlUnitModuleId"),
)
if mibBuilder.loadTexts:
    ctlUnitModulesEntry.setStatus("current")
_CtlUnitModuleId_Type = Integer32
_CtlUnitModuleId_Object = MibTableColumn
ctlUnitModuleId = _CtlUnitModuleId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 1),
    _CtlUnitModuleId_Type()
)
ctlUnitModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleId.setStatus("current")
_CtlUnitModulePcode_Type = Integer32
_CtlUnitModulePcode_Object = MibTableColumn
ctlUnitModulePcode = _CtlUnitModulePcode_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 2),
    _CtlUnitModulePcode_Type()
)
ctlUnitModulePcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModulePcode.setStatus("current")
_CtlUnitModuleSN_Type = Integer32
_CtlUnitModuleSN_Object = MibTableColumn
ctlUnitModuleSN = _CtlUnitModuleSN_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 3),
    _CtlUnitModuleSN_Type()
)
ctlUnitModuleSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleSN.setStatus("current")
_CtlUnitModuleClass_Type = OctetString
_CtlUnitModuleClass_Object = MibTableColumn
ctlUnitModuleClass = _CtlUnitModuleClass_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 4),
    _CtlUnitModuleClass_Type()
)
ctlUnitModuleClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleClass.setStatus("current")
_CtlUnitModuleType_Type = OctetString
_CtlUnitModuleType_Object = MibTableColumn
ctlUnitModuleType = _CtlUnitModuleType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 5),
    _CtlUnitModuleType_Type()
)
ctlUnitModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleType.setStatus("current")


class _CtlUnitModuleName_Type(OctetString):
    """Custom type ctlUnitModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlUnitModuleName_Type.__name__ = "OctetString"
_CtlUnitModuleName_Object = MibTableColumn
ctlUnitModuleName = _CtlUnitModuleName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 6),
    _CtlUnitModuleName_Type()
)
ctlUnitModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitModuleName.setStatus("current")
_CtlUnitModuleState_Type = OctetString
_CtlUnitModuleState_Object = MibTableColumn
ctlUnitModuleState = _CtlUnitModuleState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 7),
    _CtlUnitModuleState_Type()
)
ctlUnitModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleState.setStatus("current")
_CtlUnitGroupsTable_Object = MibTable
ctlUnitGroupsTable = _CtlUnitGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2)
)
if mibBuilder.loadTexts:
    ctlUnitGroupsTable.setStatus("current")
_CtlUnitGroupsEntry_Object = MibTableRow
ctlUnitGroupsEntry = _CtlUnitGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1)
)
ctlUnitGroupsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlUnitGroupId"),
)
if mibBuilder.loadTexts:
    ctlUnitGroupsEntry.setStatus("current")
_CtlUnitGroupId_Type = Integer32
_CtlUnitGroupId_Object = MibTableColumn
ctlUnitGroupId = _CtlUnitGroupId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1, 1),
    _CtlUnitGroupId_Type()
)
ctlUnitGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitGroupId.setStatus("current")


class _CtlUnitGroupName_Type(OctetString):
    """Custom type ctlUnitGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlUnitGroupName_Type.__name__ = "OctetString"
_CtlUnitGroupName_Object = MibTableColumn
ctlUnitGroupName = _CtlUnitGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1, 2),
    _CtlUnitGroupName_Type()
)
ctlUnitGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitGroupName.setStatus("current")


class _CtlUnitGroupDesc_Type(OctetString):
    """Custom type ctlUnitGroupDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CtlUnitGroupDesc_Type.__name__ = "OctetString"
_CtlUnitGroupDesc_Object = MibTableColumn
ctlUnitGroupDesc = _CtlUnitGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1, 3),
    _CtlUnitGroupDesc_Type()
)
ctlUnitGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitGroupDesc.setStatus("current")
_CtlUnitElementsTable_Object = MibTable
ctlUnitElementsTable = _CtlUnitElementsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3)
)
if mibBuilder.loadTexts:
    ctlUnitElementsTable.setStatus("current")
_CtlUnitElementsEntry_Object = MibTableRow
ctlUnitElementsEntry = _CtlUnitElementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1)
)
ctlUnitElementsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlUnitElementId"),
)
if mibBuilder.loadTexts:
    ctlUnitElementsEntry.setStatus("current")
_CtlUnitElementId_Type = Integer32
_CtlUnitElementId_Object = MibTableColumn
ctlUnitElementId = _CtlUnitElementId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 1),
    _CtlUnitElementId_Type()
)
ctlUnitElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementId.setStatus("current")
_CtlUnitElementGroup_Type = Integer32
_CtlUnitElementGroup_Object = MibTableColumn
ctlUnitElementGroup = _CtlUnitElementGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 2),
    _CtlUnitElementGroup_Type()
)
ctlUnitElementGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitElementGroup.setStatus("current")
_CtlUnitElementModule_Type = Integer32
_CtlUnitElementModule_Object = MibTableColumn
ctlUnitElementModule = _CtlUnitElementModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 3),
    _CtlUnitElementModule_Type()
)
ctlUnitElementModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementModule.setStatus("current")
_CtlUnitElementNum_Type = Integer32
_CtlUnitElementNum_Object = MibTableColumn
ctlUnitElementNum = _CtlUnitElementNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 4),
    _CtlUnitElementNum_Type()
)
ctlUnitElementNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementNum.setStatus("current")
_CtlUnitElementClass_Type = OctetString
_CtlUnitElementClass_Object = MibTableColumn
ctlUnitElementClass = _CtlUnitElementClass_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 5),
    _CtlUnitElementClass_Type()
)
ctlUnitElementClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementClass.setStatus("current")
_CtlUnitElementType_Type = OctetString
_CtlUnitElementType_Object = MibTableColumn
ctlUnitElementType = _CtlUnitElementType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 6),
    _CtlUnitElementType_Type()
)
ctlUnitElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementType.setStatus("current")


class _CtlUnitElementName_Type(OctetString):
    """Custom type ctlUnitElementName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlUnitElementName_Type.__name__ = "OctetString"
_CtlUnitElementName_Object = MibTableColumn
ctlUnitElementName = _CtlUnitElementName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 7),
    _CtlUnitElementName_Type()
)
ctlUnitElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitElementName.setStatus("current")
_CtlUnitElementState_Type = OctetString
_CtlUnitElementState_Object = MibTableColumn
ctlUnitElementState = _CtlUnitElementState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 8),
    _CtlUnitElementState_Type()
)
ctlUnitElementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementState.setStatus("current")
_CtlUnitElementValue_Type = OctetString
_CtlUnitElementValue_Object = MibTableColumn
ctlUnitElementValue = _CtlUnitElementValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 9),
    _CtlUnitElementValue_Type()
)
ctlUnitElementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementValue.setStatus("current")
_CtlUnitElementSpec_Type = OctetString
_CtlUnitElementSpec_Object = MibTableColumn
ctlUnitElementSpec = _CtlUnitElementSpec_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 10),
    _CtlUnitElementSpec_Type()
)
ctlUnitElementSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementSpec.setStatus("current")
_CtlUnitLogicsTable_Object = MibTable
ctlUnitLogicsTable = _CtlUnitLogicsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4)
)
if mibBuilder.loadTexts:
    ctlUnitLogicsTable.setStatus("current")
_CtlUnitLogicsEntry_Object = MibTableRow
ctlUnitLogicsEntry = _CtlUnitLogicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1)
)
ctlUnitLogicsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlUnitLogicId"),
)
if mibBuilder.loadTexts:
    ctlUnitLogicsEntry.setStatus("current")
_CtlUnitLogicId_Type = Integer32
_CtlUnitLogicId_Object = MibTableColumn
ctlUnitLogicId = _CtlUnitLogicId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 1),
    _CtlUnitLogicId_Type()
)
ctlUnitLogicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitLogicId.setStatus("current")


class _CtlUnitLogicName_Type(OctetString):
    """Custom type ctlUnitLogicName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlUnitLogicName_Type.__name__ = "OctetString"
_CtlUnitLogicName_Object = MibTableColumn
ctlUnitLogicName = _CtlUnitLogicName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 2),
    _CtlUnitLogicName_Type()
)
ctlUnitLogicName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicName.setStatus("current")


class _CtlUnitLogicDesc_Type(OctetString):
    """Custom type ctlUnitLogicDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlUnitLogicDesc_Type.__name__ = "OctetString"
_CtlUnitLogicDesc_Object = MibTableColumn
ctlUnitLogicDesc = _CtlUnitLogicDesc_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 3),
    _CtlUnitLogicDesc_Type()
)
ctlUnitLogicDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicDesc.setStatus("current")
_CtlUnitLogicDisable_Type = Integer32
_CtlUnitLogicDisable_Object = MibTableColumn
ctlUnitLogicDisable = _CtlUnitLogicDisable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 4),
    _CtlUnitLogicDisable_Type()
)
ctlUnitLogicDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicDisable.setStatus("current")
_CtlUnitLogicRowStatus_Type = Integer32
_CtlUnitLogicRowStatus_Object = MibTableColumn
ctlUnitLogicRowStatus = _CtlUnitLogicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 5),
    _CtlUnitLogicRowStatus_Type()
)
ctlUnitLogicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicRowStatus.setStatus("current")
_MacroLogicDefinition_Type = OctetString
_MacroLogicDefinition_Object = MibScalar
macroLogicDefinition = _MacroLogicDefinition_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 1),
    _MacroLogicDefinition_Type()
)
macroLogicDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroLogicDefinition.setStatus("current")
_MacroStateOfSensors_Type = OctetString
_MacroStateOfSensors_Object = MibScalar
macroStateOfSensors = _MacroStateOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 2),
    _MacroStateOfSensors_Type()
)
macroStateOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroStateOfSensors.setStatus("current")
_MacroDateAndTime_Type = OctetString
_MacroDateAndTime_Object = MibScalar
macroDateAndTime = _MacroDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 3),
    _MacroDateAndTime_Type()
)
macroDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroDateAndTime.setStatus("current")
_MacroLogicName_Type = OctetString
_MacroLogicName_Object = MibScalar
macroLogicName = _MacroLogicName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 4),
    _MacroLogicName_Type()
)
macroLogicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroLogicName.setStatus("current")
_MacroSensorName_Type = OctetString
_MacroSensorName_Object = MibScalar
macroSensorName = _MacroSensorName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 5),
    _MacroSensorName_Type()
)
macroSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroSensorName.setStatus("current")
_MacroSensorState_Type = OctetString
_MacroSensorState_Object = MibScalar
macroSensorState = _MacroSensorState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 6),
    _MacroSensorState_Type()
)
macroSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroSensorState.setStatus("current")
_MacroSensorValue_Type = OctetString
_MacroSensorValue_Object = MibScalar
macroSensorValue = _MacroSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 7),
    _MacroSensorValue_Type()
)
macroSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroSensorValue.setStatus("current")
_MacroLastModifiedSensorID_Type = Unsigned32
_MacroLastModifiedSensorID_Object = MibScalar
macroLastModifiedSensorID = _MacroLastModifiedSensorID_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 8),
    _MacroLastModifiedSensorID_Type()
)
macroLastModifiedSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macroLastModifiedSensorID.setStatus("current")
_TrapID_Type = Unsigned32
_TrapID_Object = MibScalar
trapID = _TrapID_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 20),
    _TrapID_Type()
)
trapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapID.setStatus("current")
_TrapName_Type = OctetString
_TrapName_Object = MibScalar
trapName = _TrapName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5, 21),
    _TrapName_Type()
)
trapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapName.setStatus("current")
_CtlUnitSaveToFlash_Type = Integer32
_CtlUnitSaveToFlash_Object = MibScalar
ctlUnitSaveToFlash = _CtlUnitSaveToFlash_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 6),
    _CtlUnitSaveToFlash_Type()
)
ctlUnitSaveToFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitSaveToFlash.setStatus("current")
_CtlUnitSystem_ObjectIdentity = ObjectIdentity
ctlUnitSystem = _CtlUnitSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7)
)
_SystemDevType_Type = OctetString
_SystemDevType_Object = MibScalar
systemDevType = _SystemDevType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 1),
    _SystemDevType_Type()
)
systemDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDevType.setStatus("current")
_SystemFirmware_Type = OctetString
_SystemFirmware_Object = MibScalar
systemFirmware = _SystemFirmware_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 2),
    _SystemFirmware_Type()
)
systemFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFirmware.setStatus("current")
_SystemKernel_Type = OctetString
_SystemKernel_Object = MibScalar
systemKernel = _SystemKernel_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 3),
    _SystemKernel_Type()
)
systemKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemKernel.setStatus("current")
_SystemOpTime_Type = OctetString
_SystemOpTime_Object = MibScalar
systemOpTime = _SystemOpTime_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 4),
    _SystemOpTime_Type()
)
systemOpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOpTime.setStatus("current")
_SystemUpTime_Type = OctetString
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 5),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")
_SystemCpuUsage_Type = OctetString
_SystemCpuUsage_Object = MibScalar
systemCpuUsage = _SystemCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 6),
    _SystemCpuUsage_Type()
)
systemCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCpuUsage.setStatus("current")
_SystemMemUsage_Type = OctetString
_SystemMemUsage_Object = MibScalar
systemMemUsage = _SystemMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 7),
    _SystemMemUsage_Type()
)
systemMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMemUsage.setStatus("current")
_SystemState_Type = OctetString
_SystemState_Object = MibScalar
systemState = _SystemState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 8),
    _SystemState_Type()
)
systemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemState.setStatus("current")


class _SystemHostname_Type(OctetString):
    """Custom type systemHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemHostname_Type.__name__ = "OctetString"
_SystemHostname_Object = MibScalar
systemHostname = _SystemHostname_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 9),
    _SystemHostname_Type()
)
systemHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemHostname.setStatus("current")


class _SystemDescSN_Type(OctetString):
    """Custom type systemDescSN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemDescSN_Type.__name__ = "OctetString"
_SystemDescSN_Object = MibScalar
systemDescSN = _SystemDescSN_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 10),
    _SystemDescSN_Type()
)
systemDescSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDescSN.setStatus("current")


class _SystemDescContacts_Type(OctetString):
    """Custom type systemDescContacts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SystemDescContacts_Type.__name__ = "OctetString"
_SystemDescContacts_Object = MibScalar
systemDescContacts = _SystemDescContacts_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 11),
    _SystemDescContacts_Type()
)
systemDescContacts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDescContacts.setStatus("current")


class _SystemDescLocation_Type(OctetString):
    """Custom type systemDescLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SystemDescLocation_Type.__name__ = "OctetString"
_SystemDescLocation_Object = MibScalar
systemDescLocation = _SystemDescLocation_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 12),
    _SystemDescLocation_Type()
)
systemDescLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDescLocation.setStatus("current")


class _SystemDescComment_Type(OctetString):
    """Custom type systemDescComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SystemDescComment_Type.__name__ = "OctetString"
_SystemDescComment_Object = MibScalar
systemDescComment = _SystemDescComment_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 13),
    _SystemDescComment_Type()
)
systemDescComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDescComment.setStatus("current")


class _SystemMAC_Type(OctetString):
    """Custom type systemMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemMAC_Type.__name__ = "OctetString"
_SystemMAC_Object = MibScalar
systemMAC = _SystemMAC_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 7, 14),
    _SystemMAC_Type()
)
systemMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMAC.setStatus("current")
_CtlUnitReboot_Type = Integer32
_CtlUnitReboot_Object = MibScalar
ctlUnitReboot = _CtlUnitReboot_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 8),
    _CtlUnitReboot_Type()
)
ctlUnitReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitReboot.setStatus("current")
_CtlNotifiers_ObjectIdentity = ObjectIdentity
ctlNotifiers = _CtlNotifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 2)
)
_CtlNotifiersMailersTable_Object = MibTable
ctlNotifiersMailersTable = _CtlNotifiersMailersTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1)
)
if mibBuilder.loadTexts:
    ctlNotifiersMailersTable.setStatus("current")
_CtlNotifiersMailersEntry_Object = MibTableRow
ctlNotifiersMailersEntry = _CtlNotifiersMailersEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1)
)
ctlNotifiersMailersEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlNotifiersMailerId"),
)
if mibBuilder.loadTexts:
    ctlNotifiersMailersEntry.setStatus("current")
_CtlNotifiersMailerId_Type = Integer32
_CtlNotifiersMailerId_Object = MibTableColumn
ctlNotifiersMailerId = _CtlNotifiersMailerId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 1),
    _CtlNotifiersMailerId_Type()
)
ctlNotifiersMailerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerId.setStatus("current")
_CtlNotifiersMailerModule_Type = Integer32
_CtlNotifiersMailerModule_Object = MibTableColumn
ctlNotifiersMailerModule = _CtlNotifiersMailerModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 2),
    _CtlNotifiersMailerModule_Type()
)
ctlNotifiersMailerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerModule.setStatus("current")
_CtlNotifiersMailerNum_Type = Integer32
_CtlNotifiersMailerNum_Object = MibTableColumn
ctlNotifiersMailerNum = _CtlNotifiersMailerNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 3),
    _CtlNotifiersMailerNum_Type()
)
ctlNotifiersMailerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerNum.setStatus("current")
_CtlNotifiersMailerType_Type = OctetString
_CtlNotifiersMailerType_Object = MibTableColumn
ctlNotifiersMailerType = _CtlNotifiersMailerType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 4),
    _CtlNotifiersMailerType_Type()
)
ctlNotifiersMailerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerType.setStatus("current")


class _CtlNotifiersMailerName_Type(OctetString):
    """Custom type ctlNotifiersMailerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersMailerName_Type.__name__ = "OctetString"
_CtlNotifiersMailerName_Object = MibTableColumn
ctlNotifiersMailerName = _CtlNotifiersMailerName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 5),
    _CtlNotifiersMailerName_Type()
)
ctlNotifiersMailerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerName.setStatus("current")
_CtlNotifiersMailerState_Type = OctetString
_CtlNotifiersMailerState_Object = MibTableColumn
ctlNotifiersMailerState = _CtlNotifiersMailerState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 6),
    _CtlNotifiersMailerState_Type()
)
ctlNotifiersMailerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerState.setStatus("current")
_CtlNotifiersMailerValue_Type = OctetString
_CtlNotifiersMailerValue_Object = MibTableColumn
ctlNotifiersMailerValue = _CtlNotifiersMailerValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 7),
    _CtlNotifiersMailerValue_Type()
)
ctlNotifiersMailerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerValue.setStatus("current")


class _CtlNotifiersMailerServer_Type(OctetString):
    """Custom type ctlNotifiersMailerServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlNotifiersMailerServer_Type.__name__ = "OctetString"
_CtlNotifiersMailerServer_Object = MibTableColumn
ctlNotifiersMailerServer = _CtlNotifiersMailerServer_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 8),
    _CtlNotifiersMailerServer_Type()
)
ctlNotifiersMailerServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerServer.setStatus("current")
_CtlNotifiersMailerPort_Type = Integer32
_CtlNotifiersMailerPort_Object = MibTableColumn
ctlNotifiersMailerPort = _CtlNotifiersMailerPort_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 9),
    _CtlNotifiersMailerPort_Type()
)
ctlNotifiersMailerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerPort.setStatus("current")


class _CtlNotifiersMailerLogin_Type(OctetString):
    """Custom type ctlNotifiersMailerLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersMailerLogin_Type.__name__ = "OctetString"
_CtlNotifiersMailerLogin_Object = MibTableColumn
ctlNotifiersMailerLogin = _CtlNotifiersMailerLogin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 10),
    _CtlNotifiersMailerLogin_Type()
)
ctlNotifiersMailerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerLogin.setStatus("current")
_CtlNotifiersMailerPassword_Type = Integer32
_CtlNotifiersMailerPassword_Object = MibTableColumn
ctlNotifiersMailerPassword = _CtlNotifiersMailerPassword_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 11),
    _CtlNotifiersMailerPassword_Type()
)
ctlNotifiersMailerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerPassword.setStatus("current")


class _CtlNotifiersMailersTo_Type(OctetString):
    """Custom type ctlNotifiersMailersTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersMailersTo_Type.__name__ = "OctetString"
_CtlNotifiersMailersTo_Object = MibTableColumn
ctlNotifiersMailersTo = _CtlNotifiersMailersTo_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 12),
    _CtlNotifiersMailersTo_Type()
)
ctlNotifiersMailersTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailersTo.setStatus("current")


class _CtlNotifiersMailersFrom_Type(OctetString):
    """Custom type ctlNotifiersMailersFrom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 512),
    )


_CtlNotifiersMailersFrom_Type.__name__ = "OctetString"
_CtlNotifiersMailersFrom_Object = MibTableColumn
ctlNotifiersMailersFrom = _CtlNotifiersMailersFrom_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 13),
    _CtlNotifiersMailersFrom_Type()
)
ctlNotifiersMailersFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailersFrom.setStatus("current")
_CtlNotifiersMailerMessage_Type = Integer32
_CtlNotifiersMailerMessage_Object = MibTableColumn
ctlNotifiersMailerMessage = _CtlNotifiersMailerMessage_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 14),
    _CtlNotifiersMailerMessage_Type()
)
ctlNotifiersMailerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerMessage.setStatus("current")
_CtlNotifiersTrapsTable_Object = MibTable
ctlNotifiersTrapsTable = _CtlNotifiersTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2)
)
if mibBuilder.loadTexts:
    ctlNotifiersTrapsTable.setStatus("current")
_CtlNotifiersTrapsEntry_Object = MibTableRow
ctlNotifiersTrapsEntry = _CtlNotifiersTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1)
)
ctlNotifiersTrapsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlNotifiersTrapId"),
)
if mibBuilder.loadTexts:
    ctlNotifiersTrapsEntry.setStatus("current")
_CtlNotifiersTrapId_Type = Integer32
_CtlNotifiersTrapId_Object = MibTableColumn
ctlNotifiersTrapId = _CtlNotifiersTrapId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 1),
    _CtlNotifiersTrapId_Type()
)
ctlNotifiersTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapId.setStatus("current")
_CtlNotifiersTrapModule_Type = Integer32
_CtlNotifiersTrapModule_Object = MibTableColumn
ctlNotifiersTrapModule = _CtlNotifiersTrapModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 2),
    _CtlNotifiersTrapModule_Type()
)
ctlNotifiersTrapModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapModule.setStatus("current")
_CtlNotifiersTrapNum_Type = Integer32
_CtlNotifiersTrapNum_Object = MibTableColumn
ctlNotifiersTrapNum = _CtlNotifiersTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 3),
    _CtlNotifiersTrapNum_Type()
)
ctlNotifiersTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapNum.setStatus("current")
_CtlNotifiersTrapType_Type = OctetString
_CtlNotifiersTrapType_Object = MibTableColumn
ctlNotifiersTrapType = _CtlNotifiersTrapType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 4),
    _CtlNotifiersTrapType_Type()
)
ctlNotifiersTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapType.setStatus("current")
_CtlNotifiersTrapName_Type = OctetString
_CtlNotifiersTrapName_Object = MibTableColumn
ctlNotifiersTrapName = _CtlNotifiersTrapName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 5),
    _CtlNotifiersTrapName_Type()
)
ctlNotifiersTrapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapName.setStatus("current")
_CtlNotifiersTrapState_Type = OctetString
_CtlNotifiersTrapState_Object = MibTableColumn
ctlNotifiersTrapState = _CtlNotifiersTrapState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 6),
    _CtlNotifiersTrapState_Type()
)
ctlNotifiersTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapState.setStatus("current")
_CtlNotifiersTrapValue_Type = OctetString
_CtlNotifiersTrapValue_Object = MibTableColumn
ctlNotifiersTrapValue = _CtlNotifiersTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 7),
    _CtlNotifiersTrapValue_Type()
)
ctlNotifiersTrapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapValue.setStatus("current")


class _CtlNotifiersTrapServer_Type(OctetString):
    """Custom type ctlNotifiersTrapServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersTrapServer_Type.__name__ = "OctetString"
_CtlNotifiersTrapServer_Object = MibTableColumn
ctlNotifiersTrapServer = _CtlNotifiersTrapServer_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 8),
    _CtlNotifiersTrapServer_Type()
)
ctlNotifiersTrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapServer.setStatus("current")
_CtlNotifiersTrapPort_Type = Integer32
_CtlNotifiersTrapPort_Object = MibTableColumn
ctlNotifiersTrapPort = _CtlNotifiersTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 9),
    _CtlNotifiersTrapPort_Type()
)
ctlNotifiersTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapPort.setStatus("current")


class _CtlNotifiersTrapVersion_Type(OctetString):
    """Custom type ctlNotifiersTrapVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_CtlNotifiersTrapVersion_Type.__name__ = "OctetString"
_CtlNotifiersTrapVersion_Object = MibTableColumn
ctlNotifiersTrapVersion = _CtlNotifiersTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 10),
    _CtlNotifiersTrapVersion_Type()
)
ctlNotifiersTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapVersion.setStatus("current")


class _CtlNotifiersTrapCommunity_Type(OctetString):
    """Custom type ctlNotifiersTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_CtlNotifiersTrapCommunity_Type.__name__ = "OctetString"
_CtlNotifiersTrapCommunity_Object = MibTableColumn
ctlNotifiersTrapCommunity = _CtlNotifiersTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 11),
    _CtlNotifiersTrapCommunity_Type()
)
ctlNotifiersTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapCommunity.setStatus("current")
_CtlNotifiersSMSsTable_Object = MibTable
ctlNotifiersSMSsTable = _CtlNotifiersSMSsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3)
)
if mibBuilder.loadTexts:
    ctlNotifiersSMSsTable.setStatus("current")
_CtlNotifiersSMSsEntry_Object = MibTableRow
ctlNotifiersSMSsEntry = _CtlNotifiersSMSsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1)
)
ctlNotifiersSMSsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlNotifiersSMSId"),
)
if mibBuilder.loadTexts:
    ctlNotifiersSMSsEntry.setStatus("current")
_CtlNotifiersSMSId_Type = Integer32
_CtlNotifiersSMSId_Object = MibTableColumn
ctlNotifiersSMSId = _CtlNotifiersSMSId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 1),
    _CtlNotifiersSMSId_Type()
)
ctlNotifiersSMSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSId.setStatus("current")
_CtlNotifiersSMSModule_Type = Integer32
_CtlNotifiersSMSModule_Object = MibTableColumn
ctlNotifiersSMSModule = _CtlNotifiersSMSModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 2),
    _CtlNotifiersSMSModule_Type()
)
ctlNotifiersSMSModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSModule.setStatus("current")
_CtlNotifiersSMSNum_Type = Integer32
_CtlNotifiersSMSNum_Object = MibTableColumn
ctlNotifiersSMSNum = _CtlNotifiersSMSNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 3),
    _CtlNotifiersSMSNum_Type()
)
ctlNotifiersSMSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSNum.setStatus("current")
_CtlNotifiersSMSType_Type = OctetString
_CtlNotifiersSMSType_Object = MibTableColumn
ctlNotifiersSMSType = _CtlNotifiersSMSType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 4),
    _CtlNotifiersSMSType_Type()
)
ctlNotifiersSMSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSType.setStatus("current")


class _CtlNotifiersSMSName_Type(OctetString):
    """Custom type ctlNotifiersSMSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersSMSName_Type.__name__ = "OctetString"
_CtlNotifiersSMSName_Object = MibTableColumn
ctlNotifiersSMSName = _CtlNotifiersSMSName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 5),
    _CtlNotifiersSMSName_Type()
)
ctlNotifiersSMSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSName.setStatus("current")
_CtlNotifiersSMSState_Type = OctetString
_CtlNotifiersSMSState_Object = MibTableColumn
ctlNotifiersSMSState = _CtlNotifiersSMSState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 6),
    _CtlNotifiersSMSState_Type()
)
ctlNotifiersSMSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSState.setStatus("current")
_CtlNotifiersSMSValue_Type = Integer32
_CtlNotifiersSMSValue_Object = MibTableColumn
ctlNotifiersSMSValue = _CtlNotifiersSMSValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 7),
    _CtlNotifiersSMSValue_Type()
)
ctlNotifiersSMSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSValue.setStatus("current")


class _CtlNotifiersSMSTo_Type(OctetString):
    """Custom type ctlNotifiersSMSTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 256),
    )


_CtlNotifiersSMSTo_Type.__name__ = "OctetString"
_CtlNotifiersSMSTo_Object = MibTableColumn
ctlNotifiersSMSTo = _CtlNotifiersSMSTo_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 8),
    _CtlNotifiersSMSTo_Type()
)
ctlNotifiersSMSTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSTo.setStatus("current")


class _CtlNotifiersSMSMessage_Type(OctetString):
    """Custom type ctlNotifiersSMSMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 512),
    )


_CtlNotifiersSMSMessage_Type.__name__ = "OctetString"
_CtlNotifiersSMSMessage_Object = MibTableColumn
ctlNotifiersSMSMessage = _CtlNotifiersSMSMessage_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 9),
    _CtlNotifiersSMSMessage_Type()
)
ctlNotifiersSMSMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSMessage.setStatus("current")
_CtlVirtualDevices_ObjectIdentity = ObjectIdentity
ctlVirtualDevices = _CtlVirtualDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 3)
)
_CtlVirtualDevicesTimersTable_Object = MibTable
ctlVirtualDevicesTimersTable = _CtlVirtualDevicesTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1)
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimersTable.setStatus("current")
_CtlVirtualDevicesTimersEntry_Object = MibTableRow
ctlVirtualDevicesTimersEntry = _CtlVirtualDevicesTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1)
)
ctlVirtualDevicesTimersEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlVirtualDevicesTimerId"),
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimersEntry.setStatus("current")
_CtlVirtualDevicesTimerId_Type = Integer32
_CtlVirtualDevicesTimerId_Object = MibTableColumn
ctlVirtualDevicesTimerId = _CtlVirtualDevicesTimerId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 1),
    _CtlVirtualDevicesTimerId_Type()
)
ctlVirtualDevicesTimerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerId.setStatus("current")
_CtlVirtualDevicesTimerModule_Type = Integer32
_CtlVirtualDevicesTimerModule_Object = MibTableColumn
ctlVirtualDevicesTimerModule = _CtlVirtualDevicesTimerModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 2),
    _CtlVirtualDevicesTimerModule_Type()
)
ctlVirtualDevicesTimerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerModule.setStatus("current")
_CtlVirtualDevicesTimerNum_Type = Integer32
_CtlVirtualDevicesTimerNum_Object = MibTableColumn
ctlVirtualDevicesTimerNum = _CtlVirtualDevicesTimerNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 3),
    _CtlVirtualDevicesTimerNum_Type()
)
ctlVirtualDevicesTimerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerNum.setStatus("current")
_CtlVirtualDevicesTimerType_Type = OctetString
_CtlVirtualDevicesTimerType_Object = MibTableColumn
ctlVirtualDevicesTimerType = _CtlVirtualDevicesTimerType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 4),
    _CtlVirtualDevicesTimerType_Type()
)
ctlVirtualDevicesTimerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerType.setStatus("current")


class _CtlVirtualDevicesTimerName_Type(OctetString):
    """Custom type ctlVirtualDevicesTimerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlVirtualDevicesTimerName_Type.__name__ = "OctetString"
_CtlVirtualDevicesTimerName_Object = MibTableColumn
ctlVirtualDevicesTimerName = _CtlVirtualDevicesTimerName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 5),
    _CtlVirtualDevicesTimerName_Type()
)
ctlVirtualDevicesTimerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerName.setStatus("current")
_CtlVirtualDevicesTimerState_Type = OctetString
_CtlVirtualDevicesTimerState_Object = MibTableColumn
ctlVirtualDevicesTimerState = _CtlVirtualDevicesTimerState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 6),
    _CtlVirtualDevicesTimerState_Type()
)
ctlVirtualDevicesTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerState.setStatus("current")
_CtlVirtualDevicesTimerValue_Type = OctetString
_CtlVirtualDevicesTimerValue_Object = MibTableColumn
ctlVirtualDevicesTimerValue = _CtlVirtualDevicesTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 7),
    _CtlVirtualDevicesTimerValue_Type()
)
ctlVirtualDevicesTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerValue.setStatus("current")
_CtlVirtualDevicesTimerBegin_Type = OctetString
_CtlVirtualDevicesTimerBegin_Object = MibTableColumn
ctlVirtualDevicesTimerBegin = _CtlVirtualDevicesTimerBegin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 8),
    _CtlVirtualDevicesTimerBegin_Type()
)
ctlVirtualDevicesTimerBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerBegin.setStatus("current")
_CtlVirtualDevicesTimerEnd_Type = OctetString
_CtlVirtualDevicesTimerEnd_Object = MibTableColumn
ctlVirtualDevicesTimerEnd = _CtlVirtualDevicesTimerEnd_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 9),
    _CtlVirtualDevicesTimerEnd_Type()
)
ctlVirtualDevicesTimerEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerEnd.setStatus("current")
_CtlVirtualDevicesTimerDays_Type = OctetString
_CtlVirtualDevicesTimerDays_Object = MibTableColumn
ctlVirtualDevicesTimerDays = _CtlVirtualDevicesTimerDays_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 10),
    _CtlVirtualDevicesTimerDays_Type()
)
ctlVirtualDevicesTimerDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerDays.setStatus("current")
_CtlVirtualDevicesTimerMode_Type = OctetString
_CtlVirtualDevicesTimerMode_Object = MibTableColumn
ctlVirtualDevicesTimerMode = _CtlVirtualDevicesTimerMode_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 11),
    _CtlVirtualDevicesTimerMode_Type()
)
ctlVirtualDevicesTimerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerMode.setStatus("current")


class _CtlVirtualDevicesTimerDayPattern_Type(OctetString):
    """Custom type ctlVirtualDevicesTimerDayPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CtlVirtualDevicesTimerDayPattern_Type.__name__ = "OctetString"
_CtlVirtualDevicesTimerDayPattern_Object = MibTableColumn
ctlVirtualDevicesTimerDayPattern = _CtlVirtualDevicesTimerDayPattern_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 12),
    _CtlVirtualDevicesTimerDayPattern_Type()
)
ctlVirtualDevicesTimerDayPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerDayPattern.setStatus("current")
_CtlVirtualDevicesPingsTable_Object = MibTable
ctlVirtualDevicesPingsTable = _CtlVirtualDevicesPingsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2)
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingsTable.setStatus("current")
_CtlVirtualDevicesPingsEntry_Object = MibTableRow
ctlVirtualDevicesPingsEntry = _CtlVirtualDevicesPingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1)
)
ctlVirtualDevicesPingsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlVirtualDevicesPingId"),
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingsEntry.setStatus("current")
_CtlVirtualDevicesPingId_Type = Integer32
_CtlVirtualDevicesPingId_Object = MibTableColumn
ctlVirtualDevicesPingId = _CtlVirtualDevicesPingId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 1),
    _CtlVirtualDevicesPingId_Type()
)
ctlVirtualDevicesPingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingId.setStatus("current")
_CtlVirtualDevicesPingModule_Type = Integer32
_CtlVirtualDevicesPingModule_Object = MibTableColumn
ctlVirtualDevicesPingModule = _CtlVirtualDevicesPingModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 2),
    _CtlVirtualDevicesPingModule_Type()
)
ctlVirtualDevicesPingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingModule.setStatus("current")
_CtlVirtualDevicesPingNum_Type = Integer32
_CtlVirtualDevicesPingNum_Object = MibTableColumn
ctlVirtualDevicesPingNum = _CtlVirtualDevicesPingNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 3),
    _CtlVirtualDevicesPingNum_Type()
)
ctlVirtualDevicesPingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingNum.setStatus("current")
_CtlVirtualDevicesPingType_Type = OctetString
_CtlVirtualDevicesPingType_Object = MibTableColumn
ctlVirtualDevicesPingType = _CtlVirtualDevicesPingType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 4),
    _CtlVirtualDevicesPingType_Type()
)
ctlVirtualDevicesPingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingType.setStatus("current")


class _CtlVirtualDevicesPingName_Type(OctetString):
    """Custom type ctlVirtualDevicesPingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlVirtualDevicesPingName_Type.__name__ = "OctetString"
_CtlVirtualDevicesPingName_Object = MibTableColumn
ctlVirtualDevicesPingName = _CtlVirtualDevicesPingName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 5),
    _CtlVirtualDevicesPingName_Type()
)
ctlVirtualDevicesPingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingName.setStatus("current")
_CtlVirtualDevicesPingState_Type = OctetString
_CtlVirtualDevicesPingState_Object = MibTableColumn
ctlVirtualDevicesPingState = _CtlVirtualDevicesPingState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 6),
    _CtlVirtualDevicesPingState_Type()
)
ctlVirtualDevicesPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingState.setStatus("current")
_CtlVirtualDevicesPingValue_Type = OctetString
_CtlVirtualDevicesPingValue_Object = MibTableColumn
ctlVirtualDevicesPingValue = _CtlVirtualDevicesPingValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 7),
    _CtlVirtualDevicesPingValue_Type()
)
ctlVirtualDevicesPingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingValue.setStatus("current")
_CtlVirtualDevicesPingPeriod_Type = Integer32
_CtlVirtualDevicesPingPeriod_Object = MibTableColumn
ctlVirtualDevicesPingPeriod = _CtlVirtualDevicesPingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 8),
    _CtlVirtualDevicesPingPeriod_Type()
)
ctlVirtualDevicesPingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingPeriod.setStatus("current")
_CtlVirtualDevicesPingRTT_Type = Integer32
_CtlVirtualDevicesPingRTT_Object = MibTableColumn
ctlVirtualDevicesPingRTT = _CtlVirtualDevicesPingRTT_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 9),
    _CtlVirtualDevicesPingRTT_Type()
)
ctlVirtualDevicesPingRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingRTT.setStatus("current")


class _CtlVirtualDevicesPingServer_Type(OctetString):
    """Custom type ctlVirtualDevicesPingServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlVirtualDevicesPingServer_Type.__name__ = "OctetString"
_CtlVirtualDevicesPingServer_Object = MibTableColumn
ctlVirtualDevicesPingServer = _CtlVirtualDevicesPingServer_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 10),
    _CtlVirtualDevicesPingServer_Type()
)
ctlVirtualDevicesPingServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingServer.setStatus("current")
_CtlVirtualDevicesPingIP_Type = OctetString
_CtlVirtualDevicesPingIP_Object = MibTableColumn
ctlVirtualDevicesPingIP = _CtlVirtualDevicesPingIP_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 11),
    _CtlVirtualDevicesPingIP_Type()
)
ctlVirtualDevicesPingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingIP.setStatus("current")
_CtlVirtualDevicesPingSent_Type = Integer32
_CtlVirtualDevicesPingSent_Object = MibTableColumn
ctlVirtualDevicesPingSent = _CtlVirtualDevicesPingSent_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 12),
    _CtlVirtualDevicesPingSent_Type()
)
ctlVirtualDevicesPingSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingSent.setStatus("current")
_CtlVirtualDevicesPingReceived_Type = Integer32
_CtlVirtualDevicesPingReceived_Object = MibTableColumn
ctlVirtualDevicesPingReceived = _CtlVirtualDevicesPingReceived_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 13),
    _CtlVirtualDevicesPingReceived_Type()
)
ctlVirtualDevicesPingReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingReceived.setStatus("current")
_CtlVirtualDevicesPingStatus_Type = OctetString
_CtlVirtualDevicesPingStatus_Object = MibTableColumn
ctlVirtualDevicesPingStatus = _CtlVirtualDevicesPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 14),
    _CtlVirtualDevicesPingStatus_Type()
)
ctlVirtualDevicesPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingStatus.setStatus("current")
_CtlVirtualDevicesTriggersTable_Object = MibTable
ctlVirtualDevicesTriggersTable = _CtlVirtualDevicesTriggersTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3)
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggersTable.setStatus("current")
_CtlVirtualDevicesTriggersEntry_Object = MibTableRow
ctlVirtualDevicesTriggersEntry = _CtlVirtualDevicesTriggersEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1)
)
ctlVirtualDevicesTriggersEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlVirtualDevicesTriggerId"),
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggersEntry.setStatus("current")
_CtlVirtualDevicesTriggerId_Type = Integer32
_CtlVirtualDevicesTriggerId_Object = MibTableColumn
ctlVirtualDevicesTriggerId = _CtlVirtualDevicesTriggerId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 1),
    _CtlVirtualDevicesTriggerId_Type()
)
ctlVirtualDevicesTriggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerId.setStatus("current")
_CtlVirtualDevicesTriggerModule_Type = Integer32
_CtlVirtualDevicesTriggerModule_Object = MibTableColumn
ctlVirtualDevicesTriggerModule = _CtlVirtualDevicesTriggerModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 2),
    _CtlVirtualDevicesTriggerModule_Type()
)
ctlVirtualDevicesTriggerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerModule.setStatus("current")
_CtlVirtualDevicesTriggerNum_Type = Integer32
_CtlVirtualDevicesTriggerNum_Object = MibTableColumn
ctlVirtualDevicesTriggerNum = _CtlVirtualDevicesTriggerNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 3),
    _CtlVirtualDevicesTriggerNum_Type()
)
ctlVirtualDevicesTriggerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerNum.setStatus("current")
_CtlVirtualDevicesTriggerType_Type = OctetString
_CtlVirtualDevicesTriggerType_Object = MibTableColumn
ctlVirtualDevicesTriggerType = _CtlVirtualDevicesTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 4),
    _CtlVirtualDevicesTriggerType_Type()
)
ctlVirtualDevicesTriggerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerType.setStatus("current")


class _CtlVirtualDevicesTriggerName_Type(OctetString):
    """Custom type ctlVirtualDevicesTriggerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlVirtualDevicesTriggerName_Type.__name__ = "OctetString"
_CtlVirtualDevicesTriggerName_Object = MibTableColumn
ctlVirtualDevicesTriggerName = _CtlVirtualDevicesTriggerName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 5),
    _CtlVirtualDevicesTriggerName_Type()
)
ctlVirtualDevicesTriggerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerName.setStatus("current")
_CtlVirtualDevicesTriggerState_Type = OctetString
_CtlVirtualDevicesTriggerState_Object = MibTableColumn
ctlVirtualDevicesTriggerState = _CtlVirtualDevicesTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 6),
    _CtlVirtualDevicesTriggerState_Type()
)
ctlVirtualDevicesTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerState.setStatus("current")
_CtlVirtualDevicesTriggerValue_Type = OctetString
_CtlVirtualDevicesTriggerValue_Object = MibTableColumn
ctlVirtualDevicesTriggerValue = _CtlVirtualDevicesTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 7),
    _CtlVirtualDevicesTriggerValue_Type()
)
ctlVirtualDevicesTriggerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerValue.setStatus("current")
_CtlVirtualDevicesTriggerReverse_Type = Integer32
_CtlVirtualDevicesTriggerReverse_Object = MibTableColumn
ctlVirtualDevicesTriggerReverse = _CtlVirtualDevicesTriggerReverse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 3, 1, 8),
    _CtlVirtualDevicesTriggerReverse_Type()
)
ctlVirtualDevicesTriggerReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTriggerReverse.setStatus("current")
_CtlVirtualDevicesSnmpgetsTable_Object = MibTable
ctlVirtualDevicesSnmpgetsTable = _CtlVirtualDevicesSnmpgetsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4)
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetsTable.setStatus("current")
_CtlVirtualDevicesSnmpgetsEntry_Object = MibTableRow
ctlVirtualDevicesSnmpgetsEntry = _CtlVirtualDevicesSnmpgetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1)
)
ctlVirtualDevicesSnmpgetsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlVirtualDevicesSnmpgetId"),
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetsEntry.setStatus("current")
_CtlVirtualDevicesSnmpgetId_Type = Integer32
_CtlVirtualDevicesSnmpgetId_Object = MibTableColumn
ctlVirtualDevicesSnmpgetId = _CtlVirtualDevicesSnmpgetId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 1),
    _CtlVirtualDevicesSnmpgetId_Type()
)
ctlVirtualDevicesSnmpgetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetId.setStatus("current")
_CtlVirtualDevicesSnmpgetModule_Type = Integer32
_CtlVirtualDevicesSnmpgetModule_Object = MibTableColumn
ctlVirtualDevicesSnmpgetModule = _CtlVirtualDevicesSnmpgetModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 2),
    _CtlVirtualDevicesSnmpgetModule_Type()
)
ctlVirtualDevicesSnmpgetModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetModule.setStatus("current")
_CtlVirtualDevicesSnmpgetNum_Type = Integer32
_CtlVirtualDevicesSnmpgetNum_Object = MibTableColumn
ctlVirtualDevicesSnmpgetNum = _CtlVirtualDevicesSnmpgetNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 3),
    _CtlVirtualDevicesSnmpgetNum_Type()
)
ctlVirtualDevicesSnmpgetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetNum.setStatus("current")
_CtlVirtualDevicesSnmpgetType_Type = OctetString
_CtlVirtualDevicesSnmpgetType_Object = MibTableColumn
ctlVirtualDevicesSnmpgetType = _CtlVirtualDevicesSnmpgetType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 4),
    _CtlVirtualDevicesSnmpgetType_Type()
)
ctlVirtualDevicesSnmpgetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetType.setStatus("current")


class _CtlVirtualDevicesSnmpgetName_Type(OctetString):
    """Custom type ctlVirtualDevicesSnmpgetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlVirtualDevicesSnmpgetName_Type.__name__ = "OctetString"
_CtlVirtualDevicesSnmpgetName_Object = MibTableColumn
ctlVirtualDevicesSnmpgetName = _CtlVirtualDevicesSnmpgetName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 5),
    _CtlVirtualDevicesSnmpgetName_Type()
)
ctlVirtualDevicesSnmpgetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetName.setStatus("current")
_CtlVirtualDevicesSnmpgetState_Type = OctetString
_CtlVirtualDevicesSnmpgetState_Object = MibTableColumn
ctlVirtualDevicesSnmpgetState = _CtlVirtualDevicesSnmpgetState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 6),
    _CtlVirtualDevicesSnmpgetState_Type()
)
ctlVirtualDevicesSnmpgetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetState.setStatus("current")
_CtlVirtualDevicesSnmpgetValue_Type = OctetString
_CtlVirtualDevicesSnmpgetValue_Object = MibTableColumn
ctlVirtualDevicesSnmpgetValue = _CtlVirtualDevicesSnmpgetValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 7),
    _CtlVirtualDevicesSnmpgetValue_Type()
)
ctlVirtualDevicesSnmpgetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetValue.setStatus("current")
_CtlVirtualDevicesSnmpgetStatus_Type = OctetString
_CtlVirtualDevicesSnmpgetStatus_Object = MibTableColumn
ctlVirtualDevicesSnmpgetStatus = _CtlVirtualDevicesSnmpgetStatus_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 8),
    _CtlVirtualDevicesSnmpgetStatus_Type()
)
ctlVirtualDevicesSnmpgetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetStatus.setStatus("current")
_CtlVirtualDevicesSnmpgetPeriod_Type = Integer32
_CtlVirtualDevicesSnmpgetPeriod_Object = MibTableColumn
ctlVirtualDevicesSnmpgetPeriod = _CtlVirtualDevicesSnmpgetPeriod_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 9),
    _CtlVirtualDevicesSnmpgetPeriod_Type()
)
ctlVirtualDevicesSnmpgetPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetPeriod.setStatus("current")
_CtlVirtualDevicesSnmpgetServer_Type = OctetString
_CtlVirtualDevicesSnmpgetServer_Object = MibTableColumn
ctlVirtualDevicesSnmpgetServer = _CtlVirtualDevicesSnmpgetServer_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 10),
    _CtlVirtualDevicesSnmpgetServer_Type()
)
ctlVirtualDevicesSnmpgetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetServer.setStatus("current")
_CtlVirtualDevicesSnmpgetPort_Type = Integer32
_CtlVirtualDevicesSnmpgetPort_Object = MibTableColumn
ctlVirtualDevicesSnmpgetPort = _CtlVirtualDevicesSnmpgetPort_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 11),
    _CtlVirtualDevicesSnmpgetPort_Type()
)
ctlVirtualDevicesSnmpgetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetPort.setStatus("current")
_CtlVirtualDevicesSnmpgetCommunity_Type = OctetString
_CtlVirtualDevicesSnmpgetCommunity_Object = MibTableColumn
ctlVirtualDevicesSnmpgetCommunity = _CtlVirtualDevicesSnmpgetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 12),
    _CtlVirtualDevicesSnmpgetCommunity_Type()
)
ctlVirtualDevicesSnmpgetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetCommunity.setStatus("current")
_CtlVirtualDevicesSnmpgetOid_Type = OctetString
_CtlVirtualDevicesSnmpgetOid_Object = MibTableColumn
ctlVirtualDevicesSnmpgetOid = _CtlVirtualDevicesSnmpgetOid_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 13),
    _CtlVirtualDevicesSnmpgetOid_Type()
)
ctlVirtualDevicesSnmpgetOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetOid.setStatus("current")
_CtlVirtualDevicesSnmpgetVartype_Type = OctetString
_CtlVirtualDevicesSnmpgetVartype_Object = MibTableColumn
ctlVirtualDevicesSnmpgetVartype = _CtlVirtualDevicesSnmpgetVartype_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 14),
    _CtlVirtualDevicesSnmpgetVartype_Type()
)
ctlVirtualDevicesSnmpgetVartype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetVartype.setStatus("current")
_CtlVirtualDevicesSnmpgetLowAlarm_Type = OctetString
_CtlVirtualDevicesSnmpgetLowAlarm_Object = MibTableColumn
ctlVirtualDevicesSnmpgetLowAlarm = _CtlVirtualDevicesSnmpgetLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 15),
    _CtlVirtualDevicesSnmpgetLowAlarm_Type()
)
ctlVirtualDevicesSnmpgetLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetLowAlarm.setStatus("current")
_CtlVirtualDevicesSnmpgetLowWarning_Type = OctetString
_CtlVirtualDevicesSnmpgetLowWarning_Object = MibTableColumn
ctlVirtualDevicesSnmpgetLowWarning = _CtlVirtualDevicesSnmpgetLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 16),
    _CtlVirtualDevicesSnmpgetLowWarning_Type()
)
ctlVirtualDevicesSnmpgetLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetLowWarning.setStatus("current")
_CtlVirtualDevicesSnmpgetHighWarning_Type = OctetString
_CtlVirtualDevicesSnmpgetHighWarning_Object = MibTableColumn
ctlVirtualDevicesSnmpgetHighWarning = _CtlVirtualDevicesSnmpgetHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 17),
    _CtlVirtualDevicesSnmpgetHighWarning_Type()
)
ctlVirtualDevicesSnmpgetHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetHighWarning.setStatus("current")
_CtlVirtualDevicesSnmpgetHighAlarm_Type = OctetString
_CtlVirtualDevicesSnmpgetHighAlarm_Object = MibTableColumn
ctlVirtualDevicesSnmpgetHighAlarm = _CtlVirtualDevicesSnmpgetHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 18),
    _CtlVirtualDevicesSnmpgetHighAlarm_Type()
)
ctlVirtualDevicesSnmpgetHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetHighAlarm.setStatus("current")
_CtlVirtualDevicesSnmpgetExpression_Type = OctetString
_CtlVirtualDevicesSnmpgetExpression_Object = MibTableColumn
ctlVirtualDevicesSnmpgetExpression = _CtlVirtualDevicesSnmpgetExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 4, 1, 19),
    _CtlVirtualDevicesSnmpgetExpression_Type()
)
ctlVirtualDevicesSnmpgetExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesSnmpgetExpression.setStatus("current")
_CtlVirtualDevicesAnalogsTable_Object = MibTable
ctlVirtualDevicesAnalogsTable = _CtlVirtualDevicesAnalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5)
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogsTable.setStatus("current")
_CtlVirtualDevicesAnalogsEntry_Object = MibTableRow
ctlVirtualDevicesAnalogsEntry = _CtlVirtualDevicesAnalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1)
)
ctlVirtualDevicesAnalogsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlVirtualDevicesAnalogId"),
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogsEntry.setStatus("current")
_CtlVirtualDevicesAnalogId_Type = Integer32
_CtlVirtualDevicesAnalogId_Object = MibTableColumn
ctlVirtualDevicesAnalogId = _CtlVirtualDevicesAnalogId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 1),
    _CtlVirtualDevicesAnalogId_Type()
)
ctlVirtualDevicesAnalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogId.setStatus("current")
_CtlVirtualDevicesAnalogModule_Type = Integer32
_CtlVirtualDevicesAnalogModule_Object = MibTableColumn
ctlVirtualDevicesAnalogModule = _CtlVirtualDevicesAnalogModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 2),
    _CtlVirtualDevicesAnalogModule_Type()
)
ctlVirtualDevicesAnalogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogModule.setStatus("current")
_CtlVirtualDevicesAnalogNum_Type = Integer32
_CtlVirtualDevicesAnalogNum_Object = MibTableColumn
ctlVirtualDevicesAnalogNum = _CtlVirtualDevicesAnalogNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 3),
    _CtlVirtualDevicesAnalogNum_Type()
)
ctlVirtualDevicesAnalogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogNum.setStatus("current")
_CtlVirtualDevicesAnalogType_Type = OctetString
_CtlVirtualDevicesAnalogType_Object = MibTableColumn
ctlVirtualDevicesAnalogType = _CtlVirtualDevicesAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 4),
    _CtlVirtualDevicesAnalogType_Type()
)
ctlVirtualDevicesAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogType.setStatus("current")


class _CtlVirtualDevicesAnalogName_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlVirtualDevicesAnalogName_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogName_Object = MibTableColumn
ctlVirtualDevicesAnalogName = _CtlVirtualDevicesAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 5),
    _CtlVirtualDevicesAnalogName_Type()
)
ctlVirtualDevicesAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogName.setStatus("current")
_CtlVirtualDevicesAnalogState_Type = OctetString
_CtlVirtualDevicesAnalogState_Object = MibTableColumn
ctlVirtualDevicesAnalogState = _CtlVirtualDevicesAnalogState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 6),
    _CtlVirtualDevicesAnalogState_Type()
)
ctlVirtualDevicesAnalogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogState.setStatus("current")
_CtlVirtualDevicesAnalogValue_Type = OctetString
_CtlVirtualDevicesAnalogValue_Object = MibTableColumn
ctlVirtualDevicesAnalogValue = _CtlVirtualDevicesAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 7),
    _CtlVirtualDevicesAnalogValue_Type()
)
ctlVirtualDevicesAnalogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogValue.setStatus("current")
_CtlVirtualDevicesAnalogMin_Type = OctetString
_CtlVirtualDevicesAnalogMin_Object = MibTableColumn
ctlVirtualDevicesAnalogMin = _CtlVirtualDevicesAnalogMin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 8),
    _CtlVirtualDevicesAnalogMin_Type()
)
ctlVirtualDevicesAnalogMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogMin.setStatus("current")
_CtlVirtualDevicesAnalogMax_Type = OctetString
_CtlVirtualDevicesAnalogMax_Object = MibTableColumn
ctlVirtualDevicesAnalogMax = _CtlVirtualDevicesAnalogMax_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 9),
    _CtlVirtualDevicesAnalogMax_Type()
)
ctlVirtualDevicesAnalogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogMax.setStatus("current")


class _CtlVirtualDevicesAnalogLowAlarm_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogLowAlarm_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogLowAlarm_Object = MibTableColumn
ctlVirtualDevicesAnalogLowAlarm = _CtlVirtualDevicesAnalogLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 10),
    _CtlVirtualDevicesAnalogLowAlarm_Type()
)
ctlVirtualDevicesAnalogLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogLowAlarm.setStatus("current")


class _CtlVirtualDevicesAnalogLowWarning_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogLowWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogLowWarning_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogLowWarning_Object = MibTableColumn
ctlVirtualDevicesAnalogLowWarning = _CtlVirtualDevicesAnalogLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 11),
    _CtlVirtualDevicesAnalogLowWarning_Type()
)
ctlVirtualDevicesAnalogLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogLowWarning.setStatus("current")


class _CtlVirtualDevicesAnalogHighWarning_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogHighWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogHighWarning_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogHighWarning_Object = MibTableColumn
ctlVirtualDevicesAnalogHighWarning = _CtlVirtualDevicesAnalogHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 12),
    _CtlVirtualDevicesAnalogHighWarning_Type()
)
ctlVirtualDevicesAnalogHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHighWarning.setStatus("current")


class _CtlVirtualDevicesAnalogHighAlarm_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogHighAlarm_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogHighAlarm_Object = MibTableColumn
ctlVirtualDevicesAnalogHighAlarm = _CtlVirtualDevicesAnalogHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 13),
    _CtlVirtualDevicesAnalogHighAlarm_Type()
)
ctlVirtualDevicesAnalogHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHighAlarm.setStatus("current")


class _CtlVirtualDevicesAnalogAt0_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogAt0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogAt0_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogAt0_Object = MibTableColumn
ctlVirtualDevicesAnalogAt0 = _CtlVirtualDevicesAnalogAt0_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 14),
    _CtlVirtualDevicesAnalogAt0_Type()
)
ctlVirtualDevicesAnalogAt0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogAt0.setStatus("current")


class _CtlVirtualDevicesAnalogAt75_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogAt75 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogAt75_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogAt75_Object = MibTableColumn
ctlVirtualDevicesAnalogAt75 = _CtlVirtualDevicesAnalogAt75_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 15),
    _CtlVirtualDevicesAnalogAt75_Type()
)
ctlVirtualDevicesAnalogAt75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogAt75.setStatus("current")


class _CtlVirtualDevicesAnalogExpression_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CtlVirtualDevicesAnalogExpression_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogExpression_Object = MibTableColumn
ctlVirtualDevicesAnalogExpression = _CtlVirtualDevicesAnalogExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 16),
    _CtlVirtualDevicesAnalogExpression_Type()
)
ctlVirtualDevicesAnalogExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogExpression.setStatus("current")
_CtlVirtualDevicesAnalogSpecific_Type = OctetString
_CtlVirtualDevicesAnalogSpecific_Object = MibTableColumn
ctlVirtualDevicesAnalogSpecific = _CtlVirtualDevicesAnalogSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 17),
    _CtlVirtualDevicesAnalogSpecific_Type()
)
ctlVirtualDevicesAnalogSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogSpecific.setStatus("current")


class _CtlVirtualDevicesAnalogHystType_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogHystType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogHystType_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogHystType_Object = MibTableColumn
ctlVirtualDevicesAnalogHystType = _CtlVirtualDevicesAnalogHystType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 18),
    _CtlVirtualDevicesAnalogHystType_Type()
)
ctlVirtualDevicesAnalogHystType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHystType.setStatus("current")


class _CtlVirtualDevicesAnalogHystValue_Type(OctetString):
    """Custom type ctlVirtualDevicesAnalogHystValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlVirtualDevicesAnalogHystValue_Type.__name__ = "OctetString"
_CtlVirtualDevicesAnalogHystValue_Object = MibTableColumn
ctlVirtualDevicesAnalogHystValue = _CtlVirtualDevicesAnalogHystValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 19),
    _CtlVirtualDevicesAnalogHystValue_Type()
)
ctlVirtualDevicesAnalogHystValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHystValue.setStatus("current")
_CtlVirtualDevicesAnalogHystLowAlarm_Type = Integer32
_CtlVirtualDevicesAnalogHystLowAlarm_Object = MibTableColumn
ctlVirtualDevicesAnalogHystLowAlarm = _CtlVirtualDevicesAnalogHystLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 20),
    _CtlVirtualDevicesAnalogHystLowAlarm_Type()
)
ctlVirtualDevicesAnalogHystLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHystLowAlarm.setStatus("current")
_CtlVirtualDevicesAnalogHystLowWarning_Type = Integer32
_CtlVirtualDevicesAnalogHystLowWarning_Object = MibTableColumn
ctlVirtualDevicesAnalogHystLowWarning = _CtlVirtualDevicesAnalogHystLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 21),
    _CtlVirtualDevicesAnalogHystLowWarning_Type()
)
ctlVirtualDevicesAnalogHystLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHystLowWarning.setStatus("current")
_CtlVirtualDevicesAnalogHystNormal_Type = Integer32
_CtlVirtualDevicesAnalogHystNormal_Object = MibTableColumn
ctlVirtualDevicesAnalogHystNormal = _CtlVirtualDevicesAnalogHystNormal_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 22),
    _CtlVirtualDevicesAnalogHystNormal_Type()
)
ctlVirtualDevicesAnalogHystNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHystNormal.setStatus("current")
_CtlVirtualDevicesAnalogHystHighWarning_Type = Integer32
_CtlVirtualDevicesAnalogHystHighWarning_Object = MibTableColumn
ctlVirtualDevicesAnalogHystHighWarning = _CtlVirtualDevicesAnalogHystHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 23),
    _CtlVirtualDevicesAnalogHystHighWarning_Type()
)
ctlVirtualDevicesAnalogHystHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHystHighWarning.setStatus("current")
_CtlVirtualDevicesAnalogHystHighAlarm_Type = Integer32
_CtlVirtualDevicesAnalogHystHighAlarm_Object = MibTableColumn
ctlVirtualDevicesAnalogHystHighAlarm = _CtlVirtualDevicesAnalogHystHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 24),
    _CtlVirtualDevicesAnalogHystHighAlarm_Type()
)
ctlVirtualDevicesAnalogHystHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogHystHighAlarm.setStatus("current")
_CtlVirtualDevicesAnalogValueInt_Type = Integer32
_CtlVirtualDevicesAnalogValueInt_Object = MibTableColumn
ctlVirtualDevicesAnalogValueInt = _CtlVirtualDevicesAnalogValueInt_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 5, 1, 25),
    _CtlVirtualDevicesAnalogValueInt_Type()
)
ctlVirtualDevicesAnalogValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesAnalogValueInt.setStatus("current")
_CtlHardwareDevices_ObjectIdentity = ObjectIdentity
ctlHardwareDevices = _CtlHardwareDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 4)
)
_CtlHardwareDevicesCamerasTable_Object = MibTable
ctlHardwareDevicesCamerasTable = _CtlHardwareDevicesCamerasTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1)
)
if mibBuilder.loadTexts:
    ctlHardwareDevicesCamerasTable.setStatus("current")
_CtlHardwareDevicesCamerasEntry_Object = MibTableRow
ctlHardwareDevicesCamerasEntry = _CtlHardwareDevicesCamerasEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1)
)
ctlHardwareDevicesCamerasEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlHardwareDevicesCameraId"),
)
if mibBuilder.loadTexts:
    ctlHardwareDevicesCamerasEntry.setStatus("current")
_CtlHardwareDevicesCameraId_Type = Integer32
_CtlHardwareDevicesCameraId_Object = MibTableColumn
ctlHardwareDevicesCameraId = _CtlHardwareDevicesCameraId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 1),
    _CtlHardwareDevicesCameraId_Type()
)
ctlHardwareDevicesCameraId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraId.setStatus("current")
_CtlHardwareDevicesCameraModule_Type = Integer32
_CtlHardwareDevicesCameraModule_Object = MibTableColumn
ctlHardwareDevicesCameraModule = _CtlHardwareDevicesCameraModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 2),
    _CtlHardwareDevicesCameraModule_Type()
)
ctlHardwareDevicesCameraModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraModule.setStatus("current")
_CtlHardwareDevicesCameraNum_Type = Integer32
_CtlHardwareDevicesCameraNum_Object = MibTableColumn
ctlHardwareDevicesCameraNum = _CtlHardwareDevicesCameraNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 3),
    _CtlHardwareDevicesCameraNum_Type()
)
ctlHardwareDevicesCameraNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraNum.setStatus("current")
_CtlHardwareDevicesCameraType_Type = OctetString
_CtlHardwareDevicesCameraType_Object = MibTableColumn
ctlHardwareDevicesCameraType = _CtlHardwareDevicesCameraType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 4),
    _CtlHardwareDevicesCameraType_Type()
)
ctlHardwareDevicesCameraType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraType.setStatus("current")


class _CtlHardwareDevicesCameraName_Type(OctetString):
    """Custom type ctlHardwareDevicesCameraName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlHardwareDevicesCameraName_Type.__name__ = "OctetString"
_CtlHardwareDevicesCameraName_Object = MibTableColumn
ctlHardwareDevicesCameraName = _CtlHardwareDevicesCameraName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 5),
    _CtlHardwareDevicesCameraName_Type()
)
ctlHardwareDevicesCameraName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraName.setStatus("current")
_CtlHardwareDevicesCameraState_Type = OctetString
_CtlHardwareDevicesCameraState_Object = MibTableColumn
ctlHardwareDevicesCameraState = _CtlHardwareDevicesCameraState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 6),
    _CtlHardwareDevicesCameraState_Type()
)
ctlHardwareDevicesCameraState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraState.setStatus("current")
_CtlHardwareDevicesCameraValue_Type = OctetString
_CtlHardwareDevicesCameraValue_Object = MibTableColumn
ctlHardwareDevicesCameraValue = _CtlHardwareDevicesCameraValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 7),
    _CtlHardwareDevicesCameraValue_Type()
)
ctlHardwareDevicesCameraValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraValue.setStatus("current")


class _CtlHardwareDevicesCameraURL_Type(OctetString):
    """Custom type ctlHardwareDevicesCameraURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlHardwareDevicesCameraURL_Type.__name__ = "OctetString"
_CtlHardwareDevicesCameraURL_Object = MibTableColumn
ctlHardwareDevicesCameraURL = _CtlHardwareDevicesCameraURL_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 8),
    _CtlHardwareDevicesCameraURL_Type()
)
ctlHardwareDevicesCameraURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraURL.setStatus("current")
_CtlHardwareDevicesCameraFPS_Type = OctetString
_CtlHardwareDevicesCameraFPS_Object = MibTableColumn
ctlHardwareDevicesCameraFPS = _CtlHardwareDevicesCameraFPS_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 9),
    _CtlHardwareDevicesCameraFPS_Type()
)
ctlHardwareDevicesCameraFPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraFPS.setStatus("current")
_CtlHardwareDevicesCameraResolution_Type = OctetString
_CtlHardwareDevicesCameraResolution_Object = MibTableColumn
ctlHardwareDevicesCameraResolution = _CtlHardwareDevicesCameraResolution_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 10),
    _CtlHardwareDevicesCameraResolution_Type()
)
ctlHardwareDevicesCameraResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraResolution.setStatus("current")
_CtlHardwareDevicesModemsTable_Object = MibTable
ctlHardwareDevicesModemsTable = _CtlHardwareDevicesModemsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 2)
)
if mibBuilder.loadTexts:
    ctlHardwareDevicesModemsTable.setStatus("current")
_CtlHardwareDevicesModemsEntry_Object = MibTableRow
ctlHardwareDevicesModemsEntry = _CtlHardwareDevicesModemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 2, 1)
)
ctlHardwareDevicesModemsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlHardwareDevicesModemState"),
)
if mibBuilder.loadTexts:
    ctlHardwareDevicesModemsEntry.setStatus("current")
_CtlHardwareDevicesModemState_Type = OctetString
_CtlHardwareDevicesModemState_Object = MibTableColumn
ctlHardwareDevicesModemState = _CtlHardwareDevicesModemState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 2, 1, 1),
    _CtlHardwareDevicesModemState_Type()
)
ctlHardwareDevicesModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesModemState.setStatus("current")
_CtlHardwareDevicesModemStatus_Type = OctetString
_CtlHardwareDevicesModemStatus_Object = MibTableColumn
ctlHardwareDevicesModemStatus = _CtlHardwareDevicesModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 2, 1, 2),
    _CtlHardwareDevicesModemStatus_Type()
)
ctlHardwareDevicesModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesModemStatus.setStatus("current")
_CtlHardwareDevicesModemSignal_Type = Integer32
_CtlHardwareDevicesModemSignal_Object = MibTableColumn
ctlHardwareDevicesModemSignal = _CtlHardwareDevicesModemSignal_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 2, 1, 3),
    _CtlHardwareDevicesModemSignal_Type()
)
ctlHardwareDevicesModemSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesModemSignal.setStatus("current")
_CtlHardwareDevicesModemOperator_Type = OctetString
_CtlHardwareDevicesModemOperator_Object = MibTableColumn
ctlHardwareDevicesModemOperator = _CtlHardwareDevicesModemOperator_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 2, 1, 4),
    _CtlHardwareDevicesModemOperator_Type()
)
ctlHardwareDevicesModemOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesModemOperator.setStatus("current")
_CtlHardwareDevicesModemPosition_Type = OctetString
_CtlHardwareDevicesModemPosition_Object = MibTableColumn
ctlHardwareDevicesModemPosition = _CtlHardwareDevicesModemPosition_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 2, 1, 5),
    _CtlHardwareDevicesModemPosition_Type()
)
ctlHardwareDevicesModemPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesModemPosition.setStatus("current")
_CtIInternalSensors_ObjectIdentity = ObjectIdentity
ctIInternalSensors = _CtIInternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 5)
)
_CtlInternalSensorsDiscretsTable_Object = MibTable
ctlInternalSensorsDiscretsTable = _CtlInternalSensorsDiscretsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1)
)
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretsTable.setStatus("current")
_CtlInternalSensorsDiscretsEntry_Object = MibTableRow
ctlInternalSensorsDiscretsEntry = _CtlInternalSensorsDiscretsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1)
)
ctlInternalSensorsDiscretsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlInternalSensorsDiscretId"),
)
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretsEntry.setStatus("current")
_CtlInternalSensorsDiscretId_Type = Integer32
_CtlInternalSensorsDiscretId_Object = MibTableColumn
ctlInternalSensorsDiscretId = _CtlInternalSensorsDiscretId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 1),
    _CtlInternalSensorsDiscretId_Type()
)
ctlInternalSensorsDiscretId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretId.setStatus("current")
_CtlInternalSensorsDiscretModule_Type = Integer32
_CtlInternalSensorsDiscretModule_Object = MibTableColumn
ctlInternalSensorsDiscretModule = _CtlInternalSensorsDiscretModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 2),
    _CtlInternalSensorsDiscretModule_Type()
)
ctlInternalSensorsDiscretModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretModule.setStatus("current")
_CtlInternalSensorsDiscretNum_Type = Integer32
_CtlInternalSensorsDiscretNum_Object = MibTableColumn
ctlInternalSensorsDiscretNum = _CtlInternalSensorsDiscretNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 3),
    _CtlInternalSensorsDiscretNum_Type()
)
ctlInternalSensorsDiscretNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretNum.setStatus("current")
_CtlInternalSensorsDiscretType_Type = OctetString
_CtlInternalSensorsDiscretType_Object = MibTableColumn
ctlInternalSensorsDiscretType = _CtlInternalSensorsDiscretType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 4),
    _CtlInternalSensorsDiscretType_Type()
)
ctlInternalSensorsDiscretType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretType.setStatus("current")


class _CtlInternalSensorsDiscretName_Type(OctetString):
    """Custom type ctlInternalSensorsDiscretName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlInternalSensorsDiscretName_Type.__name__ = "OctetString"
_CtlInternalSensorsDiscretName_Object = MibTableColumn
ctlInternalSensorsDiscretName = _CtlInternalSensorsDiscretName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 5),
    _CtlInternalSensorsDiscretName_Type()
)
ctlInternalSensorsDiscretName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretName.setStatus("current")
_CtlInternalSensorsDiscretState_Type = OctetString
_CtlInternalSensorsDiscretState_Object = MibTableColumn
ctlInternalSensorsDiscretState = _CtlInternalSensorsDiscretState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 6),
    _CtlInternalSensorsDiscretState_Type()
)
ctlInternalSensorsDiscretState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretState.setStatus("current")
_CtlInternalSensorsDiscretValue_Type = Integer32
_CtlInternalSensorsDiscretValue_Object = MibTableColumn
ctlInternalSensorsDiscretValue = _CtlInternalSensorsDiscretValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 7),
    _CtlInternalSensorsDiscretValue_Type()
)
ctlInternalSensorsDiscretValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretValue.setStatus("current")
_CtlInternalSensorsDiscretReset_Type = Integer32
_CtlInternalSensorsDiscretReset_Object = MibTableColumn
ctlInternalSensorsDiscretReset = _CtlInternalSensorsDiscretReset_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 8),
    _CtlInternalSensorsDiscretReset_Type()
)
ctlInternalSensorsDiscretReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretReset.setStatus("current")
_CtlInternalSensorsDiscretLevel_Type = Integer32
_CtlInternalSensorsDiscretLevel_Object = MibTableColumn
ctlInternalSensorsDiscretLevel = _CtlInternalSensorsDiscretLevel_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 9),
    _CtlInternalSensorsDiscretLevel_Type()
)
ctlInternalSensorsDiscretLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretLevel.setStatus("current")
_CtlInternalSensorsDiscretReverse_Type = Integer32
_CtlInternalSensorsDiscretReverse_Object = MibTableColumn
ctlInternalSensorsDiscretReverse = _CtlInternalSensorsDiscretReverse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 10),
    _CtlInternalSensorsDiscretReverse_Type()
)
ctlInternalSensorsDiscretReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretReverse.setStatus("current")
_CtlInternalSensorsDiscretSpecific_Type = OctetString
_CtlInternalSensorsDiscretSpecific_Object = MibTableColumn
ctlInternalSensorsDiscretSpecific = _CtlInternalSensorsDiscretSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 11),
    _CtlInternalSensorsDiscretSpecific_Type()
)
ctlInternalSensorsDiscretSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretSpecific.setStatus("current")
_CtlInternalSensorsAnalogsTable_Object = MibTable
ctlInternalSensorsAnalogsTable = _CtlInternalSensorsAnalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2)
)
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogsTable.setStatus("current")
_CtlInternalSensorsAnalogsEntry_Object = MibTableRow
ctlInternalSensorsAnalogsEntry = _CtlInternalSensorsAnalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1)
)
ctlInternalSensorsAnalogsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlInternalSensorsAnalogId"),
)
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogsEntry.setStatus("current")
_CtlInternalSensorsAnalogId_Type = Integer32
_CtlInternalSensorsAnalogId_Object = MibTableColumn
ctlInternalSensorsAnalogId = _CtlInternalSensorsAnalogId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 1),
    _CtlInternalSensorsAnalogId_Type()
)
ctlInternalSensorsAnalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogId.setStatus("current")
_CtlInternalSensorsAnalogModule_Type = Integer32
_CtlInternalSensorsAnalogModule_Object = MibTableColumn
ctlInternalSensorsAnalogModule = _CtlInternalSensorsAnalogModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 2),
    _CtlInternalSensorsAnalogModule_Type()
)
ctlInternalSensorsAnalogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogModule.setStatus("current")
_CtlInternalSensorsAnalogNum_Type = Integer32
_CtlInternalSensorsAnalogNum_Object = MibTableColumn
ctlInternalSensorsAnalogNum = _CtlInternalSensorsAnalogNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 3),
    _CtlInternalSensorsAnalogNum_Type()
)
ctlInternalSensorsAnalogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogNum.setStatus("current")
_CtlInternalSensorsAnalogType_Type = OctetString
_CtlInternalSensorsAnalogType_Object = MibTableColumn
ctlInternalSensorsAnalogType = _CtlInternalSensorsAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 4),
    _CtlInternalSensorsAnalogType_Type()
)
ctlInternalSensorsAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogType.setStatus("current")


class _CtlInternalSensorsAnalogName_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlInternalSensorsAnalogName_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogName_Object = MibTableColumn
ctlInternalSensorsAnalogName = _CtlInternalSensorsAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 5),
    _CtlInternalSensorsAnalogName_Type()
)
ctlInternalSensorsAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogName.setStatus("current")
_CtlInternalSensorsAnalogState_Type = OctetString
_CtlInternalSensorsAnalogState_Object = MibTableColumn
ctlInternalSensorsAnalogState = _CtlInternalSensorsAnalogState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 6),
    _CtlInternalSensorsAnalogState_Type()
)
ctlInternalSensorsAnalogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogState.setStatus("current")
_CtlInternalSensorsAnalogValue_Type = OctetString
_CtlInternalSensorsAnalogValue_Object = MibTableColumn
ctlInternalSensorsAnalogValue = _CtlInternalSensorsAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 7),
    _CtlInternalSensorsAnalogValue_Type()
)
ctlInternalSensorsAnalogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogValue.setStatus("current")
_CtlInternalSensorsAnalogMin_Type = OctetString
_CtlInternalSensorsAnalogMin_Object = MibTableColumn
ctlInternalSensorsAnalogMin = _CtlInternalSensorsAnalogMin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 8),
    _CtlInternalSensorsAnalogMin_Type()
)
ctlInternalSensorsAnalogMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogMin.setStatus("current")
_CtlInternalSensorsAnalogMax_Type = OctetString
_CtlInternalSensorsAnalogMax_Object = MibTableColumn
ctlInternalSensorsAnalogMax = _CtlInternalSensorsAnalogMax_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 9),
    _CtlInternalSensorsAnalogMax_Type()
)
ctlInternalSensorsAnalogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogMax.setStatus("current")


class _CtlInternalSensorsAnalogLowAlarm_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogLowAlarm_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogLowAlarm_Object = MibTableColumn
ctlInternalSensorsAnalogLowAlarm = _CtlInternalSensorsAnalogLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 10),
    _CtlInternalSensorsAnalogLowAlarm_Type()
)
ctlInternalSensorsAnalogLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogLowAlarm.setStatus("current")


class _CtlInternalSensorsAnalogLowWarning_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogLowWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogLowWarning_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogLowWarning_Object = MibTableColumn
ctlInternalSensorsAnalogLowWarning = _CtlInternalSensorsAnalogLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 11),
    _CtlInternalSensorsAnalogLowWarning_Type()
)
ctlInternalSensorsAnalogLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogLowWarning.setStatus("current")


class _CtlInternalSensorsAnalogHighWarning_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogHighWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogHighWarning_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogHighWarning_Object = MibTableColumn
ctlInternalSensorsAnalogHighWarning = _CtlInternalSensorsAnalogHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 12),
    _CtlInternalSensorsAnalogHighWarning_Type()
)
ctlInternalSensorsAnalogHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHighWarning.setStatus("current")


class _CtlInternalSensorsAnalogHighAlarm_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogHighAlarm_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogHighAlarm_Object = MibTableColumn
ctlInternalSensorsAnalogHighAlarm = _CtlInternalSensorsAnalogHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 13),
    _CtlInternalSensorsAnalogHighAlarm_Type()
)
ctlInternalSensorsAnalogHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHighAlarm.setStatus("current")


class _CtlInternalSensorsAnalogAt0_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogAt0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogAt0_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogAt0_Object = MibTableColumn
ctlInternalSensorsAnalogAt0 = _CtlInternalSensorsAnalogAt0_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 14),
    _CtlInternalSensorsAnalogAt0_Type()
)
ctlInternalSensorsAnalogAt0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogAt0.setStatus("current")


class _CtlInternalSensorsAnalogAt75_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogAt75 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogAt75_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogAt75_Object = MibTableColumn
ctlInternalSensorsAnalogAt75 = _CtlInternalSensorsAnalogAt75_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 15),
    _CtlInternalSensorsAnalogAt75_Type()
)
ctlInternalSensorsAnalogAt75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogAt75.setStatus("current")


class _CtlInternalSensorsAnalogExpression_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CtlInternalSensorsAnalogExpression_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogExpression_Object = MibTableColumn
ctlInternalSensorsAnalogExpression = _CtlInternalSensorsAnalogExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 16),
    _CtlInternalSensorsAnalogExpression_Type()
)
ctlInternalSensorsAnalogExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogExpression.setStatus("current")
_CtlInternalSensorsAnalogSpecific_Type = OctetString
_CtlInternalSensorsAnalogSpecific_Object = MibTableColumn
ctlInternalSensorsAnalogSpecific = _CtlInternalSensorsAnalogSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 17),
    _CtlInternalSensorsAnalogSpecific_Type()
)
ctlInternalSensorsAnalogSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogSpecific.setStatus("current")


class _CtlInternalSensorsAnalogHystType_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogHystType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogHystType_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogHystType_Object = MibTableColumn
ctlInternalSensorsAnalogHystType = _CtlInternalSensorsAnalogHystType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 18),
    _CtlInternalSensorsAnalogHystType_Type()
)
ctlInternalSensorsAnalogHystType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHystType.setStatus("current")


class _CtlInternalSensorsAnalogHystValue_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogHystValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogHystValue_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogHystValue_Object = MibTableColumn
ctlInternalSensorsAnalogHystValue = _CtlInternalSensorsAnalogHystValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 19),
    _CtlInternalSensorsAnalogHystValue_Type()
)
ctlInternalSensorsAnalogHystValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHystValue.setStatus("current")
_CtlInternalSensorsAnalogHystLowAlarm_Type = Integer32
_CtlInternalSensorsAnalogHystLowAlarm_Object = MibTableColumn
ctlInternalSensorsAnalogHystLowAlarm = _CtlInternalSensorsAnalogHystLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 20),
    _CtlInternalSensorsAnalogHystLowAlarm_Type()
)
ctlInternalSensorsAnalogHystLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHystLowAlarm.setStatus("current")
_CtlInternalSensorsAnalogHystLowWarning_Type = Integer32
_CtlInternalSensorsAnalogHystLowWarning_Object = MibTableColumn
ctlInternalSensorsAnalogHystLowWarning = _CtlInternalSensorsAnalogHystLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 21),
    _CtlInternalSensorsAnalogHystLowWarning_Type()
)
ctlInternalSensorsAnalogHystLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHystLowWarning.setStatus("current")
_CtlInternalSensorsAnalogHystNormal_Type = Integer32
_CtlInternalSensorsAnalogHystNormal_Object = MibTableColumn
ctlInternalSensorsAnalogHystNormal = _CtlInternalSensorsAnalogHystNormal_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 22),
    _CtlInternalSensorsAnalogHystNormal_Type()
)
ctlInternalSensorsAnalogHystNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHystNormal.setStatus("current")
_CtlInternalSensorsAnalogHystHighWarning_Type = Integer32
_CtlInternalSensorsAnalogHystHighWarning_Object = MibTableColumn
ctlInternalSensorsAnalogHystHighWarning = _CtlInternalSensorsAnalogHystHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 23),
    _CtlInternalSensorsAnalogHystHighWarning_Type()
)
ctlInternalSensorsAnalogHystHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHystHighWarning.setStatus("current")
_CtlInternalSensorsAnalogHystHighAlarm_Type = Integer32
_CtlInternalSensorsAnalogHystHighAlarm_Object = MibTableColumn
ctlInternalSensorsAnalogHystHighAlarm = _CtlInternalSensorsAnalogHystHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 24),
    _CtlInternalSensorsAnalogHystHighAlarm_Type()
)
ctlInternalSensorsAnalogHystHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHystHighAlarm.setStatus("current")
_CtlInternalSensorsAnalogValueInt_Type = Integer32
_CtlInternalSensorsAnalogValueInt_Object = MibTableColumn
ctlInternalSensorsAnalogValueInt = _CtlInternalSensorsAnalogValueInt_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 25),
    _CtlInternalSensorsAnalogValueInt_Type()
)
ctlInternalSensorsAnalogValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogValueInt.setStatus("current")
_CtlInternalSensorsOutletsTable_Object = MibTable
ctlInternalSensorsOutletsTable = _CtlInternalSensorsOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3)
)
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletsTable.setStatus("current")
_CtlInternalSensorsOutletsEntry_Object = MibTableRow
ctlInternalSensorsOutletsEntry = _CtlInternalSensorsOutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1)
)
ctlInternalSensorsOutletsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlInternalSensorsOutletId"),
)
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletsEntry.setStatus("current")
_CtlInternalSensorsOutletId_Type = Integer32
_CtlInternalSensorsOutletId_Object = MibTableColumn
ctlInternalSensorsOutletId = _CtlInternalSensorsOutletId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 1),
    _CtlInternalSensorsOutletId_Type()
)
ctlInternalSensorsOutletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletId.setStatus("current")
_CtlInternalSensorsOutletModule_Type = Integer32
_CtlInternalSensorsOutletModule_Object = MibTableColumn
ctlInternalSensorsOutletModule = _CtlInternalSensorsOutletModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 2),
    _CtlInternalSensorsOutletModule_Type()
)
ctlInternalSensorsOutletModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletModule.setStatus("current")
_CtlInternalSensorsOutletNum_Type = Integer32
_CtlInternalSensorsOutletNum_Object = MibTableColumn
ctlInternalSensorsOutletNum = _CtlInternalSensorsOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 3),
    _CtlInternalSensorsOutletNum_Type()
)
ctlInternalSensorsOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletNum.setStatus("current")
_CtlInternalSensorsOutletType_Type = OctetString
_CtlInternalSensorsOutletType_Object = MibTableColumn
ctlInternalSensorsOutletType = _CtlInternalSensorsOutletType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 4),
    _CtlInternalSensorsOutletType_Type()
)
ctlInternalSensorsOutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletType.setStatus("current")


class _CtlInternalSensorsOutletName_Type(OctetString):
    """Custom type ctlInternalSensorsOutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlInternalSensorsOutletName_Type.__name__ = "OctetString"
_CtlInternalSensorsOutletName_Object = MibTableColumn
ctlInternalSensorsOutletName = _CtlInternalSensorsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 5),
    _CtlInternalSensorsOutletName_Type()
)
ctlInternalSensorsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletName.setStatus("current")
_CtlInternalSensorsOutletState_Type = OctetString
_CtlInternalSensorsOutletState_Object = MibTableColumn
ctlInternalSensorsOutletState = _CtlInternalSensorsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 6),
    _CtlInternalSensorsOutletState_Type()
)
ctlInternalSensorsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletState.setStatus("current")
_CtlInternalSensorsOutletValue_Type = OctetString
_CtlInternalSensorsOutletValue_Object = MibTableColumn
ctlInternalSensorsOutletValue = _CtlInternalSensorsOutletValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 7),
    _CtlInternalSensorsOutletValue_Type()
)
ctlInternalSensorsOutletValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletValue.setStatus("current")
_CtlInternalSensorsOutletInitial_Type = OctetString
_CtlInternalSensorsOutletInitial_Object = MibTableColumn
ctlInternalSensorsOutletInitial = _CtlInternalSensorsOutletInitial_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 8),
    _CtlInternalSensorsOutletInitial_Type()
)
ctlInternalSensorsOutletInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletInitial.setStatus("current")
_CtlInternalSensorsDiscretPulse_Type = Integer32
_CtlInternalSensorsDiscretPulse_Object = MibTableColumn
ctlInternalSensorsDiscretPulse = _CtlInternalSensorsDiscretPulse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 9),
    _CtlInternalSensorsDiscretPulse_Type()
)
ctlInternalSensorsDiscretPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretPulse.setStatus("current")
_CtlCANSensors_ObjectIdentity = ObjectIdentity
ctlCANSensors = _CtlCANSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 6)
)
_CtlCANSensorsDiscretsTable_Object = MibTable
ctlCANSensorsDiscretsTable = _CtlCANSensorsDiscretsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1)
)
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretsTable.setStatus("current")
_CtlCANSensorsDiscretsEntry_Object = MibTableRow
ctlCANSensorsDiscretsEntry = _CtlCANSensorsDiscretsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1)
)
ctlCANSensorsDiscretsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlCANSensorsDiscretId"),
)
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretsEntry.setStatus("current")
_CtlCANSensorsDiscretId_Type = Integer32
_CtlCANSensorsDiscretId_Object = MibTableColumn
ctlCANSensorsDiscretId = _CtlCANSensorsDiscretId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 1),
    _CtlCANSensorsDiscretId_Type()
)
ctlCANSensorsDiscretId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretId.setStatus("current")
_CtlCANSensorsDiscretModule_Type = Integer32
_CtlCANSensorsDiscretModule_Object = MibTableColumn
ctlCANSensorsDiscretModule = _CtlCANSensorsDiscretModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 2),
    _CtlCANSensorsDiscretModule_Type()
)
ctlCANSensorsDiscretModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretModule.setStatus("current")
_CtlCANSensorsDiscretNum_Type = Integer32
_CtlCANSensorsDiscretNum_Object = MibTableColumn
ctlCANSensorsDiscretNum = _CtlCANSensorsDiscretNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 3),
    _CtlCANSensorsDiscretNum_Type()
)
ctlCANSensorsDiscretNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretNum.setStatus("current")
_CtlCANSensorsDiscretType_Type = OctetString
_CtlCANSensorsDiscretType_Object = MibTableColumn
ctlCANSensorsDiscretType = _CtlCANSensorsDiscretType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 4),
    _CtlCANSensorsDiscretType_Type()
)
ctlCANSensorsDiscretType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretType.setStatus("current")


class _CtlCANSensorsDiscretName_Type(OctetString):
    """Custom type ctlCANSensorsDiscretName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlCANSensorsDiscretName_Type.__name__ = "OctetString"
_CtlCANSensorsDiscretName_Object = MibTableColumn
ctlCANSensorsDiscretName = _CtlCANSensorsDiscretName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 5),
    _CtlCANSensorsDiscretName_Type()
)
ctlCANSensorsDiscretName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretName.setStatus("current")
_CtlCANSensorsDiscretState_Type = OctetString
_CtlCANSensorsDiscretState_Object = MibTableColumn
ctlCANSensorsDiscretState = _CtlCANSensorsDiscretState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 6),
    _CtlCANSensorsDiscretState_Type()
)
ctlCANSensorsDiscretState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretState.setStatus("current")
_CtlCANSensorsDiscretValue_Type = OctetString
_CtlCANSensorsDiscretValue_Object = MibTableColumn
ctlCANSensorsDiscretValue = _CtlCANSensorsDiscretValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 7),
    _CtlCANSensorsDiscretValue_Type()
)
ctlCANSensorsDiscretValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretValue.setStatus("current")
_CtlCANSensorsDiscretReset_Type = Integer32
_CtlCANSensorsDiscretReset_Object = MibTableColumn
ctlCANSensorsDiscretReset = _CtlCANSensorsDiscretReset_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 8),
    _CtlCANSensorsDiscretReset_Type()
)
ctlCANSensorsDiscretReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretReset.setStatus("current")
_CtlCANSensorsDiscretLevel_Type = Integer32
_CtlCANSensorsDiscretLevel_Object = MibTableColumn
ctlCANSensorsDiscretLevel = _CtlCANSensorsDiscretLevel_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 9),
    _CtlCANSensorsDiscretLevel_Type()
)
ctlCANSensorsDiscretLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretLevel.setStatus("current")
_CtlCANSensorsDiscretReverse_Type = Integer32
_CtlCANSensorsDiscretReverse_Object = MibTableColumn
ctlCANSensorsDiscretReverse = _CtlCANSensorsDiscretReverse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 10),
    _CtlCANSensorsDiscretReverse_Type()
)
ctlCANSensorsDiscretReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretReverse.setStatus("current")
_CtlCANSensorsDiscretSpecific_Type = OctetString
_CtlCANSensorsDiscretSpecific_Object = MibTableColumn
ctlCANSensorsDiscretSpecific = _CtlCANSensorsDiscretSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 11),
    _CtlCANSensorsDiscretSpecific_Type()
)
ctlCANSensorsDiscretSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretSpecific.setStatus("current")
_CtlCANSensorsAnalogsTable_Object = MibTable
ctlCANSensorsAnalogsTable = _CtlCANSensorsAnalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2)
)
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogsTable.setStatus("current")
_CtlCANSensorsAnalogsEntry_Object = MibTableRow
ctlCANSensorsAnalogsEntry = _CtlCANSensorsAnalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1)
)
ctlCANSensorsAnalogsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlCANSensorsAnalogId"),
)
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogsEntry.setStatus("current")
_CtlCANSensorsAnalogId_Type = Integer32
_CtlCANSensorsAnalogId_Object = MibTableColumn
ctlCANSensorsAnalogId = _CtlCANSensorsAnalogId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 1),
    _CtlCANSensorsAnalogId_Type()
)
ctlCANSensorsAnalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogId.setStatus("current")
_CtlCANSensorsAnalogModule_Type = Integer32
_CtlCANSensorsAnalogModule_Object = MibTableColumn
ctlCANSensorsAnalogModule = _CtlCANSensorsAnalogModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 2),
    _CtlCANSensorsAnalogModule_Type()
)
ctlCANSensorsAnalogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogModule.setStatus("current")
_CtlCANSensorsAnalogNum_Type = Integer32
_CtlCANSensorsAnalogNum_Object = MibTableColumn
ctlCANSensorsAnalogNum = _CtlCANSensorsAnalogNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 3),
    _CtlCANSensorsAnalogNum_Type()
)
ctlCANSensorsAnalogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogNum.setStatus("current")
_CtlCANSensorsAnalogType_Type = OctetString
_CtlCANSensorsAnalogType_Object = MibTableColumn
ctlCANSensorsAnalogType = _CtlCANSensorsAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 4),
    _CtlCANSensorsAnalogType_Type()
)
ctlCANSensorsAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogType.setStatus("current")


class _CtlCANSensorsAnalogName_Type(OctetString):
    """Custom type ctlCANSensorsAnalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlCANSensorsAnalogName_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogName_Object = MibTableColumn
ctlCANSensorsAnalogName = _CtlCANSensorsAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 5),
    _CtlCANSensorsAnalogName_Type()
)
ctlCANSensorsAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogName.setStatus("current")
_CtlCANSensorsAnalogState_Type = OctetString
_CtlCANSensorsAnalogState_Object = MibTableColumn
ctlCANSensorsAnalogState = _CtlCANSensorsAnalogState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 6),
    _CtlCANSensorsAnalogState_Type()
)
ctlCANSensorsAnalogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogState.setStatus("current")
_CtlCANSensorsAnalogValue_Type = OctetString
_CtlCANSensorsAnalogValue_Object = MibTableColumn
ctlCANSensorsAnalogValue = _CtlCANSensorsAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 7),
    _CtlCANSensorsAnalogValue_Type()
)
ctlCANSensorsAnalogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogValue.setStatus("current")
_CtlCANSensorsAnalogMin_Type = OctetString
_CtlCANSensorsAnalogMin_Object = MibTableColumn
ctlCANSensorsAnalogMin = _CtlCANSensorsAnalogMin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 8),
    _CtlCANSensorsAnalogMin_Type()
)
ctlCANSensorsAnalogMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogMin.setStatus("current")
_CtlCANSensorsAnalogMax_Type = OctetString
_CtlCANSensorsAnalogMax_Object = MibTableColumn
ctlCANSensorsAnalogMax = _CtlCANSensorsAnalogMax_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 9),
    _CtlCANSensorsAnalogMax_Type()
)
ctlCANSensorsAnalogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogMax.setStatus("current")


class _CtlCANSensorsAnalogLowAlarm_Type(OctetString):
    """Custom type ctlCANSensorsAnalogLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogLowAlarm_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogLowAlarm_Object = MibTableColumn
ctlCANSensorsAnalogLowAlarm = _CtlCANSensorsAnalogLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 10),
    _CtlCANSensorsAnalogLowAlarm_Type()
)
ctlCANSensorsAnalogLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogLowAlarm.setStatus("current")


class _CtlCANSensorsAnalogLowWarning_Type(OctetString):
    """Custom type ctlCANSensorsAnalogLowWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogLowWarning_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogLowWarning_Object = MibTableColumn
ctlCANSensorsAnalogLowWarning = _CtlCANSensorsAnalogLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 11),
    _CtlCANSensorsAnalogLowWarning_Type()
)
ctlCANSensorsAnalogLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogLowWarning.setStatus("current")


class _CtlCANSensorsAnalogHighWarning_Type(OctetString):
    """Custom type ctlCANSensorsAnalogHighWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogHighWarning_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogHighWarning_Object = MibTableColumn
ctlCANSensorsAnalogHighWarning = _CtlCANSensorsAnalogHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 12),
    _CtlCANSensorsAnalogHighWarning_Type()
)
ctlCANSensorsAnalogHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHighWarning.setStatus("current")


class _CtlCANSensorsAnalogHighAlarm_Type(OctetString):
    """Custom type ctlCANSensorsAnalogHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogHighAlarm_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogHighAlarm_Object = MibTableColumn
ctlCANSensorsAnalogHighAlarm = _CtlCANSensorsAnalogHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 13),
    _CtlCANSensorsAnalogHighAlarm_Type()
)
ctlCANSensorsAnalogHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHighAlarm.setStatus("current")


class _CtlCANSensorsAnalogAt0_Type(OctetString):
    """Custom type ctlCANSensorsAnalogAt0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogAt0_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogAt0_Object = MibTableColumn
ctlCANSensorsAnalogAt0 = _CtlCANSensorsAnalogAt0_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 14),
    _CtlCANSensorsAnalogAt0_Type()
)
ctlCANSensorsAnalogAt0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogAt0.setStatus("current")


class _CtlCANSensorsAnalogAt75_Type(OctetString):
    """Custom type ctlCANSensorsAnalogAt75 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogAt75_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogAt75_Object = MibTableColumn
ctlCANSensorsAnalogAt75 = _CtlCANSensorsAnalogAt75_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 15),
    _CtlCANSensorsAnalogAt75_Type()
)
ctlCANSensorsAnalogAt75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogAt75.setStatus("current")


class _CtlCANSensorsAnalogExpression_Type(OctetString):
    """Custom type ctlCANSensorsAnalogExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 80),
    )


_CtlCANSensorsAnalogExpression_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogExpression_Object = MibTableColumn
ctlCANSensorsAnalogExpression = _CtlCANSensorsAnalogExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 16),
    _CtlCANSensorsAnalogExpression_Type()
)
ctlCANSensorsAnalogExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogExpression.setStatus("current")


class _CtlCANSensorsAnalogSpecific_Type(OctetString):
    """Custom type ctlCANSensorsAnalogSpecific based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogSpecific_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogSpecific_Object = MibTableColumn
ctlCANSensorsAnalogSpecific = _CtlCANSensorsAnalogSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 17),
    _CtlCANSensorsAnalogSpecific_Type()
)
ctlCANSensorsAnalogSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogSpecific.setStatus("current")


class _CtlCANSensorsAnalogHystType_Type(OctetString):
    """Custom type ctlCANSensorsAnalogHystType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlCANSensorsAnalogHystType_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogHystType_Object = MibTableColumn
ctlCANSensorsAnalogHystType = _CtlCANSensorsAnalogHystType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 18),
    _CtlCANSensorsAnalogHystType_Type()
)
ctlCANSensorsAnalogHystType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHystType.setStatus("current")


class _CtlCANSensorsAnalogHystValue_Type(OctetString):
    """Custom type ctlCANSensorsAnalogHystValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlCANSensorsAnalogHystValue_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogHystValue_Object = MibTableColumn
ctlCANSensorsAnalogHystValue = _CtlCANSensorsAnalogHystValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 19),
    _CtlCANSensorsAnalogHystValue_Type()
)
ctlCANSensorsAnalogHystValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHystValue.setStatus("current")
_CtlCANSensorsAnalogHystLowAlarm_Type = Integer32
_CtlCANSensorsAnalogHystLowAlarm_Object = MibTableColumn
ctlCANSensorsAnalogHystLowAlarm = _CtlCANSensorsAnalogHystLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 20),
    _CtlCANSensorsAnalogHystLowAlarm_Type()
)
ctlCANSensorsAnalogHystLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHystLowAlarm.setStatus("current")
_CtlCANSensorsAnalogHystLowWarning_Type = Integer32
_CtlCANSensorsAnalogHystLowWarning_Object = MibTableColumn
ctlCANSensorsAnalogHystLowWarning = _CtlCANSensorsAnalogHystLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 21),
    _CtlCANSensorsAnalogHystLowWarning_Type()
)
ctlCANSensorsAnalogHystLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHystLowWarning.setStatus("current")
_CtlCANSensorsAnalogHystNormal_Type = Integer32
_CtlCANSensorsAnalogHystNormal_Object = MibTableColumn
ctlCANSensorsAnalogHystNormal = _CtlCANSensorsAnalogHystNormal_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 22),
    _CtlCANSensorsAnalogHystNormal_Type()
)
ctlCANSensorsAnalogHystNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHystNormal.setStatus("current")
_CtlCANSensorsAnalogHystHighWarning_Type = Integer32
_CtlCANSensorsAnalogHystHighWarning_Object = MibTableColumn
ctlCANSensorsAnalogHystHighWarning = _CtlCANSensorsAnalogHystHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 23),
    _CtlCANSensorsAnalogHystHighWarning_Type()
)
ctlCANSensorsAnalogHystHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHystHighWarning.setStatus("current")
_CtlCANSensorsAnalogHystHighAlarm_Type = Integer32
_CtlCANSensorsAnalogHystHighAlarm_Object = MibTableColumn
ctlCANSensorsAnalogHystHighAlarm = _CtlCANSensorsAnalogHystHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 24),
    _CtlCANSensorsAnalogHystHighAlarm_Type()
)
ctlCANSensorsAnalogHystHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHystHighAlarm.setStatus("current")
_CtlCANSensorsAnalogValueInt_Type = Integer32
_CtlCANSensorsAnalogValueInt_Object = MibTableColumn
ctlCANSensorsAnalogValueInt = _CtlCANSensorsAnalogValueInt_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 25),
    _CtlCANSensorsAnalogValueInt_Type()
)
ctlCANSensorsAnalogValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogValueInt.setStatus("current")
_CtlCANSensorsOutletsTable_Object = MibTable
ctlCANSensorsOutletsTable = _CtlCANSensorsOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3)
)
if mibBuilder.loadTexts:
    ctlCANSensorsOutletsTable.setStatus("current")
_CtlCANSensorsOutletsEntry_Object = MibTableRow
ctlCANSensorsOutletsEntry = _CtlCANSensorsOutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1)
)
ctlCANSensorsOutletsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlCANSensorsOutletId"),
)
if mibBuilder.loadTexts:
    ctlCANSensorsOutletsEntry.setStatus("current")
_CtlCANSensorsOutletId_Type = Integer32
_CtlCANSensorsOutletId_Object = MibTableColumn
ctlCANSensorsOutletId = _CtlCANSensorsOutletId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 1),
    _CtlCANSensorsOutletId_Type()
)
ctlCANSensorsOutletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletId.setStatus("current")
_CtlCANSensorsOutletModule_Type = Integer32
_CtlCANSensorsOutletModule_Object = MibTableColumn
ctlCANSensorsOutletModule = _CtlCANSensorsOutletModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 2),
    _CtlCANSensorsOutletModule_Type()
)
ctlCANSensorsOutletModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletModule.setStatus("current")
_CtlCANSensorsOutletNum_Type = Integer32
_CtlCANSensorsOutletNum_Object = MibTableColumn
ctlCANSensorsOutletNum = _CtlCANSensorsOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 3),
    _CtlCANSensorsOutletNum_Type()
)
ctlCANSensorsOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletNum.setStatus("current")
_CtlCANSensorsOutletType_Type = OctetString
_CtlCANSensorsOutletType_Object = MibTableColumn
ctlCANSensorsOutletType = _CtlCANSensorsOutletType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 4),
    _CtlCANSensorsOutletType_Type()
)
ctlCANSensorsOutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletType.setStatus("current")


class _CtlCANSensorsOutletName_Type(OctetString):
    """Custom type ctlCANSensorsOutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlCANSensorsOutletName_Type.__name__ = "OctetString"
_CtlCANSensorsOutletName_Object = MibTableColumn
ctlCANSensorsOutletName = _CtlCANSensorsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 5),
    _CtlCANSensorsOutletName_Type()
)
ctlCANSensorsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletName.setStatus("current")
_CtlCANSensorsOutletState_Type = OctetString
_CtlCANSensorsOutletState_Object = MibTableColumn
ctlCANSensorsOutletState = _CtlCANSensorsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 6),
    _CtlCANSensorsOutletState_Type()
)
ctlCANSensorsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletState.setStatus("current")
_CtlCANSensorsOutletValue_Type = OctetString
_CtlCANSensorsOutletValue_Object = MibTableColumn
ctlCANSensorsOutletValue = _CtlCANSensorsOutletValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 7),
    _CtlCANSensorsOutletValue_Type()
)
ctlCANSensorsOutletValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletValue.setStatus("current")
_CtlCANSensorsOutletInitial_Type = OctetString
_CtlCANSensorsOutletInitial_Object = MibTableColumn
ctlCANSensorsOutletInitial = _CtlCANSensorsOutletInitial_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 8),
    _CtlCANSensorsOutletInitial_Type()
)
ctlCANSensorsOutletInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletInitial.setStatus("current")
_CtlCANSensorsDiscretPulse_Type = Integer32
_CtlCANSensorsDiscretPulse_Object = MibTableColumn
ctlCANSensorsDiscretPulse = _CtlCANSensorsDiscretPulse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 9),
    _CtlCANSensorsDiscretPulse_Type()
)
ctlCANSensorsDiscretPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretPulse.setStatus("current")
_CtlRsSensors_ObjectIdentity = ObjectIdentity
ctlRsSensors = _CtlRsSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 7)
)
_CtlRsSensorsDiscretsTable_Object = MibTable
ctlRsSensorsDiscretsTable = _CtlRsSensorsDiscretsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1)
)
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretsTable.setStatus("current")
_CtlRsSensorsDiscretsEntry_Object = MibTableRow
ctlRsSensorsDiscretsEntry = _CtlRsSensorsDiscretsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1)
)
ctlRsSensorsDiscretsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlRsSensorsDiscretId"),
)
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretsEntry.setStatus("current")
_CtlRsSensorsDiscretId_Type = Integer32
_CtlRsSensorsDiscretId_Object = MibTableColumn
ctlRsSensorsDiscretId = _CtlRsSensorsDiscretId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 1),
    _CtlRsSensorsDiscretId_Type()
)
ctlRsSensorsDiscretId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretId.setStatus("current")
_CtlRsSensorsDiscretModule_Type = Integer32
_CtlRsSensorsDiscretModule_Object = MibTableColumn
ctlRsSensorsDiscretModule = _CtlRsSensorsDiscretModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 2),
    _CtlRsSensorsDiscretModule_Type()
)
ctlRsSensorsDiscretModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretModule.setStatus("current")
_CtlRsSensorsDiscretNum_Type = Integer32
_CtlRsSensorsDiscretNum_Object = MibTableColumn
ctlRsSensorsDiscretNum = _CtlRsSensorsDiscretNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 3),
    _CtlRsSensorsDiscretNum_Type()
)
ctlRsSensorsDiscretNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretNum.setStatus("current")
_CtlRsSensorsDiscretType_Type = OctetString
_CtlRsSensorsDiscretType_Object = MibTableColumn
ctlRsSensorsDiscretType = _CtlRsSensorsDiscretType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 4),
    _CtlRsSensorsDiscretType_Type()
)
ctlRsSensorsDiscretType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretType.setStatus("current")


class _CtlRsSensorsDiscretName_Type(OctetString):
    """Custom type ctlRsSensorsDiscretName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlRsSensorsDiscretName_Type.__name__ = "OctetString"
_CtlRsSensorsDiscretName_Object = MibTableColumn
ctlRsSensorsDiscretName = _CtlRsSensorsDiscretName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 5),
    _CtlRsSensorsDiscretName_Type()
)
ctlRsSensorsDiscretName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretName.setStatus("current")
_CtlRsSensorsDiscretState_Type = OctetString
_CtlRsSensorsDiscretState_Object = MibTableColumn
ctlRsSensorsDiscretState = _CtlRsSensorsDiscretState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 6),
    _CtlRsSensorsDiscretState_Type()
)
ctlRsSensorsDiscretState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretState.setStatus("current")
_CtlRsSensorsDiscretValue_Type = OctetString
_CtlRsSensorsDiscretValue_Object = MibTableColumn
ctlRsSensorsDiscretValue = _CtlRsSensorsDiscretValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 7),
    _CtlRsSensorsDiscretValue_Type()
)
ctlRsSensorsDiscretValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretValue.setStatus("current")
_CtlRsSensorsDiscretReset_Type = Integer32
_CtlRsSensorsDiscretReset_Object = MibTableColumn
ctlRsSensorsDiscretReset = _CtlRsSensorsDiscretReset_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 8),
    _CtlRsSensorsDiscretReset_Type()
)
ctlRsSensorsDiscretReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretReset.setStatus("current")
_CtlRsSensorsDiscretLevel_Type = Integer32
_CtlRsSensorsDiscretLevel_Object = MibTableColumn
ctlRsSensorsDiscretLevel = _CtlRsSensorsDiscretLevel_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 9),
    _CtlRsSensorsDiscretLevel_Type()
)
ctlRsSensorsDiscretLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretLevel.setStatus("current")
_CtlRsSensorsDiscretReverse_Type = Integer32
_CtlRsSensorsDiscretReverse_Object = MibTableColumn
ctlRsSensorsDiscretReverse = _CtlRsSensorsDiscretReverse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 10),
    _CtlRsSensorsDiscretReverse_Type()
)
ctlRsSensorsDiscretReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretReverse.setStatus("current")
_CtlRsSensorsDiscretSpecific_Type = OctetString
_CtlRsSensorsDiscretSpecific_Object = MibTableColumn
ctlRsSensorsDiscretSpecific = _CtlRsSensorsDiscretSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 11),
    _CtlRsSensorsDiscretSpecific_Type()
)
ctlRsSensorsDiscretSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretSpecific.setStatus("current")
_CtlRsSensorsAnalogsTable_Object = MibTable
ctlRsSensorsAnalogsTable = _CtlRsSensorsAnalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2)
)
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogsTable.setStatus("current")
_CtlRsSensorsAnalogsEntry_Object = MibTableRow
ctlRsSensorsAnalogsEntry = _CtlRsSensorsAnalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1)
)
ctlRsSensorsAnalogsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlRsSensorsAnalogId"),
)
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogsEntry.setStatus("current")
_CtlRsSensorsAnalogId_Type = Integer32
_CtlRsSensorsAnalogId_Object = MibTableColumn
ctlRsSensorsAnalogId = _CtlRsSensorsAnalogId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 1),
    _CtlRsSensorsAnalogId_Type()
)
ctlRsSensorsAnalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogId.setStatus("current")
_CtlRsSensorsAnalogModule_Type = Integer32
_CtlRsSensorsAnalogModule_Object = MibTableColumn
ctlRsSensorsAnalogModule = _CtlRsSensorsAnalogModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 2),
    _CtlRsSensorsAnalogModule_Type()
)
ctlRsSensorsAnalogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogModule.setStatus("current")
_CtlRsSensorsAnalogNum_Type = Integer32
_CtlRsSensorsAnalogNum_Object = MibTableColumn
ctlRsSensorsAnalogNum = _CtlRsSensorsAnalogNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 3),
    _CtlRsSensorsAnalogNum_Type()
)
ctlRsSensorsAnalogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogNum.setStatus("current")
_CtlRsSensorsAnalogType_Type = OctetString
_CtlRsSensorsAnalogType_Object = MibTableColumn
ctlRsSensorsAnalogType = _CtlRsSensorsAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 4),
    _CtlRsSensorsAnalogType_Type()
)
ctlRsSensorsAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogType.setStatus("current")


class _CtlRsSensorsAnalogName_Type(OctetString):
    """Custom type ctlRsSensorsAnalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlRsSensorsAnalogName_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogName_Object = MibTableColumn
ctlRsSensorsAnalogName = _CtlRsSensorsAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 5),
    _CtlRsSensorsAnalogName_Type()
)
ctlRsSensorsAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogName.setStatus("current")
_CtlRsSensorsAnalogState_Type = OctetString
_CtlRsSensorsAnalogState_Object = MibTableColumn
ctlRsSensorsAnalogState = _CtlRsSensorsAnalogState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 6),
    _CtlRsSensorsAnalogState_Type()
)
ctlRsSensorsAnalogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogState.setStatus("current")
_CtlRsSensorsAnalogValue_Type = OctetString
_CtlRsSensorsAnalogValue_Object = MibTableColumn
ctlRsSensorsAnalogValue = _CtlRsSensorsAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 7),
    _CtlRsSensorsAnalogValue_Type()
)
ctlRsSensorsAnalogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogValue.setStatus("current")
_CtlRsSensorsAnalogMin_Type = OctetString
_CtlRsSensorsAnalogMin_Object = MibTableColumn
ctlRsSensorsAnalogMin = _CtlRsSensorsAnalogMin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 8),
    _CtlRsSensorsAnalogMin_Type()
)
ctlRsSensorsAnalogMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogMin.setStatus("current")
_CtlRsSensorsAnalogMax_Type = OctetString
_CtlRsSensorsAnalogMax_Object = MibTableColumn
ctlRsSensorsAnalogMax = _CtlRsSensorsAnalogMax_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 9),
    _CtlRsSensorsAnalogMax_Type()
)
ctlRsSensorsAnalogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogMax.setStatus("current")


class _CtlRsSensorsAnalogLowAlarm_Type(OctetString):
    """Custom type ctlRsSensorsAnalogLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogLowAlarm_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogLowAlarm_Object = MibTableColumn
ctlRsSensorsAnalogLowAlarm = _CtlRsSensorsAnalogLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 10),
    _CtlRsSensorsAnalogLowAlarm_Type()
)
ctlRsSensorsAnalogLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogLowAlarm.setStatus("current")


class _CtlRsSensorsAnalogLowWarning_Type(OctetString):
    """Custom type ctlRsSensorsAnalogLowWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogLowWarning_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogLowWarning_Object = MibTableColumn
ctlRsSensorsAnalogLowWarning = _CtlRsSensorsAnalogLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 11),
    _CtlRsSensorsAnalogLowWarning_Type()
)
ctlRsSensorsAnalogLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogLowWarning.setStatus("current")


class _CtlRsSensorsAnalogHighWarning_Type(OctetString):
    """Custom type ctlRsSensorsAnalogHighWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogHighWarning_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogHighWarning_Object = MibTableColumn
ctlRsSensorsAnalogHighWarning = _CtlRsSensorsAnalogHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 12),
    _CtlRsSensorsAnalogHighWarning_Type()
)
ctlRsSensorsAnalogHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogHighWarning.setStatus("current")


class _CtlRsSensorsAnalogHighAlarm_Type(OctetString):
    """Custom type ctlRsSensorsAnalogHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogHighAlarm_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogHighAlarm_Object = MibTableColumn
ctlRsSensorsAnalogHighAlarm = _CtlRsSensorsAnalogHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 13),
    _CtlRsSensorsAnalogHighAlarm_Type()
)
ctlRsSensorsAnalogHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogHighAlarm.setStatus("current")


class _CtlRsSensorsAnalogAt0_Type(OctetString):
    """Custom type ctlRsSensorsAnalogAt0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogAt0_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogAt0_Object = MibTableColumn
ctlRsSensorsAnalogAt0 = _CtlRsSensorsAnalogAt0_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 14),
    _CtlRsSensorsAnalogAt0_Type()
)
ctlRsSensorsAnalogAt0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogAt0.setStatus("current")


class _CtlRsSensorsAnalogAt75_Type(OctetString):
    """Custom type ctlRsSensorsAnalogAt75 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogAt75_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogAt75_Object = MibTableColumn
ctlRsSensorsAnalogAt75 = _CtlRsSensorsAnalogAt75_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 15),
    _CtlRsSensorsAnalogAt75_Type()
)
ctlRsSensorsAnalogAt75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogAt75.setStatus("current")


class _CtlRsSensorsAnalogExpression_Type(OctetString):
    """Custom type ctlRsSensorsAnalogExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 80),
    )


_CtlRsSensorsAnalogExpression_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogExpression_Object = MibTableColumn
ctlRsSensorsAnalogExpression = _CtlRsSensorsAnalogExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 16),
    _CtlRsSensorsAnalogExpression_Type()
)
ctlRsSensorsAnalogExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogExpression.setStatus("current")


class _CtlRsSensorsAnalogSpecific_Type(OctetString):
    """Custom type ctlRsSensorsAnalogSpecific based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogSpecific_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogSpecific_Object = MibTableColumn
ctlRsSensorsAnalogSpecific = _CtlRsSensorsAnalogSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 17),
    _CtlRsSensorsAnalogSpecific_Type()
)
ctlRsSensorsAnalogSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogSpecific.setStatus("current")
_CtlRsSensorsOutletsTable_Object = MibTable
ctlRsSensorsOutletsTable = _CtlRsSensorsOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3)
)
if mibBuilder.loadTexts:
    ctlRsSensorsOutletsTable.setStatus("current")
_CtlRsSensorsOutletsEntry_Object = MibTableRow
ctlRsSensorsOutletsEntry = _CtlRsSensorsOutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1)
)
ctlRsSensorsOutletsEntry.setIndexNames(
    (0, "VUTLAN-SYSTEM-MIB", "ctlRsSensorsOutletId"),
)
if mibBuilder.loadTexts:
    ctlRsSensorsOutletsEntry.setStatus("current")
_CtlRsSensorsOutletId_Type = Integer32
_CtlRsSensorsOutletId_Object = MibTableColumn
ctlRsSensorsOutletId = _CtlRsSensorsOutletId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 1),
    _CtlRsSensorsOutletId_Type()
)
ctlRsSensorsOutletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletId.setStatus("current")
_CtlRsSensorsOutletModule_Type = Integer32
_CtlRsSensorsOutletModule_Object = MibTableColumn
ctlRsSensorsOutletModule = _CtlRsSensorsOutletModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 2),
    _CtlRsSensorsOutletModule_Type()
)
ctlRsSensorsOutletModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletModule.setStatus("current")
_CtlRsSensorsOutletNum_Type = Integer32
_CtlRsSensorsOutletNum_Object = MibTableColumn
ctlRsSensorsOutletNum = _CtlRsSensorsOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 3),
    _CtlRsSensorsOutletNum_Type()
)
ctlRsSensorsOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletNum.setStatus("current")
_CtlRsSensorsOutletType_Type = OctetString
_CtlRsSensorsOutletType_Object = MibTableColumn
ctlRsSensorsOutletType = _CtlRsSensorsOutletType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 4),
    _CtlRsSensorsOutletType_Type()
)
ctlRsSensorsOutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletType.setStatus("current")


class _CtlRsSensorsOutletName_Type(OctetString):
    """Custom type ctlRsSensorsOutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlRsSensorsOutletName_Type.__name__ = "OctetString"
_CtlRsSensorsOutletName_Object = MibTableColumn
ctlRsSensorsOutletName = _CtlRsSensorsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 5),
    _CtlRsSensorsOutletName_Type()
)
ctlRsSensorsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletName.setStatus("current")
_CtlRsSensorsOutletState_Type = OctetString
_CtlRsSensorsOutletState_Object = MibTableColumn
ctlRsSensorsOutletState = _CtlRsSensorsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 6),
    _CtlRsSensorsOutletState_Type()
)
ctlRsSensorsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletState.setStatus("current")
_CtlRsSensorsOutletValue_Type = OctetString
_CtlRsSensorsOutletValue_Object = MibTableColumn
ctlRsSensorsOutletValue = _CtlRsSensorsOutletValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 7),
    _CtlRsSensorsOutletValue_Type()
)
ctlRsSensorsOutletValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletValue.setStatus("current")
_CtlRsSensorsOutletInitial_Type = OctetString
_CtlRsSensorsOutletInitial_Object = MibTableColumn
ctlRsSensorsOutletInitial = _CtlRsSensorsOutletInitial_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 8),
    _CtlRsSensorsOutletInitial_Type()
)
ctlRsSensorsOutletInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletInitial.setStatus("current")
_CtlRsSensorsDiscretPulse_Type = Integer32
_CtlRsSensorsDiscretPulse_Object = MibTableColumn
ctlRsSensorsDiscretPulse = _CtlRsSensorsDiscretPulse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 9),
    _CtlRsSensorsDiscretPulse_Type()
)
ctlRsSensorsDiscretPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretPulse.setStatus("current")

# Managed Objects groups


# Notification objects

ctlUnitTrapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5)
)
ctlUnitTrapNotification.setObjects(
      *(("VUTLAN-SYSTEM-MIB", "macroLogicDefinition"),
        ("VUTLAN-SYSTEM-MIB", "macroStateOfSensors"),
        ("VUTLAN-SYSTEM-MIB", "macroDateAndTime"),
        ("VUTLAN-SYSTEM-MIB", "macroLogicName"),
        ("VUTLAN-SYSTEM-MIB", "macroSensorName"),
        ("VUTLAN-SYSTEM-MIB", "macroSensorState"),
        ("VUTLAN-SYSTEM-MIB", "macroSensorValue"),
        ("VUTLAN-SYSTEM-MIB", "macroLastModifiedSensorID"),
        ("VUTLAN-SYSTEM-MIB", "trapID"),
        ("VUTLAN-SYSTEM-MIB", "trapName"))
)
if mibBuilder.loadTexts:
    ctlUnitTrapNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VUTLAN-SYSTEM-MIB",
    **{"vutlan": vutlan,
       "ctlUnit": ctlUnit,
       "ctlUnitModulesTable": ctlUnitModulesTable,
       "ctlUnitModulesEntry": ctlUnitModulesEntry,
       "ctlUnitModuleId": ctlUnitModuleId,
       "ctlUnitModulePcode": ctlUnitModulePcode,
       "ctlUnitModuleSN": ctlUnitModuleSN,
       "ctlUnitModuleClass": ctlUnitModuleClass,
       "ctlUnitModuleType": ctlUnitModuleType,
       "ctlUnitModuleName": ctlUnitModuleName,
       "ctlUnitModuleState": ctlUnitModuleState,
       "ctlUnitGroupsTable": ctlUnitGroupsTable,
       "ctlUnitGroupsEntry": ctlUnitGroupsEntry,
       "ctlUnitGroupId": ctlUnitGroupId,
       "ctlUnitGroupName": ctlUnitGroupName,
       "ctlUnitGroupDesc": ctlUnitGroupDesc,
       "ctlUnitElementsTable": ctlUnitElementsTable,
       "ctlUnitElementsEntry": ctlUnitElementsEntry,
       "ctlUnitElementId": ctlUnitElementId,
       "ctlUnitElementGroup": ctlUnitElementGroup,
       "ctlUnitElementModule": ctlUnitElementModule,
       "ctlUnitElementNum": ctlUnitElementNum,
       "ctlUnitElementClass": ctlUnitElementClass,
       "ctlUnitElementType": ctlUnitElementType,
       "ctlUnitElementName": ctlUnitElementName,
       "ctlUnitElementState": ctlUnitElementState,
       "ctlUnitElementValue": ctlUnitElementValue,
       "ctlUnitElementSpec": ctlUnitElementSpec,
       "ctlUnitLogicsTable": ctlUnitLogicsTable,
       "ctlUnitLogicsEntry": ctlUnitLogicsEntry,
       "ctlUnitLogicId": ctlUnitLogicId,
       "ctlUnitLogicName": ctlUnitLogicName,
       "ctlUnitLogicDesc": ctlUnitLogicDesc,
       "ctlUnitLogicDisable": ctlUnitLogicDisable,
       "ctlUnitLogicRowStatus": ctlUnitLogicRowStatus,
       "ctlUnitTrapNotification": ctlUnitTrapNotification,
       "macroLogicDefinition": macroLogicDefinition,
       "macroStateOfSensors": macroStateOfSensors,
       "macroDateAndTime": macroDateAndTime,
       "macroLogicName": macroLogicName,
       "macroSensorName": macroSensorName,
       "macroSensorState": macroSensorState,
       "macroSensorValue": macroSensorValue,
       "macroLastModifiedSensorID": macroLastModifiedSensorID,
       "trapID": trapID,
       "trapName": trapName,
       "ctlUnitSaveToFlash": ctlUnitSaveToFlash,
       "ctlUnitSystem": ctlUnitSystem,
       "systemDevType": systemDevType,
       "systemFirmware": systemFirmware,
       "systemKernel": systemKernel,
       "systemOpTime": systemOpTime,
       "systemUpTime": systemUpTime,
       "systemCpuUsage": systemCpuUsage,
       "systemMemUsage": systemMemUsage,
       "systemState": systemState,
       "systemHostname": systemHostname,
       "systemDescSN": systemDescSN,
       "systemDescContacts": systemDescContacts,
       "systemDescLocation": systemDescLocation,
       "systemDescComment": systemDescComment,
       "systemMAC": systemMAC,
       "ctlUnitReboot": ctlUnitReboot,
       "ctlNotifiers": ctlNotifiers,
       "ctlNotifiersMailersTable": ctlNotifiersMailersTable,
       "ctlNotifiersMailersEntry": ctlNotifiersMailersEntry,
       "ctlNotifiersMailerId": ctlNotifiersMailerId,
       "ctlNotifiersMailerModule": ctlNotifiersMailerModule,
       "ctlNotifiersMailerNum": ctlNotifiersMailerNum,
       "ctlNotifiersMailerType": ctlNotifiersMailerType,
       "ctlNotifiersMailerName": ctlNotifiersMailerName,
       "ctlNotifiersMailerState": ctlNotifiersMailerState,
       "ctlNotifiersMailerValue": ctlNotifiersMailerValue,
       "ctlNotifiersMailerServer": ctlNotifiersMailerServer,
       "ctlNotifiersMailerPort": ctlNotifiersMailerPort,
       "ctlNotifiersMailerLogin": ctlNotifiersMailerLogin,
       "ctlNotifiersMailerPassword": ctlNotifiersMailerPassword,
       "ctlNotifiersMailersTo": ctlNotifiersMailersTo,
       "ctlNotifiersMailersFrom": ctlNotifiersMailersFrom,
       "ctlNotifiersMailerMessage": ctlNotifiersMailerMessage,
       "ctlNotifiersTrapsTable": ctlNotifiersTrapsTable,
       "ctlNotifiersTrapsEntry": ctlNotifiersTrapsEntry,
       "ctlNotifiersTrapId": ctlNotifiersTrapId,
       "ctlNotifiersTrapModule": ctlNotifiersTrapModule,
       "ctlNotifiersTrapNum": ctlNotifiersTrapNum,
       "ctlNotifiersTrapType": ctlNotifiersTrapType,
       "ctlNotifiersTrapName": ctlNotifiersTrapName,
       "ctlNotifiersTrapState": ctlNotifiersTrapState,
       "ctlNotifiersTrapValue": ctlNotifiersTrapValue,
       "ctlNotifiersTrapServer": ctlNotifiersTrapServer,
       "ctlNotifiersTrapPort": ctlNotifiersTrapPort,
       "ctlNotifiersTrapVersion": ctlNotifiersTrapVersion,
       "ctlNotifiersTrapCommunity": ctlNotifiersTrapCommunity,
       "ctlNotifiersSMSsTable": ctlNotifiersSMSsTable,
       "ctlNotifiersSMSsEntry": ctlNotifiersSMSsEntry,
       "ctlNotifiersSMSId": ctlNotifiersSMSId,
       "ctlNotifiersSMSModule": ctlNotifiersSMSModule,
       "ctlNotifiersSMSNum": ctlNotifiersSMSNum,
       "ctlNotifiersSMSType": ctlNotifiersSMSType,
       "ctlNotifiersSMSName": ctlNotifiersSMSName,
       "ctlNotifiersSMSState": ctlNotifiersSMSState,
       "ctlNotifiersSMSValue": ctlNotifiersSMSValue,
       "ctlNotifiersSMSTo": ctlNotifiersSMSTo,
       "ctlNotifiersSMSMessage": ctlNotifiersSMSMessage,
       "ctlVirtualDevices": ctlVirtualDevices,
       "ctlVirtualDevicesTimersTable": ctlVirtualDevicesTimersTable,
       "ctlVirtualDevicesTimersEntry": ctlVirtualDevicesTimersEntry,
       "ctlVirtualDevicesTimerId": ctlVirtualDevicesTimerId,
       "ctlVirtualDevicesTimerModule": ctlVirtualDevicesTimerModule,
       "ctlVirtualDevicesTimerNum": ctlVirtualDevicesTimerNum,
       "ctlVirtualDevicesTimerType": ctlVirtualDevicesTimerType,
       "ctlVirtualDevicesTimerName": ctlVirtualDevicesTimerName,
       "ctlVirtualDevicesTimerState": ctlVirtualDevicesTimerState,
       "ctlVirtualDevicesTimerValue": ctlVirtualDevicesTimerValue,
       "ctlVirtualDevicesTimerBegin": ctlVirtualDevicesTimerBegin,
       "ctlVirtualDevicesTimerEnd": ctlVirtualDevicesTimerEnd,
       "ctlVirtualDevicesTimerDays": ctlVirtualDevicesTimerDays,
       "ctlVirtualDevicesTimerMode": ctlVirtualDevicesTimerMode,
       "ctlVirtualDevicesTimerDayPattern": ctlVirtualDevicesTimerDayPattern,
       "ctlVirtualDevicesPingsTable": ctlVirtualDevicesPingsTable,
       "ctlVirtualDevicesPingsEntry": ctlVirtualDevicesPingsEntry,
       "ctlVirtualDevicesPingId": ctlVirtualDevicesPingId,
       "ctlVirtualDevicesPingModule": ctlVirtualDevicesPingModule,
       "ctlVirtualDevicesPingNum": ctlVirtualDevicesPingNum,
       "ctlVirtualDevicesPingType": ctlVirtualDevicesPingType,
       "ctlVirtualDevicesPingName": ctlVirtualDevicesPingName,
       "ctlVirtualDevicesPingState": ctlVirtualDevicesPingState,
       "ctlVirtualDevicesPingValue": ctlVirtualDevicesPingValue,
       "ctlVirtualDevicesPingPeriod": ctlVirtualDevicesPingPeriod,
       "ctlVirtualDevicesPingRTT": ctlVirtualDevicesPingRTT,
       "ctlVirtualDevicesPingServer": ctlVirtualDevicesPingServer,
       "ctlVirtualDevicesPingIP": ctlVirtualDevicesPingIP,
       "ctlVirtualDevicesPingSent": ctlVirtualDevicesPingSent,
       "ctlVirtualDevicesPingReceived": ctlVirtualDevicesPingReceived,
       "ctlVirtualDevicesPingStatus": ctlVirtualDevicesPingStatus,
       "ctlVirtualDevicesTriggersTable": ctlVirtualDevicesTriggersTable,
       "ctlVirtualDevicesTriggersEntry": ctlVirtualDevicesTriggersEntry,
       "ctlVirtualDevicesTriggerId": ctlVirtualDevicesTriggerId,
       "ctlVirtualDevicesTriggerModule": ctlVirtualDevicesTriggerModule,
       "ctlVirtualDevicesTriggerNum": ctlVirtualDevicesTriggerNum,
       "ctlVirtualDevicesTriggerType": ctlVirtualDevicesTriggerType,
       "ctlVirtualDevicesTriggerName": ctlVirtualDevicesTriggerName,
       "ctlVirtualDevicesTriggerState": ctlVirtualDevicesTriggerState,
       "ctlVirtualDevicesTriggerValue": ctlVirtualDevicesTriggerValue,
       "ctlVirtualDevicesTriggerReverse": ctlVirtualDevicesTriggerReverse,
       "ctlVirtualDevicesSnmpgetsTable": ctlVirtualDevicesSnmpgetsTable,
       "ctlVirtualDevicesSnmpgetsEntry": ctlVirtualDevicesSnmpgetsEntry,
       "ctlVirtualDevicesSnmpgetId": ctlVirtualDevicesSnmpgetId,
       "ctlVirtualDevicesSnmpgetModule": ctlVirtualDevicesSnmpgetModule,
       "ctlVirtualDevicesSnmpgetNum": ctlVirtualDevicesSnmpgetNum,
       "ctlVirtualDevicesSnmpgetType": ctlVirtualDevicesSnmpgetType,
       "ctlVirtualDevicesSnmpgetName": ctlVirtualDevicesSnmpgetName,
       "ctlVirtualDevicesSnmpgetState": ctlVirtualDevicesSnmpgetState,
       "ctlVirtualDevicesSnmpgetValue": ctlVirtualDevicesSnmpgetValue,
       "ctlVirtualDevicesSnmpgetStatus": ctlVirtualDevicesSnmpgetStatus,
       "ctlVirtualDevicesSnmpgetPeriod": ctlVirtualDevicesSnmpgetPeriod,
       "ctlVirtualDevicesSnmpgetServer": ctlVirtualDevicesSnmpgetServer,
       "ctlVirtualDevicesSnmpgetPort": ctlVirtualDevicesSnmpgetPort,
       "ctlVirtualDevicesSnmpgetCommunity": ctlVirtualDevicesSnmpgetCommunity,
       "ctlVirtualDevicesSnmpgetOid": ctlVirtualDevicesSnmpgetOid,
       "ctlVirtualDevicesSnmpgetVartype": ctlVirtualDevicesSnmpgetVartype,
       "ctlVirtualDevicesSnmpgetLowAlarm": ctlVirtualDevicesSnmpgetLowAlarm,
       "ctlVirtualDevicesSnmpgetLowWarning": ctlVirtualDevicesSnmpgetLowWarning,
       "ctlVirtualDevicesSnmpgetHighWarning": ctlVirtualDevicesSnmpgetHighWarning,
       "ctlVirtualDevicesSnmpgetHighAlarm": ctlVirtualDevicesSnmpgetHighAlarm,
       "ctlVirtualDevicesSnmpgetExpression": ctlVirtualDevicesSnmpgetExpression,
       "ctlVirtualDevicesAnalogsTable": ctlVirtualDevicesAnalogsTable,
       "ctlVirtualDevicesAnalogsEntry": ctlVirtualDevicesAnalogsEntry,
       "ctlVirtualDevicesAnalogId": ctlVirtualDevicesAnalogId,
       "ctlVirtualDevicesAnalogModule": ctlVirtualDevicesAnalogModule,
       "ctlVirtualDevicesAnalogNum": ctlVirtualDevicesAnalogNum,
       "ctlVirtualDevicesAnalogType": ctlVirtualDevicesAnalogType,
       "ctlVirtualDevicesAnalogName": ctlVirtualDevicesAnalogName,
       "ctlVirtualDevicesAnalogState": ctlVirtualDevicesAnalogState,
       "ctlVirtualDevicesAnalogValue": ctlVirtualDevicesAnalogValue,
       "ctlVirtualDevicesAnalogMin": ctlVirtualDevicesAnalogMin,
       "ctlVirtualDevicesAnalogMax": ctlVirtualDevicesAnalogMax,
       "ctlVirtualDevicesAnalogLowAlarm": ctlVirtualDevicesAnalogLowAlarm,
       "ctlVirtualDevicesAnalogLowWarning": ctlVirtualDevicesAnalogLowWarning,
       "ctlVirtualDevicesAnalogHighWarning": ctlVirtualDevicesAnalogHighWarning,
       "ctlVirtualDevicesAnalogHighAlarm": ctlVirtualDevicesAnalogHighAlarm,
       "ctlVirtualDevicesAnalogAt0": ctlVirtualDevicesAnalogAt0,
       "ctlVirtualDevicesAnalogAt75": ctlVirtualDevicesAnalogAt75,
       "ctlVirtualDevicesAnalogExpression": ctlVirtualDevicesAnalogExpression,
       "ctlVirtualDevicesAnalogSpecific": ctlVirtualDevicesAnalogSpecific,
       "ctlVirtualDevicesAnalogHystType": ctlVirtualDevicesAnalogHystType,
       "ctlVirtualDevicesAnalogHystValue": ctlVirtualDevicesAnalogHystValue,
       "ctlVirtualDevicesAnalogHystLowAlarm": ctlVirtualDevicesAnalogHystLowAlarm,
       "ctlVirtualDevicesAnalogHystLowWarning": ctlVirtualDevicesAnalogHystLowWarning,
       "ctlVirtualDevicesAnalogHystNormal": ctlVirtualDevicesAnalogHystNormal,
       "ctlVirtualDevicesAnalogHystHighWarning": ctlVirtualDevicesAnalogHystHighWarning,
       "ctlVirtualDevicesAnalogHystHighAlarm": ctlVirtualDevicesAnalogHystHighAlarm,
       "ctlVirtualDevicesAnalogValueInt": ctlVirtualDevicesAnalogValueInt,
       "ctlHardwareDevices": ctlHardwareDevices,
       "ctlHardwareDevicesCamerasTable": ctlHardwareDevicesCamerasTable,
       "ctlHardwareDevicesCamerasEntry": ctlHardwareDevicesCamerasEntry,
       "ctlHardwareDevicesCameraId": ctlHardwareDevicesCameraId,
       "ctlHardwareDevicesCameraModule": ctlHardwareDevicesCameraModule,
       "ctlHardwareDevicesCameraNum": ctlHardwareDevicesCameraNum,
       "ctlHardwareDevicesCameraType": ctlHardwareDevicesCameraType,
       "ctlHardwareDevicesCameraName": ctlHardwareDevicesCameraName,
       "ctlHardwareDevicesCameraState": ctlHardwareDevicesCameraState,
       "ctlHardwareDevicesCameraValue": ctlHardwareDevicesCameraValue,
       "ctlHardwareDevicesCameraURL": ctlHardwareDevicesCameraURL,
       "ctlHardwareDevicesCameraFPS": ctlHardwareDevicesCameraFPS,
       "ctlHardwareDevicesCameraResolution": ctlHardwareDevicesCameraResolution,
       "ctlHardwareDevicesModemsTable": ctlHardwareDevicesModemsTable,
       "ctlHardwareDevicesModemsEntry": ctlHardwareDevicesModemsEntry,
       "ctlHardwareDevicesModemState": ctlHardwareDevicesModemState,
       "ctlHardwareDevicesModemStatus": ctlHardwareDevicesModemStatus,
       "ctlHardwareDevicesModemSignal": ctlHardwareDevicesModemSignal,
       "ctlHardwareDevicesModemOperator": ctlHardwareDevicesModemOperator,
       "ctlHardwareDevicesModemPosition": ctlHardwareDevicesModemPosition,
       "ctIInternalSensors": ctIInternalSensors,
       "ctlInternalSensorsDiscretsTable": ctlInternalSensorsDiscretsTable,
       "ctlInternalSensorsDiscretsEntry": ctlInternalSensorsDiscretsEntry,
       "ctlInternalSensorsDiscretId": ctlInternalSensorsDiscretId,
       "ctlInternalSensorsDiscretModule": ctlInternalSensorsDiscretModule,
       "ctlInternalSensorsDiscretNum": ctlInternalSensorsDiscretNum,
       "ctlInternalSensorsDiscretType": ctlInternalSensorsDiscretType,
       "ctlInternalSensorsDiscretName": ctlInternalSensorsDiscretName,
       "ctlInternalSensorsDiscretState": ctlInternalSensorsDiscretState,
       "ctlInternalSensorsDiscretValue": ctlInternalSensorsDiscretValue,
       "ctlInternalSensorsDiscretReset": ctlInternalSensorsDiscretReset,
       "ctlInternalSensorsDiscretLevel": ctlInternalSensorsDiscretLevel,
       "ctlInternalSensorsDiscretReverse": ctlInternalSensorsDiscretReverse,
       "ctlInternalSensorsDiscretSpecific": ctlInternalSensorsDiscretSpecific,
       "ctlInternalSensorsAnalogsTable": ctlInternalSensorsAnalogsTable,
       "ctlInternalSensorsAnalogsEntry": ctlInternalSensorsAnalogsEntry,
       "ctlInternalSensorsAnalogId": ctlInternalSensorsAnalogId,
       "ctlInternalSensorsAnalogModule": ctlInternalSensorsAnalogModule,
       "ctlInternalSensorsAnalogNum": ctlInternalSensorsAnalogNum,
       "ctlInternalSensorsAnalogType": ctlInternalSensorsAnalogType,
       "ctlInternalSensorsAnalogName": ctlInternalSensorsAnalogName,
       "ctlInternalSensorsAnalogState": ctlInternalSensorsAnalogState,
       "ctlInternalSensorsAnalogValue": ctlInternalSensorsAnalogValue,
       "ctlInternalSensorsAnalogMin": ctlInternalSensorsAnalogMin,
       "ctlInternalSensorsAnalogMax": ctlInternalSensorsAnalogMax,
       "ctlInternalSensorsAnalogLowAlarm": ctlInternalSensorsAnalogLowAlarm,
       "ctlInternalSensorsAnalogLowWarning": ctlInternalSensorsAnalogLowWarning,
       "ctlInternalSensorsAnalogHighWarning": ctlInternalSensorsAnalogHighWarning,
       "ctlInternalSensorsAnalogHighAlarm": ctlInternalSensorsAnalogHighAlarm,
       "ctlInternalSensorsAnalogAt0": ctlInternalSensorsAnalogAt0,
       "ctlInternalSensorsAnalogAt75": ctlInternalSensorsAnalogAt75,
       "ctlInternalSensorsAnalogExpression": ctlInternalSensorsAnalogExpression,
       "ctlInternalSensorsAnalogSpecific": ctlInternalSensorsAnalogSpecific,
       "ctlInternalSensorsAnalogHystType": ctlInternalSensorsAnalogHystType,
       "ctlInternalSensorsAnalogHystValue": ctlInternalSensorsAnalogHystValue,
       "ctlInternalSensorsAnalogHystLowAlarm": ctlInternalSensorsAnalogHystLowAlarm,
       "ctlInternalSensorsAnalogHystLowWarning": ctlInternalSensorsAnalogHystLowWarning,
       "ctlInternalSensorsAnalogHystNormal": ctlInternalSensorsAnalogHystNormal,
       "ctlInternalSensorsAnalogHystHighWarning": ctlInternalSensorsAnalogHystHighWarning,
       "ctlInternalSensorsAnalogHystHighAlarm": ctlInternalSensorsAnalogHystHighAlarm,
       "ctlInternalSensorsAnalogValueInt": ctlInternalSensorsAnalogValueInt,
       "ctlInternalSensorsOutletsTable": ctlInternalSensorsOutletsTable,
       "ctlInternalSensorsOutletsEntry": ctlInternalSensorsOutletsEntry,
       "ctlInternalSensorsOutletId": ctlInternalSensorsOutletId,
       "ctlInternalSensorsOutletModule": ctlInternalSensorsOutletModule,
       "ctlInternalSensorsOutletNum": ctlInternalSensorsOutletNum,
       "ctlInternalSensorsOutletType": ctlInternalSensorsOutletType,
       "ctlInternalSensorsOutletName": ctlInternalSensorsOutletName,
       "ctlInternalSensorsOutletState": ctlInternalSensorsOutletState,
       "ctlInternalSensorsOutletValue": ctlInternalSensorsOutletValue,
       "ctlInternalSensorsOutletInitial": ctlInternalSensorsOutletInitial,
       "ctlInternalSensorsDiscretPulse": ctlInternalSensorsDiscretPulse,
       "ctlCANSensors": ctlCANSensors,
       "ctlCANSensorsDiscretsTable": ctlCANSensorsDiscretsTable,
       "ctlCANSensorsDiscretsEntry": ctlCANSensorsDiscretsEntry,
       "ctlCANSensorsDiscretId": ctlCANSensorsDiscretId,
       "ctlCANSensorsDiscretModule": ctlCANSensorsDiscretModule,
       "ctlCANSensorsDiscretNum": ctlCANSensorsDiscretNum,
       "ctlCANSensorsDiscretType": ctlCANSensorsDiscretType,
       "ctlCANSensorsDiscretName": ctlCANSensorsDiscretName,
       "ctlCANSensorsDiscretState": ctlCANSensorsDiscretState,
       "ctlCANSensorsDiscretValue": ctlCANSensorsDiscretValue,
       "ctlCANSensorsDiscretReset": ctlCANSensorsDiscretReset,
       "ctlCANSensorsDiscretLevel": ctlCANSensorsDiscretLevel,
       "ctlCANSensorsDiscretReverse": ctlCANSensorsDiscretReverse,
       "ctlCANSensorsDiscretSpecific": ctlCANSensorsDiscretSpecific,
       "ctlCANSensorsAnalogsTable": ctlCANSensorsAnalogsTable,
       "ctlCANSensorsAnalogsEntry": ctlCANSensorsAnalogsEntry,
       "ctlCANSensorsAnalogId": ctlCANSensorsAnalogId,
       "ctlCANSensorsAnalogModule": ctlCANSensorsAnalogModule,
       "ctlCANSensorsAnalogNum": ctlCANSensorsAnalogNum,
       "ctlCANSensorsAnalogType": ctlCANSensorsAnalogType,
       "ctlCANSensorsAnalogName": ctlCANSensorsAnalogName,
       "ctlCANSensorsAnalogState": ctlCANSensorsAnalogState,
       "ctlCANSensorsAnalogValue": ctlCANSensorsAnalogValue,
       "ctlCANSensorsAnalogMin": ctlCANSensorsAnalogMin,
       "ctlCANSensorsAnalogMax": ctlCANSensorsAnalogMax,
       "ctlCANSensorsAnalogLowAlarm": ctlCANSensorsAnalogLowAlarm,
       "ctlCANSensorsAnalogLowWarning": ctlCANSensorsAnalogLowWarning,
       "ctlCANSensorsAnalogHighWarning": ctlCANSensorsAnalogHighWarning,
       "ctlCANSensorsAnalogHighAlarm": ctlCANSensorsAnalogHighAlarm,
       "ctlCANSensorsAnalogAt0": ctlCANSensorsAnalogAt0,
       "ctlCANSensorsAnalogAt75": ctlCANSensorsAnalogAt75,
       "ctlCANSensorsAnalogExpression": ctlCANSensorsAnalogExpression,
       "ctlCANSensorsAnalogSpecific": ctlCANSensorsAnalogSpecific,
       "ctlCANSensorsAnalogHystType": ctlCANSensorsAnalogHystType,
       "ctlCANSensorsAnalogHystValue": ctlCANSensorsAnalogHystValue,
       "ctlCANSensorsAnalogHystLowAlarm": ctlCANSensorsAnalogHystLowAlarm,
       "ctlCANSensorsAnalogHystLowWarning": ctlCANSensorsAnalogHystLowWarning,
       "ctlCANSensorsAnalogHystNormal": ctlCANSensorsAnalogHystNormal,
       "ctlCANSensorsAnalogHystHighWarning": ctlCANSensorsAnalogHystHighWarning,
       "ctlCANSensorsAnalogHystHighAlarm": ctlCANSensorsAnalogHystHighAlarm,
       "ctlCANSensorsAnalogValueInt": ctlCANSensorsAnalogValueInt,
       "ctlCANSensorsOutletsTable": ctlCANSensorsOutletsTable,
       "ctlCANSensorsOutletsEntry": ctlCANSensorsOutletsEntry,
       "ctlCANSensorsOutletId": ctlCANSensorsOutletId,
       "ctlCANSensorsOutletModule": ctlCANSensorsOutletModule,
       "ctlCANSensorsOutletNum": ctlCANSensorsOutletNum,
       "ctlCANSensorsOutletType": ctlCANSensorsOutletType,
       "ctlCANSensorsOutletName": ctlCANSensorsOutletName,
       "ctlCANSensorsOutletState": ctlCANSensorsOutletState,
       "ctlCANSensorsOutletValue": ctlCANSensorsOutletValue,
       "ctlCANSensorsOutletInitial": ctlCANSensorsOutletInitial,
       "ctlCANSensorsDiscretPulse": ctlCANSensorsDiscretPulse,
       "ctlRsSensors": ctlRsSensors,
       "ctlRsSensorsDiscretsTable": ctlRsSensorsDiscretsTable,
       "ctlRsSensorsDiscretsEntry": ctlRsSensorsDiscretsEntry,
       "ctlRsSensorsDiscretId": ctlRsSensorsDiscretId,
       "ctlRsSensorsDiscretModule": ctlRsSensorsDiscretModule,
       "ctlRsSensorsDiscretNum": ctlRsSensorsDiscretNum,
       "ctlRsSensorsDiscretType": ctlRsSensorsDiscretType,
       "ctlRsSensorsDiscretName": ctlRsSensorsDiscretName,
       "ctlRsSensorsDiscretState": ctlRsSensorsDiscretState,
       "ctlRsSensorsDiscretValue": ctlRsSensorsDiscretValue,
       "ctlRsSensorsDiscretReset": ctlRsSensorsDiscretReset,
       "ctlRsSensorsDiscretLevel": ctlRsSensorsDiscretLevel,
       "ctlRsSensorsDiscretReverse": ctlRsSensorsDiscretReverse,
       "ctlRsSensorsDiscretSpecific": ctlRsSensorsDiscretSpecific,
       "ctlRsSensorsAnalogsTable": ctlRsSensorsAnalogsTable,
       "ctlRsSensorsAnalogsEntry": ctlRsSensorsAnalogsEntry,
       "ctlRsSensorsAnalogId": ctlRsSensorsAnalogId,
       "ctlRsSensorsAnalogModule": ctlRsSensorsAnalogModule,
       "ctlRsSensorsAnalogNum": ctlRsSensorsAnalogNum,
       "ctlRsSensorsAnalogType": ctlRsSensorsAnalogType,
       "ctlRsSensorsAnalogName": ctlRsSensorsAnalogName,
       "ctlRsSensorsAnalogState": ctlRsSensorsAnalogState,
       "ctlRsSensorsAnalogValue": ctlRsSensorsAnalogValue,
       "ctlRsSensorsAnalogMin": ctlRsSensorsAnalogMin,
       "ctlRsSensorsAnalogMax": ctlRsSensorsAnalogMax,
       "ctlRsSensorsAnalogLowAlarm": ctlRsSensorsAnalogLowAlarm,
       "ctlRsSensorsAnalogLowWarning": ctlRsSensorsAnalogLowWarning,
       "ctlRsSensorsAnalogHighWarning": ctlRsSensorsAnalogHighWarning,
       "ctlRsSensorsAnalogHighAlarm": ctlRsSensorsAnalogHighAlarm,
       "ctlRsSensorsAnalogAt0": ctlRsSensorsAnalogAt0,
       "ctlRsSensorsAnalogAt75": ctlRsSensorsAnalogAt75,
       "ctlRsSensorsAnalogExpression": ctlRsSensorsAnalogExpression,
       "ctlRsSensorsAnalogSpecific": ctlRsSensorsAnalogSpecific,
       "ctlRsSensorsOutletsTable": ctlRsSensorsOutletsTable,
       "ctlRsSensorsOutletsEntry": ctlRsSensorsOutletsEntry,
       "ctlRsSensorsOutletId": ctlRsSensorsOutletId,
       "ctlRsSensorsOutletModule": ctlRsSensorsOutletModule,
       "ctlRsSensorsOutletNum": ctlRsSensorsOutletNum,
       "ctlRsSensorsOutletType": ctlRsSensorsOutletType,
       "ctlRsSensorsOutletName": ctlRsSensorsOutletName,
       "ctlRsSensorsOutletState": ctlRsSensorsOutletState,
       "ctlRsSensorsOutletValue": ctlRsSensorsOutletValue,
       "ctlRsSensorsOutletInitial": ctlRsSensorsOutletInitial,
       "ctlRsSensorsDiscretPulse": ctlRsSensorsDiscretPulse}
)
