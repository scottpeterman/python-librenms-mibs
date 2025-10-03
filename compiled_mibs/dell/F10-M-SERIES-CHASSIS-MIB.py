# SNMP MIB module (F10-M-SERIES-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\F10-M-SERIES-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:06 2025
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

(chAlarmVarInteger,
 chAlarmVarPort,
 chAlarmVarSlot,
 chAlarmVarString) = mibBuilder.importSymbols(
    "F10-CHASSIS-MIB",
    "chAlarmVarInteger",
    "chAlarmVarPort",
    "chAlarmVarSlot",
    "chAlarmVarString")

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(F10ChassisType,
 F10HundredthdB,
 F10MSeriesPortType,
 F10MfgDate,
 F10ProcessorModuleType,
 F10SwDate) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "F10ChassisType",
    "F10HundredthdB",
    "F10MSeriesPortType",
    "F10MfgDate",
    "F10ProcessorModuleType",
    "F10SwDate")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

f10MSerChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19)
)
if mibBuilder.loadTexts:
    f10MSerChassisMib.setRevisions(
        ("2012-11-02 12:00",
         "2012-12-03 12:00",
         "2012-03-27 12:00",
         "2007-10-03 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CodeType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


class UnitType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_F10MSerChassisObject_ObjectIdentity = ObjectIdentity
f10MSerChassisObject = _F10MSerChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1)
)
_ChObjects_ObjectIdentity = ObjectIdentity
chObjects = _ChObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 1)
)
_ChNumStackUnits_Type = Integer32
_ChNumStackUnits_Object = MibScalar
chNumStackUnits = _ChNumStackUnits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 1, 1),
    _ChNumStackUnits_Type()
)
chNumStackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumStackUnits.setStatus("current")
_ChNumMaxStackableUnits_Type = Integer32
_ChNumMaxStackableUnits_Object = MibScalar
chNumMaxStackableUnits = _ChNumMaxStackableUnits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 1, 2),
    _ChNumMaxStackableUnits_Type()
)
chNumMaxStackableUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumMaxStackableUnits.setStatus("current")


class _ChStackUnitIndexNext_Type(Integer32):
    """Custom type chStackUnitIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 6),
    )


_ChStackUnitIndexNext_Type.__name__ = "Integer32"
_ChStackUnitIndexNext_Object = MibScalar
chStackUnitIndexNext = _ChStackUnitIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 1, 3),
    _ChStackUnitIndexNext_Type()
)
chStackUnitIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitIndexNext.setStatus("current")
_ChSysObjects_ObjectIdentity = ObjectIdentity
chSysObjects = _ChSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2)
)
_ChStackUnitTable_Object = MibTable
chStackUnitTable = _ChStackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chStackUnitTable.setStatus("current")
_ChStackUnitEntry_Object = MibTableRow
chStackUnitEntry = _ChStackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1)
)
chStackUnitEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitIndex"),
)
if mibBuilder.loadTexts:
    chStackUnitEntry.setStatus("current")
_ChStackUnitIndex_Type = Integer32
_ChStackUnitIndex_Object = MibTableColumn
chStackUnitIndex = _ChStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 1),
    _ChStackUnitIndex_Type()
)
chStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chStackUnitIndex.setStatus("current")


class _ChStackUnitNumber_Type(Integer32):
    """Custom type chStackUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 6),
    )


_ChStackUnitNumber_Type.__name__ = "Integer32"
_ChStackUnitNumber_Object = MibTableColumn
chStackUnitNumber = _ChStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 2),
    _ChStackUnitNumber_Type()
)
chStackUnitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitNumber.setStatus("current")
_ChStackUnitSID_Type = Integer32
_ChStackUnitSID_Object = MibTableColumn
chStackUnitSID = _ChStackUnitSID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 3),
    _ChStackUnitSID_Type()
)
chStackUnitSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitSID.setStatus("deprecated")


class _ChStackUnitMgmtStatus_Type(Integer32):
    """Custom type chStackUnitMgmtStatus based on Integer32"""
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
        *(("mgmtUnit", 1),
          ("standbyUnit", 2),
          ("stackUnit", 3),
          ("unassigned", 4))
    )


_ChStackUnitMgmtStatus_Type.__name__ = "Integer32"
_ChStackUnitMgmtStatus_Object = MibTableColumn
chStackUnitMgmtStatus = _ChStackUnitMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 4),
    _ChStackUnitMgmtStatus_Type()
)
chStackUnitMgmtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitMgmtStatus.setStatus("current")


class _ChStackUnitHwMgmtPreference_Type(Integer32):
    """Custom type chStackUnitHwMgmtPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("unsassigned", 1),
          ("assigned", 2))
    )


_ChStackUnitHwMgmtPreference_Type.__name__ = "Integer32"
_ChStackUnitHwMgmtPreference_Object = MibTableColumn
chStackUnitHwMgmtPreference = _ChStackUnitHwMgmtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 5),
    _ChStackUnitHwMgmtPreference_Type()
)
chStackUnitHwMgmtPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitHwMgmtPreference.setStatus("current")


class _ChStackUnitAdmMgmtPreference_Type(Integer32):
    """Custom type chStackUnitAdmMgmtPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_ChStackUnitAdmMgmtPreference_Type.__name__ = "Integer32"
_ChStackUnitAdmMgmtPreference_Object = MibTableColumn
chStackUnitAdmMgmtPreference = _ChStackUnitAdmMgmtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 6),
    _ChStackUnitAdmMgmtPreference_Type()
)
chStackUnitAdmMgmtPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitAdmMgmtPreference.setStatus("current")
_ChStackUnitModelID_Type = DisplayString
_ChStackUnitModelID_Object = MibTableColumn
chStackUnitModelID = _ChStackUnitModelID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 7),
    _ChStackUnitModelID_Type()
)
chStackUnitModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitModelID.setStatus("current")


class _ChStackUnitStatus_Type(Integer32):
    """Custom type chStackUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("unsupported", 2),
          ("codeMismatch", 3),
          ("configMismatch", 4),
          ("unitDown", 5),
          ("notPresent", 6))
    )


_ChStackUnitStatus_Type.__name__ = "Integer32"
_ChStackUnitStatus_Object = MibTableColumn
chStackUnitStatus = _ChStackUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 8),
    _ChStackUnitStatus_Type()
)
chStackUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitStatus.setStatus("current")
_ChStackUnitDescription_Type = DisplayString
_ChStackUnitDescription_Object = MibTableColumn
chStackUnitDescription = _ChStackUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 9),
    _ChStackUnitDescription_Type()
)
chStackUnitDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitDescription.setStatus("current")
_ChStackUnitCodeVersion_Type = DisplayString
_ChStackUnitCodeVersion_Object = MibTableColumn
chStackUnitCodeVersion = _ChStackUnitCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 10),
    _ChStackUnitCodeVersion_Type()
)
chStackUnitCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCodeVersion.setStatus("current")
_ChStackUnitCodeVersionInFlash_Type = DisplayString
_ChStackUnitCodeVersionInFlash_Object = MibTableColumn
chStackUnitCodeVersionInFlash = _ChStackUnitCodeVersionInFlash_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 11),
    _ChStackUnitCodeVersionInFlash_Type()
)
chStackUnitCodeVersionInFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCodeVersionInFlash.setStatus("current")
_ChStackUnitSerialNumber_Type = DisplayString
_ChStackUnitSerialNumber_Object = MibTableColumn
chStackUnitSerialNumber = _ChStackUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 12),
    _ChStackUnitSerialNumber_Type()
)
chStackUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitSerialNumber.setStatus("current")
_ChStackUnitUpTime_Type = TimeTicks
_ChStackUnitUpTime_Object = MibTableColumn
chStackUnitUpTime = _ChStackUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 13),
    _ChStackUnitUpTime_Type()
)
chStackUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitUpTime.setStatus("current")
_ChStackUnitTemp_Type = Gauge32
_ChStackUnitTemp_Object = MibTableColumn
chStackUnitTemp = _ChStackUnitTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 14),
    _ChStackUnitTemp_Type()
)
chStackUnitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitTemp.setStatus("current")
_ChStackUnitType_Type = UnitType
_ChStackUnitType_Object = MibTableColumn
chStackUnitType = _ChStackUnitType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 15),
    _ChStackUnitType_Type()
)
chStackUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitType.setStatus("current")
_ChStackUnitSysType_Type = F10ChassisType
_ChStackUnitSysType_Object = MibTableColumn
chStackUnitSysType = _ChStackUnitSysType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 16),
    _ChStackUnitSysType_Type()
)
chStackUnitSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitSysType.setStatus("current")
_ChStackUnitVendorId_Type = DisplayString
_ChStackUnitVendorId_Object = MibTableColumn
chStackUnitVendorId = _ChStackUnitVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 17),
    _ChStackUnitVendorId_Type()
)
chStackUnitVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitVendorId.setStatus("current")
_ChStackUnitMfgDate_Type = F10MfgDate
_ChStackUnitMfgDate_Object = MibTableColumn
chStackUnitMfgDate = _ChStackUnitMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 18),
    _ChStackUnitMfgDate_Type()
)
chStackUnitMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitMfgDate.setStatus("current")
_ChStackUnitMacAddress_Type = MacAddress
_ChStackUnitMacAddress_Object = MibTableColumn
chStackUnitMacAddress = _ChStackUnitMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 19),
    _ChStackUnitMacAddress_Type()
)
chStackUnitMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitMacAddress.setStatus("current")
_ChStackUnitPartNum_Type = DisplayString
_ChStackUnitPartNum_Object = MibTableColumn
chStackUnitPartNum = _ChStackUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 20),
    _ChStackUnitPartNum_Type()
)
chStackUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitPartNum.setStatus("current")
_ChStackUnitProductRev_Type = DisplayString
_ChStackUnitProductRev_Object = MibTableColumn
chStackUnitProductRev = _ChStackUnitProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 21),
    _ChStackUnitProductRev_Type()
)
chStackUnitProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitProductRev.setStatus("current")
_ChStackUnitProductOrder_Type = DisplayString
_ChStackUnitProductOrder_Object = MibTableColumn
chStackUnitProductOrder = _ChStackUnitProductOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 22),
    _ChStackUnitProductOrder_Type()
)
chStackUnitProductOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitProductOrder.setStatus("current")


class _ChStackUnitCountryCode_Type(OctetString):
    """Custom type chStackUnitCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_ChStackUnitCountryCode_Type.__name__ = "OctetString"
_ChStackUnitCountryCode_Object = MibTableColumn
chStackUnitCountryCode = _ChStackUnitCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 23),
    _ChStackUnitCountryCode_Type()
)
chStackUnitCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCountryCode.setStatus("current")
_ChStackUnitNum10GigEtherPorts_Type = Integer32
_ChStackUnitNum10GigEtherPorts_Object = MibTableColumn
chStackUnitNum10GigEtherPorts = _ChStackUnitNum10GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 24),
    _ChStackUnitNum10GigEtherPorts_Type()
)
chStackUnitNum10GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNum10GigEtherPorts.setStatus("current")
_ChStackUnitNumGigEtherPorts_Type = Integer32
_ChStackUnitNumGigEtherPorts_Object = MibTableColumn
chStackUnitNumGigEtherPorts = _ChStackUnitNumGigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 25),
    _ChStackUnitNumGigEtherPorts_Type()
)
chStackUnitNumGigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumGigEtherPorts.setStatus("current")
_ChStackUnitNumFastEtherPorts_Type = Integer32
_ChStackUnitNumFastEtherPorts_Object = MibTableColumn
chStackUnitNumFastEtherPorts = _ChStackUnitNumFastEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 26),
    _ChStackUnitNumFastEtherPorts_Type()
)
chStackUnitNumFastEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumFastEtherPorts.setStatus("current")
_ChStackUnitNumFanTrays_Type = Integer32
_ChStackUnitNumFanTrays_Object = MibTableColumn
chStackUnitNumFanTrays = _ChStackUnitNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 27),
    _ChStackUnitNumFanTrays_Type()
)
chStackUnitNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumFanTrays.setStatus("current")
_ChStackUnitNumPowerSupplies_Type = Integer32
_ChStackUnitNumPowerSupplies_Object = MibTableColumn
chStackUnitNumPowerSupplies = _ChStackUnitNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 28),
    _ChStackUnitNumPowerSupplies_Type()
)
chStackUnitNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumPowerSupplies.setStatus("current")
_ChStackUnitNumPluggableModules_Type = Integer32
_ChStackUnitNumPluggableModules_Object = MibTableColumn
chStackUnitNumPluggableModules = _ChStackUnitNumPluggableModules_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 29),
    _ChStackUnitNumPluggableModules_Type()
)
chStackUnitNumPluggableModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumPluggableModules.setStatus("current")
_ChStackUnitNum40GigEtherPorts_Type = Integer32
_ChStackUnitNum40GigEtherPorts_Object = MibTableColumn
chStackUnitNum40GigEtherPorts = _ChStackUnitNum40GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 30),
    _ChStackUnitNum40GigEtherPorts_Type()
)
chStackUnitNum40GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNum40GigEtherPorts.setStatus("current")
_ChStackUnitRowStatus_Type = RowStatus
_ChStackUnitRowStatus_Object = MibTableColumn
chStackUnitRowStatus = _ChStackUnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 31),
    _ChStackUnitRowStatus_Type()
)
chStackUnitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitRowStatus.setStatus("current")


class _ChStackUnitPiecePartID_Type(DisplayString):
    """Custom type chStackUnitPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChStackUnitPiecePartID_Type.__name__ = "DisplayString"
_ChStackUnitPiecePartID_Object = MibTableColumn
chStackUnitPiecePartID = _ChStackUnitPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 32),
    _ChStackUnitPiecePartID_Type()
)
chStackUnitPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitPiecePartID.setStatus("current")


class _ChStackUnitPPIDRevision_Type(DisplayString):
    """Custom type chStackUnitPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChStackUnitPPIDRevision_Type.__name__ = "DisplayString"
_ChStackUnitPPIDRevision_Object = MibTableColumn
chStackUnitPPIDRevision = _ChStackUnitPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 33),
    _ChStackUnitPPIDRevision_Type()
)
chStackUnitPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitPPIDRevision.setStatus("current")


class _ChStackUnitServiceTag_Type(DisplayString):
    """Custom type chStackUnitServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChStackUnitServiceTag_Type.__name__ = "DisplayString"
_ChStackUnitServiceTag_Object = MibTableColumn
chStackUnitServiceTag = _ChStackUnitServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 34),
    _ChStackUnitServiceTag_Type()
)
chStackUnitServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitServiceTag.setStatus("current")


class _ChStackUnitExpressServiceCode_Type(DisplayString):
    """Custom type chStackUnitExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChStackUnitExpressServiceCode_Type.__name__ = "DisplayString"
_ChStackUnitExpressServiceCode_Object = MibTableColumn
chStackUnitExpressServiceCode = _ChStackUnitExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 1, 1, 35),
    _ChStackUnitExpressServiceCode_Type()
)
chStackUnitExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitExpressServiceCode.setStatus("current")
_ChSysPowerSupplyTable_Object = MibTable
chSysPowerSupplyTable = _ChSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    chSysPowerSupplyTable.setStatus("current")
_ChSysPowerSupplyEntry_Object = MibTableRow
chSysPowerSupplyEntry = _ChSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 2, 1)
)
chSysPowerSupplyEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-M-SERIES-CHASSIS-MIB", "chSysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    chSysPowerSupplyEntry.setStatus("current")
_ChSysPowerSupplyIndex_Type = Integer32
_ChSysPowerSupplyIndex_Object = MibTableColumn
chSysPowerSupplyIndex = _ChSysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 2, 1, 1),
    _ChSysPowerSupplyIndex_Type()
)
chSysPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyIndex.setStatus("current")


class _ChSysPowerSupplyOperStatus_Type(Integer32):
    """Custom type chSysPowerSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("shutdown", 4),
          ("notPresent", 5),
          ("notFunctioning", 6))
    )


_ChSysPowerSupplyOperStatus_Type.__name__ = "Integer32"
_ChSysPowerSupplyOperStatus_Object = MibTableColumn
chSysPowerSupplyOperStatus = _ChSysPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 2, 1, 2),
    _ChSysPowerSupplyOperStatus_Type()
)
chSysPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyOperStatus.setStatus("current")


class _ChSysPowerSupplyType_Type(Integer32):
    """Custom type chSysPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ac", 2),
          ("dc", 3),
          ("externalPowerSupply", 4),
          ("internalRedundant", 5))
    )


_ChSysPowerSupplyType_Type.__name__ = "Integer32"
_ChSysPowerSupplyType_Object = MibTableColumn
chSysPowerSupplyType = _ChSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 2, 1, 3),
    _ChSysPowerSupplyType_Type()
)
chSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyType.setStatus("current")
_ChSysFanTrayTable_Object = MibTable
chSysFanTrayTable = _ChSysFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 3)
)
if mibBuilder.loadTexts:
    chSysFanTrayTable.setStatus("current")
_ChSysFanTrayEntry_Object = MibTableRow
chSysFanTrayEntry = _ChSysFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 3, 1)
)
chSysFanTrayEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-M-SERIES-CHASSIS-MIB", "chSysFanTrayIndex"),
)
if mibBuilder.loadTexts:
    chSysFanTrayEntry.setStatus("current")
_ChSysFanTrayIndex_Type = Integer32
_ChSysFanTrayIndex_Object = MibTableColumn
chSysFanTrayIndex = _ChSysFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 3, 1, 1),
    _ChSysFanTrayIndex_Type()
)
chSysFanTrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayIndex.setStatus("current")


class _ChSysFanTrayOperStatus_Type(Integer32):
    """Custom type chSysFanTrayOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ChSysFanTrayOperStatus_Type.__name__ = "Integer32"
_ChSysFanTrayOperStatus_Object = MibTableColumn
chSysFanTrayOperStatus = _ChSysFanTrayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 3, 1, 2),
    _ChSysFanTrayOperStatus_Type()
)
chSysFanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayOperStatus.setStatus("current")
_ChSysPortTable_Object = MibTable
chSysPortTable = _ChSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4)
)
if mibBuilder.loadTexts:
    chSysPortTable.setStatus("current")
_ChSysPortEntry_Object = MibTableRow
chSysPortEntry = _ChSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1)
)
chSysPortEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-M-SERIES-CHASSIS-MIB", "chSysPortIndex"),
)
if mibBuilder.loadTexts:
    chSysPortEntry.setStatus("current")
_ChSysPortIndex_Type = Integer32
_ChSysPortIndex_Object = MibTableColumn
chSysPortIndex = _ChSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 1),
    _ChSysPortIndex_Type()
)
chSysPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIndex.setStatus("current")
_ChSysPortType_Type = F10MSeriesPortType
_ChSysPortType_Object = MibTableColumn
chSysPortType = _ChSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 2),
    _ChSysPortType_Type()
)
chSysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortType.setStatus("current")


class _ChSysPortAdminStatus_Type(Integer32):
    """Custom type chSysPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ChSysPortAdminStatus_Type.__name__ = "Integer32"
_ChSysPortAdminStatus_Object = MibTableColumn
chSysPortAdminStatus = _ChSysPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 3),
    _ChSysPortAdminStatus_Type()
)
chSysPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortAdminStatus.setStatus("current")


class _ChSysPortOperStatus_Type(Integer32):
    """Custom type chSysPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("portDown", 2),
          ("portProblem", 3),
          ("cardProblem", 4),
          ("cardDown", 5),
          ("notPresent", 6))
    )


_ChSysPortOperStatus_Type.__name__ = "Integer32"
_ChSysPortOperStatus_Object = MibTableColumn
chSysPortOperStatus = _ChSysPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 4),
    _ChSysPortOperStatus_Type()
)
chSysPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortOperStatus.setStatus("current")
_ChSysPortIfIndex_Type = Integer32
_ChSysPortIfIndex_Object = MibTableColumn
chSysPortIfIndex = _ChSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 5),
    _ChSysPortIfIndex_Type()
)
chSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIfIndex.setStatus("current")
_ChSysPortXfpRecvPower_Type = F10HundredthdB
_ChSysPortXfpRecvPower_Object = MibTableColumn
chSysPortXfpRecvPower = _ChSysPortXfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 6),
    _ChSysPortXfpRecvPower_Type()
)
chSysPortXfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortXfpRecvPower.setStatus("current")
if mibBuilder.loadTexts:
    chSysPortXfpRecvPower.setUnits("dB")
_ChSysPortXfpRecvTemp_Type = Integer32
_ChSysPortXfpRecvTemp_Object = MibTableColumn
chSysPortXfpRecvTemp = _ChSysPortXfpRecvTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 7),
    _ChSysPortXfpRecvTemp_Type()
)
chSysPortXfpRecvTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortXfpRecvTemp.setStatus("current")
_ChSysPortXfpTxPower_Type = F10HundredthdB
_ChSysPortXfpTxPower_Object = MibTableColumn
chSysPortXfpTxPower = _ChSysPortXfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 4, 1, 8),
    _ChSysPortXfpTxPower_Type()
)
chSysPortXfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortXfpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    chSysPortXfpTxPower.setUnits("dB")
_ChSysStackPortTable_Object = MibTable
chSysStackPortTable = _ChSysStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5)
)
if mibBuilder.loadTexts:
    chSysStackPortTable.setStatus("current")
_ChSysStackPortEntry_Object = MibTableRow
chSysStackPortEntry = _ChSysStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1)
)
chSysStackPortEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-M-SERIES-CHASSIS-MIB", "chSysStackPortIndex"),
)
if mibBuilder.loadTexts:
    chSysStackPortEntry.setStatus("current")
_ChSysStackPortIndex_Type = Integer32
_ChSysStackPortIndex_Object = MibTableColumn
chSysStackPortIndex = _ChSysStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 1),
    _ChSysStackPortIndex_Type()
)
chSysStackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortIndex.setStatus("current")


class _ChSysStackPortConfiguredMode_Type(Integer32):
    """Custom type chSysStackPortConfiguredMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stack", 1),
          ("ethernet", 2),
          ("unknown", 3))
    )


_ChSysStackPortConfiguredMode_Type.__name__ = "Integer32"
_ChSysStackPortConfiguredMode_Object = MibTableColumn
chSysStackPortConfiguredMode = _ChSysStackPortConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 2),
    _ChSysStackPortConfiguredMode_Type()
)
chSysStackPortConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortConfiguredMode.setStatus("current")


class _ChSysStackPortRunningMode_Type(Integer32):
    """Custom type chSysStackPortRunningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stack", 1),
          ("ethernet", 2),
          ("unknown", 3))
    )


_ChSysStackPortRunningMode_Type.__name__ = "Integer32"
_ChSysStackPortRunningMode_Object = MibTableColumn
chSysStackPortRunningMode = _ChSysStackPortRunningMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 3),
    _ChSysStackPortRunningMode_Type()
)
chSysStackPortRunningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortRunningMode.setStatus("current")


class _ChSysStackPortLinkStatus_Type(Integer32):
    """Custom type chSysStackPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ChSysStackPortLinkStatus_Type.__name__ = "Integer32"
_ChSysStackPortLinkStatus_Object = MibTableColumn
chSysStackPortLinkStatus = _ChSysStackPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 4),
    _ChSysStackPortLinkStatus_Type()
)
chSysStackPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortLinkStatus.setStatus("current")
_ChSysStackPortLinkSpeed_Type = Gauge32
_ChSysStackPortLinkSpeed_Object = MibTableColumn
chSysStackPortLinkSpeed = _ChSysStackPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 5),
    _ChSysStackPortLinkSpeed_Type()
)
chSysStackPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortLinkSpeed.setStatus("current")
_ChSysStackPortRxDataRate_Type = Counter32
_ChSysStackPortRxDataRate_Object = MibTableColumn
chSysStackPortRxDataRate = _ChSysStackPortRxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 6),
    _ChSysStackPortRxDataRate_Type()
)
chSysStackPortRxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortRxDataRate.setStatus("current")
_ChSysStackPortRxErrorRate_Type = Counter32
_ChSysStackPortRxErrorRate_Object = MibTableColumn
chSysStackPortRxErrorRate = _ChSysStackPortRxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 7),
    _ChSysStackPortRxErrorRate_Type()
)
chSysStackPortRxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortRxErrorRate.setStatus("current")
_ChSysStackPortRxTotalErrors_Type = Counter32
_ChSysStackPortRxTotalErrors_Object = MibTableColumn
chSysStackPortRxTotalErrors = _ChSysStackPortRxTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 8),
    _ChSysStackPortRxTotalErrors_Type()
)
chSysStackPortRxTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortRxTotalErrors.setStatus("current")
_ChSysStackPortTxDataRate_Type = Counter32
_ChSysStackPortTxDataRate_Object = MibTableColumn
chSysStackPortTxDataRate = _ChSysStackPortTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 9),
    _ChSysStackPortTxDataRate_Type()
)
chSysStackPortTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortTxDataRate.setStatus("current")
_ChSysStackPortTxErrorRate_Type = Counter32
_ChSysStackPortTxErrorRate_Object = MibTableColumn
chSysStackPortTxErrorRate = _ChSysStackPortTxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 10),
    _ChSysStackPortTxErrorRate_Type()
)
chSysStackPortTxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortTxErrorRate.setStatus("current")
_ChSysStackPortTxTotalErrors_Type = Counter32
_ChSysStackPortTxTotalErrors_Object = MibTableColumn
chSysStackPortTxTotalErrors = _ChSysStackPortTxTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 5, 1, 11),
    _ChSysStackPortTxTotalErrors_Type()
)
chSysStackPortTxTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortTxTotalErrors.setStatus("current")
_ChSysProcessorTable_Object = MibTable
chSysProcessorTable = _ChSysProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 6)
)
if mibBuilder.loadTexts:
    chSysProcessorTable.setStatus("current")
_ChSysProcessorEntry_Object = MibTableRow
chSysProcessorEntry = _ChSysProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 6, 1)
)
chSysProcessorEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
)
if mibBuilder.loadTexts:
    chSysProcessorEntry.setStatus("current")
_ChSysProcessorModule_Type = F10ProcessorModuleType
_ChSysProcessorModule_Object = MibTableColumn
chSysProcessorModule = _ChSysProcessorModule_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 6, 1, 1),
    _ChSysProcessorModule_Type()
)
chSysProcessorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorModule.setStatus("current")
_ChSysProcessorUpTime_Type = TimeTicks
_ChSysProcessorUpTime_Object = MibTableColumn
chSysProcessorUpTime = _ChSysProcessorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 6, 1, 2),
    _ChSysProcessorUpTime_Type()
)
chSysProcessorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorUpTime.setStatus("current")
_ChSysProcessorNvramSize_Type = Integer32
_ChSysProcessorNvramSize_Object = MibTableColumn
chSysProcessorNvramSize = _ChSysProcessorNvramSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 6, 1, 3),
    _ChSysProcessorNvramSize_Type()
)
chSysProcessorNvramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorNvramSize.setStatus("current")
_ChSysProcessorMemSize_Type = Integer32
_ChSysProcessorMemSize_Object = MibTableColumn
chSysProcessorMemSize = _ChSysProcessorMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 6, 1, 4),
    _ChSysProcessorMemSize_Type()
)
chSysProcessorMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorMemSize.setStatus("current")
_ChSysSwModuleTable_Object = MibTable
chSysSwModuleTable = _ChSysSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7)
)
if mibBuilder.loadTexts:
    chSysSwModuleTable.setStatus("current")
_ChSysSwModuleEntry_Object = MibTableRow
chSysSwModuleEntry = _ChSysSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1)
)
chSysSwModuleEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
)
if mibBuilder.loadTexts:
    chSysSwModuleEntry.setStatus("current")
_ChSysSwRuntimeImgVersion_Type = DisplayString
_ChSysSwRuntimeImgVersion_Object = MibTableColumn
chSysSwRuntimeImgVersion = _ChSysSwRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 1),
    _ChSysSwRuntimeImgVersion_Type()
)
chSysSwRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgVersion.setStatus("current")
_ChSysSwRuntimeImgDate_Type = F10SwDate
_ChSysSwRuntimeImgDate_Object = MibTableColumn
chSysSwRuntimeImgDate = _ChSysSwRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 2),
    _ChSysSwRuntimeImgDate_Type()
)
chSysSwRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgDate.setStatus("current")
_ChSysSwCurrentBootImgVersion_Type = DisplayString
_ChSysSwCurrentBootImgVersion_Object = MibTableColumn
chSysSwCurrentBootImgVersion = _ChSysSwCurrentBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 3),
    _ChSysSwCurrentBootImgVersion_Type()
)
chSysSwCurrentBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgVersion.setStatus("current")
_ChSysSwCurrentBootImgDate_Type = DateAndTime
_ChSysSwCurrentBootImgDate_Object = MibTableColumn
chSysSwCurrentBootImgDate = _ChSysSwCurrentBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 4),
    _ChSysSwCurrentBootImgDate_Type()
)
chSysSwCurrentBootImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgDate.setStatus("current")


class _ChSysSwCurrentBootImgStatus_Type(Integer32):
    """Custom type chSysSwCurrentBootImgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2))
    )


_ChSysSwCurrentBootImgStatus_Type.__name__ = "Integer32"
_ChSysSwCurrentBootImgStatus_Object = MibTableColumn
chSysSwCurrentBootImgStatus = _ChSysSwCurrentBootImgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 5),
    _ChSysSwCurrentBootImgStatus_Type()
)
chSysSwCurrentBootImgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgStatus.setStatus("current")
_ChSysSwBackupBootImgVersion_Type = DisplayString
_ChSysSwBackupBootImgVersion_Object = MibTableColumn
chSysSwBackupBootImgVersion = _ChSysSwBackupBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 6),
    _ChSysSwBackupBootImgVersion_Type()
)
chSysSwBackupBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgVersion.setStatus("current")
_ChSysSwBackupBootImgDate_Type = DateAndTime
_ChSysSwBackupBootImgDate_Object = MibTableColumn
chSysSwBackupBootImgDate = _ChSysSwBackupBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 7),
    _ChSysSwBackupBootImgDate_Type()
)
chSysSwBackupBootImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgDate.setStatus("current")


class _ChSysSwBackupBootImgStatus_Type(Integer32):
    """Custom type chSysSwBackupBootImgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2))
    )


_ChSysSwBackupBootImgStatus_Type.__name__ = "Integer32"
_ChSysSwBackupBootImgStatus_Object = MibTableColumn
chSysSwBackupBootImgStatus = _ChSysSwBackupBootImgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 8),
    _ChSysSwBackupBootImgStatus_Type()
)
chSysSwBackupBootImgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgStatus.setStatus("current")


class _ChSysSwNextRebootImage_Type(Integer32):
    """Custom type chSysSwNextRebootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootImage-A", 1),
          ("bootImage-B", 2))
    )


_ChSysSwNextRebootImage_Type.__name__ = "Integer32"
_ChSysSwNextRebootImage_Object = MibTableColumn
chSysSwNextRebootImage = _ChSysSwNextRebootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 9),
    _ChSysSwNextRebootImage_Type()
)
chSysSwNextRebootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwNextRebootImage.setStatus("current")


class _ChSysSwCurrentBootImage_Type(Integer32):
    """Custom type chSysSwCurrentBootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootImage-A", 1),
          ("bootImage-B", 2))
    )


_ChSysSwCurrentBootImage_Type.__name__ = "Integer32"
_ChSysSwCurrentBootImage_Object = MibTableColumn
chSysSwCurrentBootImage = _ChSysSwCurrentBootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 10),
    _ChSysSwCurrentBootImage_Type()
)
chSysSwCurrentBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImage.setStatus("current")
_ChSysSwInPartitionAImgVers_Type = DisplayString
_ChSysSwInPartitionAImgVers_Object = MibTableColumn
chSysSwInPartitionAImgVers = _ChSysSwInPartitionAImgVers_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 11),
    _ChSysSwInPartitionAImgVers_Type()
)
chSysSwInPartitionAImgVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwInPartitionAImgVers.setStatus("current")
_ChSysSwInPartitionBImgVers_Type = DisplayString
_ChSysSwInPartitionBImgVers_Object = MibTableColumn
chSysSwInPartitionBImgVers = _ChSysSwInPartitionBImgVers_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 7, 1, 12),
    _ChSysSwInPartitionBImgVers_Type()
)
chSysSwInPartitionBImgVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwInPartitionBImgVers.setStatus("current")
_ChStackUnitUtilTable_Object = MibTable
chStackUnitUtilTable = _ChStackUnitUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8)
)
if mibBuilder.loadTexts:
    chStackUnitUtilTable.setStatus("current")
_ChStackUnitUtilEntry_Object = MibTableRow
chStackUnitUtilEntry = _ChStackUnitUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8, 1)
)
chStackUnitUtilEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
)
if mibBuilder.loadTexts:
    chStackUnitUtilEntry.setStatus("current")
_ChStackUnitCpuType_Type = F10ProcessorModuleType
_ChStackUnitCpuType_Object = MibTableColumn
chStackUnitCpuType = _ChStackUnitCpuType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8, 1, 1),
    _ChStackUnitCpuType_Type()
)
chStackUnitCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCpuType.setStatus("current")


class _ChStackUnitCpuUtil5Sec_Type(Gauge32):
    """Custom type chStackUnitCpuUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChStackUnitCpuUtil5Sec_Type.__name__ = "Gauge32"
_ChStackUnitCpuUtil5Sec_Object = MibTableColumn
chStackUnitCpuUtil5Sec = _ChStackUnitCpuUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8, 1, 2),
    _ChStackUnitCpuUtil5Sec_Type()
)
chStackUnitCpuUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCpuUtil5Sec.setStatus("current")
if mibBuilder.loadTexts:
    chStackUnitCpuUtil5Sec.setUnits("percent")


class _ChStackUnitCpuUtil1Min_Type(Gauge32):
    """Custom type chStackUnitCpuUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChStackUnitCpuUtil1Min_Type.__name__ = "Gauge32"
_ChStackUnitCpuUtil1Min_Object = MibTableColumn
chStackUnitCpuUtil1Min = _ChStackUnitCpuUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8, 1, 3),
    _ChStackUnitCpuUtil1Min_Type()
)
chStackUnitCpuUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCpuUtil1Min.setStatus("current")
if mibBuilder.loadTexts:
    chStackUnitCpuUtil1Min.setUnits("percent")


class _ChStackUnitCpuUtil5Min_Type(Gauge32):
    """Custom type chStackUnitCpuUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChStackUnitCpuUtil5Min_Type.__name__ = "Gauge32"
_ChStackUnitCpuUtil5Min_Object = MibTableColumn
chStackUnitCpuUtil5Min = _ChStackUnitCpuUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8, 1, 4),
    _ChStackUnitCpuUtil5Min_Type()
)
chStackUnitCpuUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCpuUtil5Min.setStatus("current")
if mibBuilder.loadTexts:
    chStackUnitCpuUtil5Min.setUnits("percent")


class _ChStackUnitMemUsageUtil_Type(Gauge32):
    """Custom type chStackUnitMemUsageUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChStackUnitMemUsageUtil_Type.__name__ = "Gauge32"
_ChStackUnitMemUsageUtil_Object = MibTableColumn
chStackUnitMemUsageUtil = _ChStackUnitMemUsageUtil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8, 1, 5),
    _ChStackUnitMemUsageUtil_Type()
)
chStackUnitMemUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitMemUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    chStackUnitMemUsageUtil.setUnits("percent")


class _ChStackUnitFlashUsageUtil_Type(Gauge32):
    """Custom type chStackUnitFlashUsageUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChStackUnitFlashUsageUtil_Type.__name__ = "Gauge32"
_ChStackUnitFlashUsageUtil_Object = MibTableColumn
chStackUnitFlashUsageUtil = _ChStackUnitFlashUsageUtil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 8, 1, 6),
    _ChStackUnitFlashUsageUtil_Type()
)
chStackUnitFlashUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitFlashUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    chStackUnitFlashUsageUtil.setUnits("percent")
_ChSysSwCoresTable_Object = MibTable
chSysSwCoresTable = _ChSysSwCoresTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 9)
)
if mibBuilder.loadTexts:
    chSysSwCoresTable.setStatus("current")
_ChSysCoresEntry_Object = MibTableRow
chSysCoresEntry = _ChSysCoresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 9, 1)
)
chSysCoresEntry.setIndexNames(
    (0, "F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-M-SERIES-CHASSIS-MIB", "chSysCoresInstance"),
)
if mibBuilder.loadTexts:
    chSysCoresEntry.setStatus("current")
_ChSysCoresInstance_Type = Integer32
_ChSysCoresInstance_Object = MibTableColumn
chSysCoresInstance = _ChSysCoresInstance_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 9, 1, 1),
    _ChSysCoresInstance_Type()
)
chSysCoresInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresInstance.setStatus("current")
_ChSysCoresFileName_Type = DisplayString
_ChSysCoresFileName_Object = MibTableColumn
chSysCoresFileName = _ChSysCoresFileName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 9, 1, 2),
    _ChSysCoresFileName_Type()
)
chSysCoresFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresFileName.setStatus("current")
_ChSysCoresTimeCreated_Type = F10SwDate
_ChSysCoresTimeCreated_Object = MibTableColumn
chSysCoresTimeCreated = _ChSysCoresTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 9, 1, 3),
    _ChSysCoresTimeCreated_Type()
)
chSysCoresTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresTimeCreated.setStatus("current")


class _ChSysCoresStackUnitNumber_Type(Integer32):
    """Custom type chSysCoresStackUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ChSysCoresStackUnitNumber_Type.__name__ = "Integer32"
_ChSysCoresStackUnitNumber_Object = MibTableColumn
chSysCoresStackUnitNumber = _ChSysCoresStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 9, 1, 4),
    _ChSysCoresStackUnitNumber_Type()
)
chSysCoresStackUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresStackUnitNumber.setStatus("current")
_ChSysCoresProcess_Type = DisplayString
_ChSysCoresProcess_Object = MibTableColumn
chSysCoresProcess = _ChSysCoresProcess_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 2, 9, 1, 5),
    _ChSysCoresProcess_Type()
)
chSysCoresProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresProcess.setStatus("current")
_ChAlarmObjects_ObjectIdentity = ObjectIdentity
chAlarmObjects = _ChAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4)
)
_ChAlarmMibNotifications_ObjectIdentity = ObjectIdentity
chAlarmMibNotifications = _ChAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0)
)
_F10mSeriesMibConformance_ObjectIdentity = ObjectIdentity
f10mSeriesMibConformance = _F10mSeriesMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 2)
)
_F10mSeriesMibCompliances_ObjectIdentity = ObjectIdentity
f10mSeriesMibCompliances = _F10mSeriesMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 2, 1)
)
_F10mSeriesMibGroups_ObjectIdentity = ObjectIdentity
f10mSeriesMibGroups = _F10mSeriesMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 2, 2)
)

# Managed Objects groups

f10mSeriesComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 2, 2, 1)
)
f10mSeriesComponentGroup.setObjects(
      *(("F10-M-SERIES-CHASSIS-MIB", "chNumStackUnits"),
        ("F10-M-SERIES-CHASSIS-MIB", "chNumMaxStackableUnits"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitIndexNext"))
)
if mibBuilder.loadTexts:
    f10mSeriesComponentGroup.setStatus("current")

f10mSeriesSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 2, 2, 2)
)
f10mSeriesSystemGroup.setObjects(
      *(("F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitSID"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitMgmtStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitHwMgmtPreference"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitAdmMgmtPreference"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitModelID"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitDescription"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitCodeVersion"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitCodeVersionInFlash"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitSerialNumber"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitUpTime"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitTemp"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitType"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitSysType"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitVendorId"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitMfgDate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitMacAddress"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitPartNum"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitProductRev"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitProductOrder"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitCountryCode"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitNum10GigEtherPorts"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumGigEtherPorts"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumFastEtherPorts"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumFanTrays"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumPowerSupplies"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitNumPluggableModules"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitRowStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitPiecePartID"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitPPIDRevision"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitServiceTag"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitExpressServiceCode"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPowerSupplyIndex"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPowerSupplyOperStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPowerSupplyType"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysFanTrayIndex"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysFanTrayOperStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortIndex"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortType"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortAdminStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortOperStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortIfIndex"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortXfpRecvPower"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortXfpRecvTemp"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysPortXfpTxPower"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortIndex"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortConfiguredMode"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortRunningMode"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortLinkStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortLinkSpeed"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortRxDataRate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortRxErrorRate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortRxTotalErrors"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortTxDataRate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortTxErrorRate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysStackPortTxTotalErrors"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysProcessorModule"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysProcessorUpTime"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysProcessorNvramSize"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysProcessorMemSize"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwRuntimeImgVersion"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwRuntimeImgDate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgVersion"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgDate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgVersion"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgDate"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgStatus"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwNextRebootImage"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImage"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwInPartitionAImgVers"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysSwInPartitionBImgVers"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitCpuType"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitCpuUtil5Sec"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitCpuUtil1Min"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitCpuUtil5Min"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitMemUsageUtil"),
        ("F10-M-SERIES-CHASSIS-MIB", "chStackUnitFlashUsageUtil"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysCoresInstance"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysCoresFileName"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysCoresTimeCreated"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysCoresStackUnitNumber"),
        ("F10-M-SERIES-CHASSIS-MIB", "chSysCoresProcess"))
)
if mibBuilder.loadTexts:
    f10mSeriesSystemGroup.setStatus("current")


# Notification objects

chAlarmStackUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 1)
)
chAlarmStackUnitDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmStackUnitDown.setStatus(
        "current"
    )

chAlarmStackUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 2)
)
chAlarmStackUnitUp.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmStackUnitUp.setStatus(
        "current"
    )

chAlarmStackUnitReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 3)
)
chAlarmStackUnitReset.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmStackUnitReset.setStatus(
        "current"
    )

chAlarmStackUnitOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 4)
)
chAlarmStackUnitOffline.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmStackUnitOffline.setStatus(
        "current"
    )

chAlarmStackUnitCodeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 5)
)
chAlarmStackUnitCodeMismatch.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmStackUnitCodeMismatch.setStatus(
        "current"
    )

chAlarmStackPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 6)
)
chAlarmStackPortLinkUp.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmStackPortLinkUp.setStatus(
        "current"
    )

chAlarmStackPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 7)
)
chAlarmStackPortLinkDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmStackPortLinkDown.setStatus(
        "current"
    )

chAlarmStackUnitRoleChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 1, 4, 0, 8)
)
chAlarmStackUnitRoleChanged.setObjects(
      *(("F10-M-SERIES-CHASSIS-MIB", "chStackUnitMgmtStatus"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"))
)
if mibBuilder.loadTexts:
    chAlarmStackUnitRoleChanged.setStatus(
        "current"
    )


# Notifications groups

f10mSeriesNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 2, 2, 3)
)
f10mSeriesNotificationGroup.setObjects(
      *(("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackUnitDown"),
        ("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackUnitUp"),
        ("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackUnitReset"),
        ("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackUnitOffline"),
        ("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackUnitCodeMismatch"),
        ("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackPortLinkUp"),
        ("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackPortLinkDown"),
        ("F10-M-SERIES-CHASSIS-MIB", "chAlarmStackUnitRoleChanged"))
)
if mibBuilder.loadTexts:
    f10mSeriesNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f10mSeriesMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 19, 2, 1, 1)
)
f10mSeriesMibCompliance.setObjects(
      *(("F10-M-SERIES-CHASSIS-MIB", "f10mSeriesComponentGroup"),
        ("F10-M-SERIES-CHASSIS-MIB", "f10mSeriesSystemGroup"),
        ("F10-M-SERIES-CHASSIS-MIB", "f10mSeriesNotificationGroup"))
)
if mibBuilder.loadTexts:
    f10mSeriesMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-M-SERIES-CHASSIS-MIB",
    **{"CodeType": CodeType,
       "UnitType": UnitType,
       "f10MSerChassisMib": f10MSerChassisMib,
       "f10MSerChassisObject": f10MSerChassisObject,
       "chObjects": chObjects,
       "chNumStackUnits": chNumStackUnits,
       "chNumMaxStackableUnits": chNumMaxStackableUnits,
       "chStackUnitIndexNext": chStackUnitIndexNext,
       "chSysObjects": chSysObjects,
       "chStackUnitTable": chStackUnitTable,
       "chStackUnitEntry": chStackUnitEntry,
       "chStackUnitIndex": chStackUnitIndex,
       "chStackUnitNumber": chStackUnitNumber,
       "chStackUnitSID": chStackUnitSID,
       "chStackUnitMgmtStatus": chStackUnitMgmtStatus,
       "chStackUnitHwMgmtPreference": chStackUnitHwMgmtPreference,
       "chStackUnitAdmMgmtPreference": chStackUnitAdmMgmtPreference,
       "chStackUnitModelID": chStackUnitModelID,
       "chStackUnitStatus": chStackUnitStatus,
       "chStackUnitDescription": chStackUnitDescription,
       "chStackUnitCodeVersion": chStackUnitCodeVersion,
       "chStackUnitCodeVersionInFlash": chStackUnitCodeVersionInFlash,
       "chStackUnitSerialNumber": chStackUnitSerialNumber,
       "chStackUnitUpTime": chStackUnitUpTime,
       "chStackUnitTemp": chStackUnitTemp,
       "chStackUnitType": chStackUnitType,
       "chStackUnitSysType": chStackUnitSysType,
       "chStackUnitVendorId": chStackUnitVendorId,
       "chStackUnitMfgDate": chStackUnitMfgDate,
       "chStackUnitMacAddress": chStackUnitMacAddress,
       "chStackUnitPartNum": chStackUnitPartNum,
       "chStackUnitProductRev": chStackUnitProductRev,
       "chStackUnitProductOrder": chStackUnitProductOrder,
       "chStackUnitCountryCode": chStackUnitCountryCode,
       "chStackUnitNum10GigEtherPorts": chStackUnitNum10GigEtherPorts,
       "chStackUnitNumGigEtherPorts": chStackUnitNumGigEtherPorts,
       "chStackUnitNumFastEtherPorts": chStackUnitNumFastEtherPorts,
       "chStackUnitNumFanTrays": chStackUnitNumFanTrays,
       "chStackUnitNumPowerSupplies": chStackUnitNumPowerSupplies,
       "chStackUnitNumPluggableModules": chStackUnitNumPluggableModules,
       "chStackUnitNum40GigEtherPorts": chStackUnitNum40GigEtherPorts,
       "chStackUnitRowStatus": chStackUnitRowStatus,
       "chStackUnitPiecePartID": chStackUnitPiecePartID,
       "chStackUnitPPIDRevision": chStackUnitPPIDRevision,
       "chStackUnitServiceTag": chStackUnitServiceTag,
       "chStackUnitExpressServiceCode": chStackUnitExpressServiceCode,
       "chSysPowerSupplyTable": chSysPowerSupplyTable,
       "chSysPowerSupplyEntry": chSysPowerSupplyEntry,
       "chSysPowerSupplyIndex": chSysPowerSupplyIndex,
       "chSysPowerSupplyOperStatus": chSysPowerSupplyOperStatus,
       "chSysPowerSupplyType": chSysPowerSupplyType,
       "chSysFanTrayTable": chSysFanTrayTable,
       "chSysFanTrayEntry": chSysFanTrayEntry,
       "chSysFanTrayIndex": chSysFanTrayIndex,
       "chSysFanTrayOperStatus": chSysFanTrayOperStatus,
       "chSysPortTable": chSysPortTable,
       "chSysPortEntry": chSysPortEntry,
       "chSysPortIndex": chSysPortIndex,
       "chSysPortType": chSysPortType,
       "chSysPortAdminStatus": chSysPortAdminStatus,
       "chSysPortOperStatus": chSysPortOperStatus,
       "chSysPortIfIndex": chSysPortIfIndex,
       "chSysPortXfpRecvPower": chSysPortXfpRecvPower,
       "chSysPortXfpRecvTemp": chSysPortXfpRecvTemp,
       "chSysPortXfpTxPower": chSysPortXfpTxPower,
       "chSysStackPortTable": chSysStackPortTable,
       "chSysStackPortEntry": chSysStackPortEntry,
       "chSysStackPortIndex": chSysStackPortIndex,
       "chSysStackPortConfiguredMode": chSysStackPortConfiguredMode,
       "chSysStackPortRunningMode": chSysStackPortRunningMode,
       "chSysStackPortLinkStatus": chSysStackPortLinkStatus,
       "chSysStackPortLinkSpeed": chSysStackPortLinkSpeed,
       "chSysStackPortRxDataRate": chSysStackPortRxDataRate,
       "chSysStackPortRxErrorRate": chSysStackPortRxErrorRate,
       "chSysStackPortRxTotalErrors": chSysStackPortRxTotalErrors,
       "chSysStackPortTxDataRate": chSysStackPortTxDataRate,
       "chSysStackPortTxErrorRate": chSysStackPortTxErrorRate,
       "chSysStackPortTxTotalErrors": chSysStackPortTxTotalErrors,
       "chSysProcessorTable": chSysProcessorTable,
       "chSysProcessorEntry": chSysProcessorEntry,
       "chSysProcessorModule": chSysProcessorModule,
       "chSysProcessorUpTime": chSysProcessorUpTime,
       "chSysProcessorNvramSize": chSysProcessorNvramSize,
       "chSysProcessorMemSize": chSysProcessorMemSize,
       "chSysSwModuleTable": chSysSwModuleTable,
       "chSysSwModuleEntry": chSysSwModuleEntry,
       "chSysSwRuntimeImgVersion": chSysSwRuntimeImgVersion,
       "chSysSwRuntimeImgDate": chSysSwRuntimeImgDate,
       "chSysSwCurrentBootImgVersion": chSysSwCurrentBootImgVersion,
       "chSysSwCurrentBootImgDate": chSysSwCurrentBootImgDate,
       "chSysSwCurrentBootImgStatus": chSysSwCurrentBootImgStatus,
       "chSysSwBackupBootImgVersion": chSysSwBackupBootImgVersion,
       "chSysSwBackupBootImgDate": chSysSwBackupBootImgDate,
       "chSysSwBackupBootImgStatus": chSysSwBackupBootImgStatus,
       "chSysSwNextRebootImage": chSysSwNextRebootImage,
       "chSysSwCurrentBootImage": chSysSwCurrentBootImage,
       "chSysSwInPartitionAImgVers": chSysSwInPartitionAImgVers,
       "chSysSwInPartitionBImgVers": chSysSwInPartitionBImgVers,
       "chStackUnitUtilTable": chStackUnitUtilTable,
       "chStackUnitUtilEntry": chStackUnitUtilEntry,
       "chStackUnitCpuType": chStackUnitCpuType,
       "chStackUnitCpuUtil5Sec": chStackUnitCpuUtil5Sec,
       "chStackUnitCpuUtil1Min": chStackUnitCpuUtil1Min,
       "chStackUnitCpuUtil5Min": chStackUnitCpuUtil5Min,
       "chStackUnitMemUsageUtil": chStackUnitMemUsageUtil,
       "chStackUnitFlashUsageUtil": chStackUnitFlashUsageUtil,
       "chSysSwCoresTable": chSysSwCoresTable,
       "chSysCoresEntry": chSysCoresEntry,
       "chSysCoresInstance": chSysCoresInstance,
       "chSysCoresFileName": chSysCoresFileName,
       "chSysCoresTimeCreated": chSysCoresTimeCreated,
       "chSysCoresStackUnitNumber": chSysCoresStackUnitNumber,
       "chSysCoresProcess": chSysCoresProcess,
       "chAlarmObjects": chAlarmObjects,
       "chAlarmMibNotifications": chAlarmMibNotifications,
       "chAlarmStackUnitDown": chAlarmStackUnitDown,
       "chAlarmStackUnitUp": chAlarmStackUnitUp,
       "chAlarmStackUnitReset": chAlarmStackUnitReset,
       "chAlarmStackUnitOffline": chAlarmStackUnitOffline,
       "chAlarmStackUnitCodeMismatch": chAlarmStackUnitCodeMismatch,
       "chAlarmStackPortLinkUp": chAlarmStackPortLinkUp,
       "chAlarmStackPortLinkDown": chAlarmStackPortLinkDown,
       "chAlarmStackUnitRoleChanged": chAlarmStackUnitRoleChanged,
       "f10mSeriesMibConformance": f10mSeriesMibConformance,
       "f10mSeriesMibCompliances": f10mSeriesMibCompliances,
       "f10mSeriesMibCompliance": f10mSeriesMibCompliance,
       "f10mSeriesMibGroups": f10mSeriesMibGroups,
       "f10mSeriesComponentGroup": f10mSeriesComponentGroup,
       "f10mSeriesSystemGroup": f10mSeriesSystemGroup,
       "f10mSeriesNotificationGroup": f10mSeriesNotificationGroup}
)
