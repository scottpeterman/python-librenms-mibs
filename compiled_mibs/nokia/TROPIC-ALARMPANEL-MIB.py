# SNMP MIB module (TROPIC-ALARMPANEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-ALARMPANEL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:21 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(tnAlarmPanelMIB,
 tnMiscModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnAlarmPanelMIB",
    "tnMiscModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(TnCommand,
 TnTrapCategory,
 TropicCardCLEI,
 TropicCardHFD,
 TropicCardManufacturingPartNumber,
 TropicCardMarketingPartNumber,
 TropicCardSerialNumber,
 TropicLEDColorType,
 TropicLEDStateType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCommand",
    "TnTrapCategory",
    "TropicCardCLEI",
    "TropicCardHFD",
    "TropicCardManufacturingPartNumber",
    "TropicCardMarketingPartNumber",
    "TropicCardSerialNumber",
    "TropicLEDColorType",
    "TropicLEDStateType")


# MODULE-IDENTITY

tnAlarmPanelMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    tnAlarmPanelMibModule.setRevisions(
        ("2018-02-23 12:00",
         "2016-11-16 12:00",
         "2014-01-13 12:00",
         "2013-05-20 12:00",
         "2013-03-14 12:00",
         "2012-03-29 12:00",
         "2010-04-16 12:00",
         "2010-01-06 12:00",
         "2009-09-01 12:00",
         "2009-08-24 12:00",
         "2009-05-21 12:00",
         "2009-03-03 12:00",
         "2009-02-27 12:00",
         "2008-05-29 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnAlarmPanelConf_ObjectIdentity = ObjectIdentity
tnAlarmPanelConf = _TnAlarmPanelConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 1)
)
_TnAlarmPanelGroups_ObjectIdentity = ObjectIdentity
tnAlarmPanelGroups = _TnAlarmPanelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 1, 1)
)
_TnAlarmPanelCompliances_ObjectIdentity = ObjectIdentity
tnAlarmPanelCompliances = _TnAlarmPanelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 1, 2)
)
_TnAlarmPanelObjs_ObjectIdentity = ObjectIdentity
tnAlarmPanelObjs = _TnAlarmPanelObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2)
)
_TnAlarmPanelBasics_ObjectIdentity = ObjectIdentity
tnAlarmPanelBasics = _TnAlarmPanelBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1)
)
_TnUserInterfacePanelTable_Object = MibTable
tnUserInterfacePanelTable = _TnUserInterfacePanelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelTable.setStatus("current")
_TnUserInterfacePanelEntry_Object = MibTableRow
tnUserInterfacePanelEntry = _TnUserInterfacePanelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1)
)
tnUserInterfacePanelEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelEntry.setStatus("current")


class _TnUserInterfacePanelName_Type(SnmpAdminString):
    """Custom type tnUserInterfacePanelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnUserInterfacePanelName_Type.__name__ = "SnmpAdminString"
_TnUserInterfacePanelName_Object = MibTableColumn
tnUserInterfacePanelName = _TnUserInterfacePanelName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 1),
    _TnUserInterfacePanelName_Type()
)
tnUserInterfacePanelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelName.setStatus("current")


class _TnUserInterfacePanelDescr_Type(SnmpAdminString):
    """Custom type tnUserInterfacePanelDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnUserInterfacePanelDescr_Type.__name__ = "SnmpAdminString"
_TnUserInterfacePanelDescr_Object = MibTableColumn
tnUserInterfacePanelDescr = _TnUserInterfacePanelDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 2),
    _TnUserInterfacePanelDescr_Type()
)
tnUserInterfacePanelDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelDescr.setStatus("current")
_TnUserInterfacePanelCLEI_Type = TropicCardCLEI
_TnUserInterfacePanelCLEI_Object = MibTableColumn
tnUserInterfacePanelCLEI = _TnUserInterfacePanelCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 3),
    _TnUserInterfacePanelCLEI_Type()
)
tnUserInterfacePanelCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCLEI.setStatus("current")
_TnUserInterfacePanelHFD_Type = TropicCardHFD
_TnUserInterfacePanelHFD_Object = MibTableColumn
tnUserInterfacePanelHFD = _TnUserInterfacePanelHFD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 4),
    _TnUserInterfacePanelHFD_Type()
)
tnUserInterfacePanelHFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelHFD.setStatus("current")
_TnUserInterfacePanelSerialNumber_Type = TropicCardSerialNumber
_TnUserInterfacePanelSerialNumber_Object = MibTableColumn
tnUserInterfacePanelSerialNumber = _TnUserInterfacePanelSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 5),
    _TnUserInterfacePanelSerialNumber_Type()
)
tnUserInterfacePanelSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelSerialNumber.setStatus("current")
_TnUserInterfacePanelManufacturingPartNumber_Type = TropicCardManufacturingPartNumber
_TnUserInterfacePanelManufacturingPartNumber_Object = MibTableColumn
tnUserInterfacePanelManufacturingPartNumber = _TnUserInterfacePanelManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 6),
    _TnUserInterfacePanelManufacturingPartNumber_Type()
)
tnUserInterfacePanelManufacturingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelManufacturingPartNumber.setStatus("current")
_TnUserInterfacePanelMarketingPartNumber_Type = TropicCardMarketingPartNumber
_TnUserInterfacePanelMarketingPartNumber_Object = MibTableColumn
tnUserInterfacePanelMarketingPartNumber = _TnUserInterfacePanelMarketingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 7),
    _TnUserInterfacePanelMarketingPartNumber_Type()
)
tnUserInterfacePanelMarketingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelMarketingPartNumber.setStatus("current")
_TnUserInterfacePanelACOLEDColor_Type = TropicLEDColorType
_TnUserInterfacePanelACOLEDColor_Object = MibTableColumn
tnUserInterfacePanelACOLEDColor = _TnUserInterfacePanelACOLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 8),
    _TnUserInterfacePanelACOLEDColor_Type()
)
tnUserInterfacePanelACOLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelACOLEDColor.setStatus("current")
_TnUserInterfacePanelACOLEDState_Type = TropicLEDStateType
_TnUserInterfacePanelACOLEDState_Object = MibTableColumn
tnUserInterfacePanelACOLEDState = _TnUserInterfacePanelACOLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 9),
    _TnUserInterfacePanelACOLEDState_Type()
)
tnUserInterfacePanelACOLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelACOLEDState.setStatus("current")
_TnUserInterfacePanelNodeCriticalLEDColor_Type = TropicLEDColorType
_TnUserInterfacePanelNodeCriticalLEDColor_Object = MibTableColumn
tnUserInterfacePanelNodeCriticalLEDColor = _TnUserInterfacePanelNodeCriticalLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 10),
    _TnUserInterfacePanelNodeCriticalLEDColor_Type()
)
tnUserInterfacePanelNodeCriticalLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeCriticalLEDColor.setStatus("current")
_TnUserInterfacePanelNodeCriticalLEDState_Type = TropicLEDStateType
_TnUserInterfacePanelNodeCriticalLEDState_Object = MibTableColumn
tnUserInterfacePanelNodeCriticalLEDState = _TnUserInterfacePanelNodeCriticalLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 11),
    _TnUserInterfacePanelNodeCriticalLEDState_Type()
)
tnUserInterfacePanelNodeCriticalLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeCriticalLEDState.setStatus("current")
_TnUserInterfacePanelNodeMajorLEDColor_Type = TropicLEDColorType
_TnUserInterfacePanelNodeMajorLEDColor_Object = MibTableColumn
tnUserInterfacePanelNodeMajorLEDColor = _TnUserInterfacePanelNodeMajorLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 12),
    _TnUserInterfacePanelNodeMajorLEDColor_Type()
)
tnUserInterfacePanelNodeMajorLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeMajorLEDColor.setStatus("current")
_TnUserInterfacePanelNodeMajorLEDState_Type = TropicLEDStateType
_TnUserInterfacePanelNodeMajorLEDState_Object = MibTableColumn
tnUserInterfacePanelNodeMajorLEDState = _TnUserInterfacePanelNodeMajorLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 13),
    _TnUserInterfacePanelNodeMajorLEDState_Type()
)
tnUserInterfacePanelNodeMajorLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeMajorLEDState.setStatus("current")
_TnUserInterfacePanelNodeMinorLEDColor_Type = TropicLEDColorType
_TnUserInterfacePanelNodeMinorLEDColor_Object = MibTableColumn
tnUserInterfacePanelNodeMinorLEDColor = _TnUserInterfacePanelNodeMinorLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 14),
    _TnUserInterfacePanelNodeMinorLEDColor_Type()
)
tnUserInterfacePanelNodeMinorLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeMinorLEDColor.setStatus("current")
_TnUserInterfacePanelNodeMinorLEDState_Type = TropicLEDStateType
_TnUserInterfacePanelNodeMinorLEDState_Object = MibTableColumn
tnUserInterfacePanelNodeMinorLEDState = _TnUserInterfacePanelNodeMinorLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 15),
    _TnUserInterfacePanelNodeMinorLEDState_Type()
)
tnUserInterfacePanelNodeMinorLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeMinorLEDState.setStatus("current")
_TnUserInterfacePanelShelfLEDColor_Type = TropicLEDColorType
_TnUserInterfacePanelShelfLEDColor_Object = MibTableColumn
tnUserInterfacePanelShelfLEDColor = _TnUserInterfacePanelShelfLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 16),
    _TnUserInterfacePanelShelfLEDColor_Type()
)
tnUserInterfacePanelShelfLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelShelfLEDColor.setStatus("current")
_TnUserInterfacePanelShelfLEDState_Type = TropicLEDStateType
_TnUserInterfacePanelShelfLEDState_Object = MibTableColumn
tnUserInterfacePanelShelfLEDState = _TnUserInterfacePanelShelfLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 17),
    _TnUserInterfacePanelShelfLEDState_Type()
)
tnUserInterfacePanelShelfLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelShelfLEDState.setStatus("current")
_TnUserInterfacePanelACO_Type = TnCommand
_TnUserInterfacePanelACO_Object = MibTableColumn
tnUserInterfacePanelACO = _TnUserInterfacePanelACO_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 18),
    _TnUserInterfacePanelACO_Type()
)
tnUserInterfacePanelACO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelACO.setStatus("current")
_TnUserInterfacePanelNodeWarningLEDColor_Type = TropicLEDColorType
_TnUserInterfacePanelNodeWarningLEDColor_Object = MibTableColumn
tnUserInterfacePanelNodeWarningLEDColor = _TnUserInterfacePanelNodeWarningLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 19),
    _TnUserInterfacePanelNodeWarningLEDColor_Type()
)
tnUserInterfacePanelNodeWarningLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeWarningLEDColor.setStatus("current")
_TnUserInterfacePanelNodeWarningLEDState_Type = TropicLEDStateType
_TnUserInterfacePanelNodeWarningLEDState_Object = MibTableColumn
tnUserInterfacePanelNodeWarningLEDState = _TnUserInterfacePanelNodeWarningLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 3, 1, 20),
    _TnUserInterfacePanelNodeWarningLEDState_Type()
)
tnUserInterfacePanelNodeWarningLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserInterfacePanelNodeWarningLEDState.setStatus("current")
_TnUserInterfacePanelCpiTable_Object = MibTable
tnUserInterfacePanelCpiTable = _TnUserInterfacePanelCpiTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpiTable.setStatus("current")
_TnUserInterfacePanelCpiEntry_Object = MibTableRow
tnUserInterfacePanelCpiEntry = _TnUserInterfacePanelCpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 4, 1)
)
tnUserInterfacePanelCpiEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpiIndex"),
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpiEntry.setStatus("current")
_TnUserInterfacePanelCpiIndex_Type = Unsigned32
_TnUserInterfacePanelCpiIndex_Object = MibTableColumn
tnUserInterfacePanelCpiIndex = _TnUserInterfacePanelCpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 4, 1, 1),
    _TnUserInterfacePanelCpiIndex_Type()
)
tnUserInterfacePanelCpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpiIndex.setStatus("current")


class _TnUserInterfacePanelCpiAlarmMsg_Type(SnmpAdminString):
    """Custom type tnUserInterfacePanelCpiAlarmMsg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_TnUserInterfacePanelCpiAlarmMsg_Type.__name__ = "SnmpAdminString"
_TnUserInterfacePanelCpiAlarmMsg_Object = MibTableColumn
tnUserInterfacePanelCpiAlarmMsg = _TnUserInterfacePanelCpiAlarmMsg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 4, 1, 3),
    _TnUserInterfacePanelCpiAlarmMsg_Type()
)
tnUserInterfacePanelCpiAlarmMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpiAlarmMsg.setStatus("current")


class _TnUserInterfacePanelCpiPolarity_Type(Integer32):
    """Custom type tnUserInterfacePanelCpiPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alow", 1),
          ("ahigh", 2))
    )


_TnUserInterfacePanelCpiPolarity_Type.__name__ = "Integer32"
_TnUserInterfacePanelCpiPolarity_Object = MibTableColumn
tnUserInterfacePanelCpiPolarity = _TnUserInterfacePanelCpiPolarity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 4, 1, 4),
    _TnUserInterfacePanelCpiPolarity_Type()
)
tnUserInterfacePanelCpiPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpiPolarity.setStatus("current")
_TnUserInterfacePanelCpiCategory_Type = TnTrapCategory
_TnUserInterfacePanelCpiCategory_Object = MibTableColumn
tnUserInterfacePanelCpiCategory = _TnUserInterfacePanelCpiCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 4, 1, 5),
    _TnUserInterfacePanelCpiCategory_Type()
)
tnUserInterfacePanelCpiCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpiCategory.setStatus("current")
_TnUserInterfacePanelCpoTable_Object = MibTable
tnUserInterfacePanelCpoTable = _TnUserInterfacePanelCpoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpoTable.setStatus("current")
_TnUserInterfacePanelCpoEntry_Object = MibTableRow
tnUserInterfacePanelCpoEntry = _TnUserInterfacePanelCpoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 5, 1)
)
tnUserInterfacePanelCpoEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpoIndex"),
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpoEntry.setStatus("current")
_TnUserInterfacePanelCpoIndex_Type = Unsigned32
_TnUserInterfacePanelCpoIndex_Object = MibTableColumn
tnUserInterfacePanelCpoIndex = _TnUserInterfacePanelCpoIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 5, 1, 1),
    _TnUserInterfacePanelCpoIndex_Type()
)
tnUserInterfacePanelCpoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpoIndex.setStatus("current")


class _TnUserInterfacePanelCpoConState_Type(Integer32):
    """Custom type tnUserInterfacePanelCpoConState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rls", 1),
          ("opr", 2),
          ("auto", 3),
          ("racklamp", 4))
    )


_TnUserInterfacePanelCpoConState_Type.__name__ = "Integer32"
_TnUserInterfacePanelCpoConState_Object = MibTableColumn
tnUserInterfacePanelCpoConState = _TnUserInterfacePanelCpoConState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 5, 1, 2),
    _TnUserInterfacePanelCpoConState_Type()
)
tnUserInterfacePanelCpoConState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpoConState.setStatus("current")


class _TnUserInterfacePanelCpoContType_Type(SnmpAdminString):
    """Custom type tnUserInterfacePanelCpoContType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_TnUserInterfacePanelCpoContType_Type.__name__ = "SnmpAdminString"
_TnUserInterfacePanelCpoContType_Object = MibTableColumn
tnUserInterfacePanelCpoContType = _TnUserInterfacePanelCpoContType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 5, 1, 3),
    _TnUserInterfacePanelCpoContType_Type()
)
tnUserInterfacePanelCpoContType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpoContType.setStatus("current")
_TnUserInterfacePanelCpoConnTo_Type = InterfaceIndexOrZero
_TnUserInterfacePanelCpoConnTo_Object = MibTableColumn
tnUserInterfacePanelCpoConnTo = _TnUserInterfacePanelCpoConnTo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 2, 1, 5, 1, 5),
    _TnUserInterfacePanelCpoConnTo_Type()
)
tnUserInterfacePanelCpoConnTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpoConnTo.setStatus("current")

# Managed Objects groups

tnUserInterfacePanelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 1, 1, 3)
)
tnUserInterfacePanelGroup.setObjects(
      *(("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelName"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelDescr"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCLEI"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelHFD"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelSerialNumber"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelManufacturingPartNumber"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelMarketingPartNumber"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelACOLEDColor"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelACOLEDState"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeCriticalLEDColor"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeCriticalLEDState"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeMajorLEDColor"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeMajorLEDState"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeMinorLEDColor"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeMinorLEDState"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelShelfLEDColor"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelShelfLEDState"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelACO"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeWarningLEDColor"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelNodeWarningLEDState"))
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelGroup.setStatus("current")

tnUserInterfacePanelCpiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 1, 1, 4)
)
tnUserInterfacePanelCpiGroup.setObjects(
      *(("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpiAlarmMsg"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpiPolarity"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpiCategory"))
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpiGroup.setStatus("current")

tnUserInterfacePanelCpoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 1, 1, 5)
)
tnUserInterfacePanelCpoGroup.setObjects(
      *(("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpoConState"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpoContType"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpoConnTo"))
)
if mibBuilder.loadTexts:
    tnUserInterfacePanelCpoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnAlarmPanelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3, 1, 2, 1)
)
tnAlarmPanelCompliance.setObjects(
      *(("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelGroup"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpiGroup"),
        ("TROPIC-ALARMPANEL-MIB", "tnUserInterfacePanelCpoGroup"))
)
if mibBuilder.loadTexts:
    tnAlarmPanelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-ALARMPANEL-MIB",
    **{"tnAlarmPanelMibModule": tnAlarmPanelMibModule,
       "tnAlarmPanelConf": tnAlarmPanelConf,
       "tnAlarmPanelGroups": tnAlarmPanelGroups,
       "tnUserInterfacePanelGroup": tnUserInterfacePanelGroup,
       "tnUserInterfacePanelCpiGroup": tnUserInterfacePanelCpiGroup,
       "tnUserInterfacePanelCpoGroup": tnUserInterfacePanelCpoGroup,
       "tnAlarmPanelCompliances": tnAlarmPanelCompliances,
       "tnAlarmPanelCompliance": tnAlarmPanelCompliance,
       "tnAlarmPanelObjs": tnAlarmPanelObjs,
       "tnAlarmPanelBasics": tnAlarmPanelBasics,
       "tnUserInterfacePanelTable": tnUserInterfacePanelTable,
       "tnUserInterfacePanelEntry": tnUserInterfacePanelEntry,
       "tnUserInterfacePanelName": tnUserInterfacePanelName,
       "tnUserInterfacePanelDescr": tnUserInterfacePanelDescr,
       "tnUserInterfacePanelCLEI": tnUserInterfacePanelCLEI,
       "tnUserInterfacePanelHFD": tnUserInterfacePanelHFD,
       "tnUserInterfacePanelSerialNumber": tnUserInterfacePanelSerialNumber,
       "tnUserInterfacePanelManufacturingPartNumber": tnUserInterfacePanelManufacturingPartNumber,
       "tnUserInterfacePanelMarketingPartNumber": tnUserInterfacePanelMarketingPartNumber,
       "tnUserInterfacePanelACOLEDColor": tnUserInterfacePanelACOLEDColor,
       "tnUserInterfacePanelACOLEDState": tnUserInterfacePanelACOLEDState,
       "tnUserInterfacePanelNodeCriticalLEDColor": tnUserInterfacePanelNodeCriticalLEDColor,
       "tnUserInterfacePanelNodeCriticalLEDState": tnUserInterfacePanelNodeCriticalLEDState,
       "tnUserInterfacePanelNodeMajorLEDColor": tnUserInterfacePanelNodeMajorLEDColor,
       "tnUserInterfacePanelNodeMajorLEDState": tnUserInterfacePanelNodeMajorLEDState,
       "tnUserInterfacePanelNodeMinorLEDColor": tnUserInterfacePanelNodeMinorLEDColor,
       "tnUserInterfacePanelNodeMinorLEDState": tnUserInterfacePanelNodeMinorLEDState,
       "tnUserInterfacePanelShelfLEDColor": tnUserInterfacePanelShelfLEDColor,
       "tnUserInterfacePanelShelfLEDState": tnUserInterfacePanelShelfLEDState,
       "tnUserInterfacePanelACO": tnUserInterfacePanelACO,
       "tnUserInterfacePanelNodeWarningLEDColor": tnUserInterfacePanelNodeWarningLEDColor,
       "tnUserInterfacePanelNodeWarningLEDState": tnUserInterfacePanelNodeWarningLEDState,
       "tnUserInterfacePanelCpiTable": tnUserInterfacePanelCpiTable,
       "tnUserInterfacePanelCpiEntry": tnUserInterfacePanelCpiEntry,
       "tnUserInterfacePanelCpiIndex": tnUserInterfacePanelCpiIndex,
       "tnUserInterfacePanelCpiAlarmMsg": tnUserInterfacePanelCpiAlarmMsg,
       "tnUserInterfacePanelCpiPolarity": tnUserInterfacePanelCpiPolarity,
       "tnUserInterfacePanelCpiCategory": tnUserInterfacePanelCpiCategory,
       "tnUserInterfacePanelCpoTable": tnUserInterfacePanelCpoTable,
       "tnUserInterfacePanelCpoEntry": tnUserInterfacePanelCpoEntry,
       "tnUserInterfacePanelCpoIndex": tnUserInterfacePanelCpoIndex,
       "tnUserInterfacePanelCpoConState": tnUserInterfacePanelCpoConState,
       "tnUserInterfacePanelCpoContType": tnUserInterfacePanelCpoContType,
       "tnUserInterfacePanelCpoConnTo": tnUserInterfacePanelCpoConnTo}
)
