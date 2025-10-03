# SNMP MIB module (F10-S-SERIES-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\F10-S-SERIES-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:07 2025
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
 F10MfgDate,
 F10ProcessorModuleType,
 F10SSeriesPortType,
 F10SwDate) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "F10ChassisType",
    "F10HundredthdB",
    "F10MfgDate",
    "F10ProcessorModuleType",
    "F10SSeriesPortType",
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

f10SSerChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10)
)
if mibBuilder.loadTexts:
    f10SSerChassisMib.setRevisions(
        ("2007-10-03 12:00",)
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

_F10SSerChassisObject_ObjectIdentity = ObjectIdentity
f10SSerChassisObject = _F10SSerChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1)
)
_ChObjects_ObjectIdentity = ObjectIdentity
chObjects = _ChObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 1)
)
_ChNumStackUnits_Type = Integer32
_ChNumStackUnits_Object = MibScalar
chNumStackUnits = _ChNumStackUnits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 1, 1),
    _ChNumStackUnits_Type()
)
chNumStackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumStackUnits.setStatus("current")
_ChNumMaxStackableUnits_Type = Integer32
_ChNumMaxStackableUnits_Object = MibScalar
chNumMaxStackableUnits = _ChNumMaxStackableUnits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 1, 2),
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
        ValueRangeConstraint(1, 8),
    )


_ChStackUnitIndexNext_Type.__name__ = "Integer32"
_ChStackUnitIndexNext_Object = MibScalar
chStackUnitIndexNext = _ChStackUnitIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 1, 3),
    _ChStackUnitIndexNext_Type()
)
chStackUnitIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitIndexNext.setStatus("current")
_ChSysObjects_ObjectIdentity = ObjectIdentity
chSysObjects = _ChSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2)
)
_ChSwitchTypeTable_Object = MibTable
chSwitchTypeTable = _ChSwitchTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chSwitchTypeTable.setStatus("deprecated")
_ChSwitchTypeEntry_Object = MibTableRow
chSwitchTypeEntry = _ChSwitchTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 1, 1)
)
chSwitchTypeEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chSwitchTypeSID"),
)
if mibBuilder.loadTexts:
    chSwitchTypeEntry.setStatus("deprecated")
_ChSwitchTypeSID_Type = Integer32
_ChSwitchTypeSID_Object = MibTableColumn
chSwitchTypeSID = _ChSwitchTypeSID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 1, 1, 1),
    _ChSwitchTypeSID_Type()
)
chSwitchTypeSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSwitchTypeSID.setStatus("deprecated")
_ChSwitchTypeModelID_Type = DisplayString
_ChSwitchTypeModelID_Object = MibTableColumn
chSwitchTypeModelID = _ChSwitchTypeModelID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 1, 1, 2),
    _ChSwitchTypeModelID_Type()
)
chSwitchTypeModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSwitchTypeModelID.setStatus("deprecated")
_ChSwitchTypeCodeType_Type = CodeType
_ChSwitchTypeCodeType_Object = MibTableColumn
chSwitchTypeCodeType = _ChSwitchTypeCodeType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 1, 1, 3),
    _ChSwitchTypeCodeType_Type()
)
chSwitchTypeCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSwitchTypeCodeType.setStatus("deprecated")


class _ChSwitchTypeMgmtPreference_Type(Integer32):
    """Custom type chSwitchTypeMgmtPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_ChSwitchTypeMgmtPreference_Type.__name__ = "Integer32"
_ChSwitchTypeMgmtPreference_Object = MibTableColumn
chSwitchTypeMgmtPreference = _ChSwitchTypeMgmtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 1, 1, 4),
    _ChSwitchTypeMgmtPreference_Type()
)
chSwitchTypeMgmtPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSwitchTypeMgmtPreference.setStatus("deprecated")
_ChStackUnitTable_Object = MibTable
chStackUnitTable = _ChStackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    chStackUnitTable.setStatus("current")
_ChStackUnitEntry_Object = MibTableRow
chStackUnitEntry = _ChStackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1)
)
chStackUnitEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitIndex"),
)
if mibBuilder.loadTexts:
    chStackUnitEntry.setStatus("current")
_ChStackUnitIndex_Type = Integer32
_ChStackUnitIndex_Object = MibTableColumn
chStackUnitIndex = _ChStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 1),
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
        ValueRangeConstraint(1, 8),
    )


_ChStackUnitNumber_Type.__name__ = "Integer32"
_ChStackUnitNumber_Object = MibTableColumn
chStackUnitNumber = _ChStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 2),
    _ChStackUnitNumber_Type()
)
chStackUnitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitNumber.setStatus("current")
_ChStackUnitSID_Type = Integer32
_ChStackUnitSID_Object = MibTableColumn
chStackUnitSID = _ChStackUnitSID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 6),
    _ChStackUnitAdmMgmtPreference_Type()
)
chStackUnitAdmMgmtPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitAdmMgmtPreference.setStatus("current")
_ChStackUnitModelID_Type = DisplayString
_ChStackUnitModelID_Object = MibTableColumn
chStackUnitModelID = _ChStackUnitModelID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 8),
    _ChStackUnitStatus_Type()
)
chStackUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitStatus.setStatus("current")
_ChStackUnitDescription_Type = DisplayString
_ChStackUnitDescription_Object = MibTableColumn
chStackUnitDescription = _ChStackUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 9),
    _ChStackUnitDescription_Type()
)
chStackUnitDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitDescription.setStatus("current")
_ChStackUnitCodeVersion_Type = DisplayString
_ChStackUnitCodeVersion_Object = MibTableColumn
chStackUnitCodeVersion = _ChStackUnitCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 10),
    _ChStackUnitCodeVersion_Type()
)
chStackUnitCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCodeVersion.setStatus("current")
_ChStackUnitCodeVersionInFlash_Type = DisplayString
_ChStackUnitCodeVersionInFlash_Object = MibTableColumn
chStackUnitCodeVersionInFlash = _ChStackUnitCodeVersionInFlash_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 11),
    _ChStackUnitCodeVersionInFlash_Type()
)
chStackUnitCodeVersionInFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCodeVersionInFlash.setStatus("current")
_ChStackUnitSerialNumber_Type = DisplayString
_ChStackUnitSerialNumber_Object = MibTableColumn
chStackUnitSerialNumber = _ChStackUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 12),
    _ChStackUnitSerialNumber_Type()
)
chStackUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitSerialNumber.setStatus("current")
_ChStackUnitUpTime_Type = TimeTicks
_ChStackUnitUpTime_Object = MibTableColumn
chStackUnitUpTime = _ChStackUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 13),
    _ChStackUnitUpTime_Type()
)
chStackUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitUpTime.setStatus("current")
_ChStackUnitTemp_Type = Gauge32
_ChStackUnitTemp_Object = MibTableColumn
chStackUnitTemp = _ChStackUnitTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 14),
    _ChStackUnitTemp_Type()
)
chStackUnitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitTemp.setStatus("current")
_ChStackUnitType_Type = UnitType
_ChStackUnitType_Object = MibTableColumn
chStackUnitType = _ChStackUnitType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 15),
    _ChStackUnitType_Type()
)
chStackUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitType.setStatus("current")
_ChStackUnitSysType_Type = F10ChassisType
_ChStackUnitSysType_Object = MibTableColumn
chStackUnitSysType = _ChStackUnitSysType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 16),
    _ChStackUnitSysType_Type()
)
chStackUnitSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitSysType.setStatus("current")
_ChStackUnitVendorId_Type = DisplayString
_ChStackUnitVendorId_Object = MibTableColumn
chStackUnitVendorId = _ChStackUnitVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 17),
    _ChStackUnitVendorId_Type()
)
chStackUnitVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitVendorId.setStatus("current")
_ChStackUnitMfgDate_Type = F10MfgDate
_ChStackUnitMfgDate_Object = MibTableColumn
chStackUnitMfgDate = _ChStackUnitMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 18),
    _ChStackUnitMfgDate_Type()
)
chStackUnitMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitMfgDate.setStatus("current")
_ChStackUnitMacAddress_Type = MacAddress
_ChStackUnitMacAddress_Object = MibTableColumn
chStackUnitMacAddress = _ChStackUnitMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 19),
    _ChStackUnitMacAddress_Type()
)
chStackUnitMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitMacAddress.setStatus("current")
_ChStackUnitPartNum_Type = DisplayString
_ChStackUnitPartNum_Object = MibTableColumn
chStackUnitPartNum = _ChStackUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 20),
    _ChStackUnitPartNum_Type()
)
chStackUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitPartNum.setStatus("current")
_ChStackUnitProductRev_Type = DisplayString
_ChStackUnitProductRev_Object = MibTableColumn
chStackUnitProductRev = _ChStackUnitProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 21),
    _ChStackUnitProductRev_Type()
)
chStackUnitProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitProductRev.setStatus("current")
_ChStackUnitProductOrder_Type = DisplayString
_ChStackUnitProductOrder_Object = MibTableColumn
chStackUnitProductOrder = _ChStackUnitProductOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 23),
    _ChStackUnitCountryCode_Type()
)
chStackUnitCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitCountryCode.setStatus("current")
_ChStackUnitNum10GigEtherPorts_Type = Integer32
_ChStackUnitNum10GigEtherPorts_Object = MibTableColumn
chStackUnitNum10GigEtherPorts = _ChStackUnitNum10GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 24),
    _ChStackUnitNum10GigEtherPorts_Type()
)
chStackUnitNum10GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNum10GigEtherPorts.setStatus("current")
_ChStackUnitNumGigEtherPorts_Type = Integer32
_ChStackUnitNumGigEtherPorts_Object = MibTableColumn
chStackUnitNumGigEtherPorts = _ChStackUnitNumGigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 25),
    _ChStackUnitNumGigEtherPorts_Type()
)
chStackUnitNumGigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumGigEtherPorts.setStatus("current")
_ChStackUnitNumFastEtherPorts_Type = Integer32
_ChStackUnitNumFastEtherPorts_Object = MibTableColumn
chStackUnitNumFastEtherPorts = _ChStackUnitNumFastEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 26),
    _ChStackUnitNumFastEtherPorts_Type()
)
chStackUnitNumFastEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumFastEtherPorts.setStatus("current")
_ChStackUnitNumFanTrays_Type = Integer32
_ChStackUnitNumFanTrays_Object = MibTableColumn
chStackUnitNumFanTrays = _ChStackUnitNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 27),
    _ChStackUnitNumFanTrays_Type()
)
chStackUnitNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumFanTrays.setStatus("current")
_ChStackUnitNumPowerSupplies_Type = Integer32
_ChStackUnitNumPowerSupplies_Object = MibTableColumn
chStackUnitNumPowerSupplies = _ChStackUnitNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 28),
    _ChStackUnitNumPowerSupplies_Type()
)
chStackUnitNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumPowerSupplies.setStatus("current")
_ChStackUnitNumPluggableModules_Type = Integer32
_ChStackUnitNumPluggableModules_Object = MibTableColumn
chStackUnitNumPluggableModules = _ChStackUnitNumPluggableModules_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 29),
    _ChStackUnitNumPluggableModules_Type()
)
chStackUnitNumPluggableModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitNumPluggableModules.setStatus("current")
_ChStackUnitRowStatus_Type = RowStatus
_ChStackUnitRowStatus_Object = MibTableColumn
chStackUnitRowStatus = _ChStackUnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 2, 1, 30),
    _ChStackUnitRowStatus_Type()
)
chStackUnitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chStackUnitRowStatus.setStatus("current")
_ChSysPowerSupplyTable_Object = MibTable
chSysPowerSupplyTable = _ChSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    chSysPowerSupplyTable.setStatus("current")
_ChSysPowerSupplyEntry_Object = MibTableRow
chSysPowerSupplyEntry = _ChSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 3, 1)
)
chSysPowerSupplyEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-S-SERIES-CHASSIS-MIB", "chSysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    chSysPowerSupplyEntry.setStatus("current")
_ChSysPowerSupplyIndex_Type = Integer32
_ChSysPowerSupplyIndex_Object = MibTableColumn
chSysPowerSupplyIndex = _ChSysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 3, 1, 1),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ChSysPowerSupplyOperStatus_Type.__name__ = "Integer32"
_ChSysPowerSupplyOperStatus_Object = MibTableColumn
chSysPowerSupplyOperStatus = _ChSysPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 3, 1, 2),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_ChSysPowerSupplyType_Type.__name__ = "Integer32"
_ChSysPowerSupplyType_Object = MibTableColumn
chSysPowerSupplyType = _ChSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 3, 1, 3),
    _ChSysPowerSupplyType_Type()
)
chSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyType.setStatus("current")
_ChSysFanTrayTable_Object = MibTable
chSysFanTrayTable = _ChSysFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 4)
)
if mibBuilder.loadTexts:
    chSysFanTrayTable.setStatus("current")
_ChSysFanTrayEntry_Object = MibTableRow
chSysFanTrayEntry = _ChSysFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 4, 1)
)
chSysFanTrayEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-S-SERIES-CHASSIS-MIB", "chSysFanTrayIndex"),
)
if mibBuilder.loadTexts:
    chSysFanTrayEntry.setStatus("current")
_ChSysFanTrayIndex_Type = Integer32
_ChSysFanTrayIndex_Object = MibTableColumn
chSysFanTrayIndex = _ChSysFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 4, 1, 2),
    _ChSysFanTrayOperStatus_Type()
)
chSysFanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayOperStatus.setStatus("current")
_ChSysPortTable_Object = MibTable
chSysPortTable = _ChSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5)
)
if mibBuilder.loadTexts:
    chSysPortTable.setStatus("current")
_ChSysPortEntry_Object = MibTableRow
chSysPortEntry = _ChSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5, 1)
)
chSysPortEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-S-SERIES-CHASSIS-MIB", "chSysPortIndex"),
)
if mibBuilder.loadTexts:
    chSysPortEntry.setStatus("current")
_ChSysPortIndex_Type = Integer32
_ChSysPortIndex_Object = MibTableColumn
chSysPortIndex = _ChSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5, 1, 1),
    _ChSysPortIndex_Type()
)
chSysPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIndex.setStatus("current")
_ChSysPortType_Type = F10SSeriesPortType
_ChSysPortType_Object = MibTableColumn
chSysPortType = _ChSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5, 1, 4),
    _ChSysPortOperStatus_Type()
)
chSysPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortOperStatus.setStatus("current")
_ChSysPortIfIndex_Type = Integer32
_ChSysPortIfIndex_Object = MibTableColumn
chSysPortIfIndex = _ChSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5, 1, 5),
    _ChSysPortIfIndex_Type()
)
chSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIfIndex.setStatus("current")
_ChSysPortXfpRecvPower_Type = F10HundredthdB
_ChSysPortXfpRecvPower_Object = MibTableColumn
chSysPortXfpRecvPower = _ChSysPortXfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 5, 1, 6),
    _ChSysPortXfpRecvPower_Type()
)
chSysPortXfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortXfpRecvPower.setStatus("current")
if mibBuilder.loadTexts:
    chSysPortXfpRecvPower.setUnits("dB")
_ChSysStackPortTable_Object = MibTable
chSysStackPortTable = _ChSysStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6)
)
if mibBuilder.loadTexts:
    chSysStackPortTable.setStatus("current")
_ChSysStackPortEntry_Object = MibTableRow
chSysStackPortEntry = _ChSysStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1)
)
chSysStackPortEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
    (0, "F10-S-SERIES-CHASSIS-MIB", "chSysStackPortIndex"),
)
if mibBuilder.loadTexts:
    chSysStackPortEntry.setStatus("current")
_ChSysStackPortIndex_Type = Integer32
_ChSysStackPortIndex_Object = MibTableColumn
chSysStackPortIndex = _ChSysStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 4),
    _ChSysStackPortLinkStatus_Type()
)
chSysStackPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortLinkStatus.setStatus("current")
_ChSysStackPortLinkSpeed_Type = Gauge32
_ChSysStackPortLinkSpeed_Object = MibTableColumn
chSysStackPortLinkSpeed = _ChSysStackPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 5),
    _ChSysStackPortLinkSpeed_Type()
)
chSysStackPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortLinkSpeed.setStatus("current")
_ChSysStackPortRxDataRate_Type = Counter32
_ChSysStackPortRxDataRate_Object = MibTableColumn
chSysStackPortRxDataRate = _ChSysStackPortRxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 6),
    _ChSysStackPortRxDataRate_Type()
)
chSysStackPortRxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortRxDataRate.setStatus("current")
_ChSysStackPortRxErrorRate_Type = Counter32
_ChSysStackPortRxErrorRate_Object = MibTableColumn
chSysStackPortRxErrorRate = _ChSysStackPortRxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 7),
    _ChSysStackPortRxErrorRate_Type()
)
chSysStackPortRxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortRxErrorRate.setStatus("current")
_ChSysStackPortRxTotalErrors_Type = Counter32
_ChSysStackPortRxTotalErrors_Object = MibTableColumn
chSysStackPortRxTotalErrors = _ChSysStackPortRxTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 8),
    _ChSysStackPortRxTotalErrors_Type()
)
chSysStackPortRxTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortRxTotalErrors.setStatus("current")
_ChSysStackPortTxDataRate_Type = Counter32
_ChSysStackPortTxDataRate_Object = MibTableColumn
chSysStackPortTxDataRate = _ChSysStackPortTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 9),
    _ChSysStackPortTxDataRate_Type()
)
chSysStackPortTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortTxDataRate.setStatus("current")
_ChSysStackPortTxErrorRate_Type = Counter32
_ChSysStackPortTxErrorRate_Object = MibTableColumn
chSysStackPortTxErrorRate = _ChSysStackPortTxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 10),
    _ChSysStackPortTxErrorRate_Type()
)
chSysStackPortTxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortTxErrorRate.setStatus("current")
_ChSysStackPortTxTotalErrors_Type = Counter32
_ChSysStackPortTxTotalErrors_Object = MibTableColumn
chSysStackPortTxTotalErrors = _ChSysStackPortTxTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 6, 1, 11),
    _ChSysStackPortTxTotalErrors_Type()
)
chSysStackPortTxTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysStackPortTxTotalErrors.setStatus("current")
_ChSysProcessorTable_Object = MibTable
chSysProcessorTable = _ChSysProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 7)
)
if mibBuilder.loadTexts:
    chSysProcessorTable.setStatus("current")
_ChSysProcessorEntry_Object = MibTableRow
chSysProcessorEntry = _ChSysProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 7, 1)
)
chSysProcessorEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
)
if mibBuilder.loadTexts:
    chSysProcessorEntry.setStatus("current")
_ChSysProcessorModule_Type = F10ProcessorModuleType
_ChSysProcessorModule_Object = MibTableColumn
chSysProcessorModule = _ChSysProcessorModule_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 7, 1, 1),
    _ChSysProcessorModule_Type()
)
chSysProcessorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorModule.setStatus("current")
_ChSysProcessorUpTime_Type = TimeTicks
_ChSysProcessorUpTime_Object = MibTableColumn
chSysProcessorUpTime = _ChSysProcessorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 7, 1, 2),
    _ChSysProcessorUpTime_Type()
)
chSysProcessorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorUpTime.setStatus("current")
_ChSysProcessorNvramSize_Type = Integer32
_ChSysProcessorNvramSize_Object = MibTableColumn
chSysProcessorNvramSize = _ChSysProcessorNvramSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 7, 1, 3),
    _ChSysProcessorNvramSize_Type()
)
chSysProcessorNvramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorNvramSize.setStatus("current")
_ChSysProcessorMemSize_Type = Integer32
_ChSysProcessorMemSize_Object = MibTableColumn
chSysProcessorMemSize = _ChSysProcessorMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 7, 1, 4),
    _ChSysProcessorMemSize_Type()
)
chSysProcessorMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorMemSize.setStatus("current")
_ChSysSwModuleTable_Object = MibTable
chSysSwModuleTable = _ChSysSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8)
)
if mibBuilder.loadTexts:
    chSysSwModuleTable.setStatus("current")
_ChSysSwModuleEntry_Object = MibTableRow
chSysSwModuleEntry = _ChSysSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1)
)
chSysSwModuleEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
)
if mibBuilder.loadTexts:
    chSysSwModuleEntry.setStatus("current")
_ChSysSwRuntimeImgVersion_Type = DisplayString
_ChSysSwRuntimeImgVersion_Object = MibTableColumn
chSysSwRuntimeImgVersion = _ChSysSwRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 1),
    _ChSysSwRuntimeImgVersion_Type()
)
chSysSwRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgVersion.setStatus("current")
_ChSysSwRuntimeImgDate_Type = F10SwDate
_ChSysSwRuntimeImgDate_Object = MibTableColumn
chSysSwRuntimeImgDate = _ChSysSwRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 2),
    _ChSysSwRuntimeImgDate_Type()
)
chSysSwRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgDate.setStatus("current")
_ChSysSwCurrentBootImgVersion_Type = DisplayString
_ChSysSwCurrentBootImgVersion_Object = MibTableColumn
chSysSwCurrentBootImgVersion = _ChSysSwCurrentBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 3),
    _ChSysSwCurrentBootImgVersion_Type()
)
chSysSwCurrentBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgVersion.setStatus("current")
_ChSysSwCurrentBootImgDate_Type = DateAndTime
_ChSysSwCurrentBootImgDate_Object = MibTableColumn
chSysSwCurrentBootImgDate = _ChSysSwCurrentBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 5),
    _ChSysSwCurrentBootImgStatus_Type()
)
chSysSwCurrentBootImgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgStatus.setStatus("current")
_ChSysSwBackupBootImgVersion_Type = DisplayString
_ChSysSwBackupBootImgVersion_Object = MibTableColumn
chSysSwBackupBootImgVersion = _ChSysSwBackupBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 6),
    _ChSysSwBackupBootImgVersion_Type()
)
chSysSwBackupBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgVersion.setStatus("current")
_ChSysSwBackupBootImgDate_Type = DateAndTime
_ChSysSwBackupBootImgDate_Object = MibTableColumn
chSysSwBackupBootImgDate = _ChSysSwBackupBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 8, 1, 10),
    _ChSysSwCurrentBootImage_Type()
)
chSysSwCurrentBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImage.setStatus("current")
_ChStackUnitUtilTable_Object = MibTable
chStackUnitUtilTable = _ChStackUnitUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 9)
)
if mibBuilder.loadTexts:
    chStackUnitUtilTable.setStatus("current")
_ChStackUnitUtilEntry_Object = MibTableRow
chStackUnitUtilEntry = _ChStackUnitUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 9, 1)
)
chStackUnitUtilEntry.setIndexNames(
    (0, "F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
)
if mibBuilder.loadTexts:
    chStackUnitUtilEntry.setStatus("current")
_ChStackUnitCpuType_Type = F10ProcessorModuleType
_ChStackUnitCpuType_Object = MibTableColumn
chStackUnitCpuType = _ChStackUnitCpuType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 9, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 9, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 9, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 2, 9, 1, 5),
    _ChStackUnitMemUsageUtil_Type()
)
chStackUnitMemUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStackUnitMemUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    chStackUnitMemUsageUtil.setUnits("percent")
_ChAlarmObjects_ObjectIdentity = ObjectIdentity
chAlarmObjects = _ChAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4)
)
_ChAlarmMibNotifications_ObjectIdentity = ObjectIdentity
chAlarmMibNotifications = _ChAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0)
)
_F10sSeriesMibConformance_ObjectIdentity = ObjectIdentity
f10sSeriesMibConformance = _F10sSeriesMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 2)
)
_F10sSeriesMibCompliances_ObjectIdentity = ObjectIdentity
f10sSeriesMibCompliances = _F10sSeriesMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 2, 1)
)
_F10sSeriesMibGroups_ObjectIdentity = ObjectIdentity
f10sSeriesMibGroups = _F10sSeriesMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 2, 2)
)

# Managed Objects groups

f10sSeriesComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 2, 2, 1)
)
f10sSeriesComponentGroup.setObjects(
      *(("F10-S-SERIES-CHASSIS-MIB", "chNumStackUnits"),
        ("F10-S-SERIES-CHASSIS-MIB", "chNumMaxStackableUnits"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitIndexNext"))
)
if mibBuilder.loadTexts:
    f10sSeriesComponentGroup.setStatus("current")

f10sSeriesSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 2, 2, 2)
)
f10sSeriesSystemGroup.setObjects(
      *(("F10-S-SERIES-CHASSIS-MIB", "chSwitchTypeSID"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSwitchTypeModelID"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSwitchTypeCodeType"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSwitchTypeMgmtPreference"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumber"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitSID"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitMgmtStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitHwMgmtPreference"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitAdmMgmtPreference"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitModelID"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitDescription"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitCodeVersion"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitCodeVersionInFlash"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitSerialNumber"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitUpTime"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitTemp"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitType"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitSysType"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitVendorId"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitMfgDate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitMacAddress"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitPartNum"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitProductRev"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitProductOrder"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitCountryCode"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitNum10GigEtherPorts"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumGigEtherPorts"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumFastEtherPorts"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumFanTrays"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumPowerSupplies"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitNumPluggableModules"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitRowStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPowerSupplyIndex"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPowerSupplyOperStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPowerSupplyType"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysFanTrayIndex"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysFanTrayOperStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPortIndex"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPortType"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPortAdminStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPortOperStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPortIfIndex"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysPortXfpRecvPower"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortIndex"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortConfiguredMode"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortRunningMode"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortLinkStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortLinkSpeed"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortRxDataRate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortRxErrorRate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortRxTotalErrors"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortTxDataRate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortTxErrorRate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysStackPortTxTotalErrors"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysProcessorModule"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysProcessorUpTime"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysProcessorNvramSize"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysProcessorMemSize"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwRuntimeImgVersion"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwRuntimeImgDate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgVersion"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgDate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgVersion"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgDate"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgStatus"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwNextRebootImage"),
        ("F10-S-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImage"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitCpuType"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitCpuUtil5Sec"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitCpuUtil1Min"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitCpuUtil5Min"),
        ("F10-S-SERIES-CHASSIS-MIB", "chStackUnitMemUsageUtil"))
)
if mibBuilder.loadTexts:
    f10sSeriesSystemGroup.setStatus("current")


# Notification objects

chAlarmStackUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0, 1)
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0, 2)
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0, 3)
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0, 4)
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0, 5)
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0, 6)
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 1, 4, 0, 7)
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


# Notifications groups

f10sSeriesNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 2, 2, 3)
)
f10sSeriesNotificationGroup.setObjects(
      *(("F10-S-SERIES-CHASSIS-MIB", "chAlarmStackUnitDown"),
        ("F10-S-SERIES-CHASSIS-MIB", "chAlarmStackUnitUp"),
        ("F10-S-SERIES-CHASSIS-MIB", "chAlarmStackUnitReset"),
        ("F10-S-SERIES-CHASSIS-MIB", "chAlarmStackUnitOffline"),
        ("F10-S-SERIES-CHASSIS-MIB", "chAlarmStackUnitCodeMismatch"),
        ("F10-S-SERIES-CHASSIS-MIB", "chAlarmStackPortLinkUp"),
        ("F10-S-SERIES-CHASSIS-MIB", "chAlarmStackPortLinkDown"))
)
if mibBuilder.loadTexts:
    f10sSeriesNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f10sSeriesMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 10, 2, 1, 1)
)
f10sSeriesMibCompliance.setObjects(
      *(("F10-S-SERIES-CHASSIS-MIB", "f10sSeriesComponentGroup"),
        ("F10-S-SERIES-CHASSIS-MIB", "f10sSeriesSystemGroup"),
        ("F10-S-SERIES-CHASSIS-MIB", "f10sSeriesNotificationGroup"))
)
if mibBuilder.loadTexts:
    f10sSeriesMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-S-SERIES-CHASSIS-MIB",
    **{"CodeType": CodeType,
       "UnitType": UnitType,
       "f10SSerChassisMib": f10SSerChassisMib,
       "f10SSerChassisObject": f10SSerChassisObject,
       "chObjects": chObjects,
       "chNumStackUnits": chNumStackUnits,
       "chNumMaxStackableUnits": chNumMaxStackableUnits,
       "chStackUnitIndexNext": chStackUnitIndexNext,
       "chSysObjects": chSysObjects,
       "chSwitchTypeTable": chSwitchTypeTable,
       "chSwitchTypeEntry": chSwitchTypeEntry,
       "chSwitchTypeSID": chSwitchTypeSID,
       "chSwitchTypeModelID": chSwitchTypeModelID,
       "chSwitchTypeCodeType": chSwitchTypeCodeType,
       "chSwitchTypeMgmtPreference": chSwitchTypeMgmtPreference,
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
       "chStackUnitRowStatus": chStackUnitRowStatus,
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
       "chStackUnitUtilTable": chStackUnitUtilTable,
       "chStackUnitUtilEntry": chStackUnitUtilEntry,
       "chStackUnitCpuType": chStackUnitCpuType,
       "chStackUnitCpuUtil5Sec": chStackUnitCpuUtil5Sec,
       "chStackUnitCpuUtil1Min": chStackUnitCpuUtil1Min,
       "chStackUnitCpuUtil5Min": chStackUnitCpuUtil5Min,
       "chStackUnitMemUsageUtil": chStackUnitMemUsageUtil,
       "chAlarmObjects": chAlarmObjects,
       "chAlarmMibNotifications": chAlarmMibNotifications,
       "chAlarmStackUnitDown": chAlarmStackUnitDown,
       "chAlarmStackUnitUp": chAlarmStackUnitUp,
       "chAlarmStackUnitReset": chAlarmStackUnitReset,
       "chAlarmStackUnitOffline": chAlarmStackUnitOffline,
       "chAlarmStackUnitCodeMismatch": chAlarmStackUnitCodeMismatch,
       "chAlarmStackPortLinkUp": chAlarmStackPortLinkUp,
       "chAlarmStackPortLinkDown": chAlarmStackPortLinkDown,
       "f10sSeriesMibConformance": f10sSeriesMibConformance,
       "f10sSeriesMibCompliances": f10sSeriesMibCompliances,
       "f10sSeriesMibCompliance": f10sSeriesMibCompliance,
       "f10sSeriesMibGroups": f10sSeriesMibGroups,
       "f10sSeriesComponentGroup": f10sSeriesComponentGroup,
       "f10sSeriesSystemGroup": f10sSeriesSystemGroup,
       "f10sSeriesNotificationGroup": f10sSeriesNotificationGroup}
)
