# SNMP MIB module (IPI-CMM-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ipinfusion\IPI-CMM-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:54 2025
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

(ipi,) = mibBuilder.importSymbols(
    "IPI-MODULE-MIB",
    "ipi")

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

cmm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100)
)
if mibBuilder.loadTexts:
    cmm.setRevisions(
        ("2020-05-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LedColorCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              30)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("none", 1),
          ("green", 2),
          ("blinking-green", 3),
          ("solid-green", 4),
          ("amber", 5),
          ("blinking-amber", 6),
          ("solid-amber", 7),
          ("red", 8),
          ("blinking-red", 9),
          ("solid-red", 10),
          ("blue", 11),
          ("blinking-blue", 12),
          ("yellow", 13),
          ("blinking-yellow", 14),
          ("orange", 15),
          ("slow-blinking-green", 16),
          ("fast-blinking-green", 17),
          ("unknown", 30))
    )



class SystemStatusCode(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cpu", 0),
          ("ram", 1),
          ("disk", 2),
          ("low-temperature", 3),
          ("high-temperature", 4),
          ("fan", 5),
          ("power", 6),
          ("software", 7))
    )


class ErrorFigures(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CmmChassisObject_ObjectIdentity = ObjectIdentity
cmmChassisObject = _CmmChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1)
)
_CmmObjects_ObjectIdentity = ObjectIdentity
cmmObjects = _CmmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 1)
)
_CmmNumStackUnits_Type = Integer32
_CmmNumStackUnits_Object = MibScalar
cmmNumStackUnits = _CmmNumStackUnits_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 1, 1),
    _CmmNumStackUnits_Type()
)
cmmNumStackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmNumStackUnits.setStatus("current")
_CmmSysObjects_ObjectIdentity = ObjectIdentity
cmmSysObjects = _CmmSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2)
)
_CmmStackUnitTable_Object = MibTable
cmmStackUnitTable = _CmmStackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmmStackUnitTable.setStatus("current")
_CmmStackUnitEntry_Object = MibTableRow
cmmStackUnitEntry = _CmmStackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1)
)
cmmStackUnitEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmStackUnitEntry.setStatus("current")


class _CmmStackUnitIndex_Type(Integer32):
    """Custom type cmmStackUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmStackUnitIndex_Type.__name__ = "Integer32"
_CmmStackUnitIndex_Object = MibTableColumn
cmmStackUnitIndex = _CmmStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 1),
    _CmmStackUnitIndex_Type()
)
cmmStackUnitIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmStackUnitIndex.setStatus("current")
_CmmStackUnitModelName_Type = DisplayString
_CmmStackUnitModelName_Object = MibTableColumn
cmmStackUnitModelName = _CmmStackUnitModelName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 2),
    _CmmStackUnitModelName_Type()
)
cmmStackUnitModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitModelName.setStatus("current")
_CmmStackUnitSerialNumber_Type = DisplayString
_CmmStackUnitSerialNumber_Object = MibTableColumn
cmmStackUnitSerialNumber = _CmmStackUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 3),
    _CmmStackUnitSerialNumber_Type()
)
cmmStackUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitSerialNumber.setStatus("current")
_CmmStackUnitUpTime_Type = TimeTicks
_CmmStackUnitUpTime_Object = MibTableColumn
cmmStackUnitUpTime = _CmmStackUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 4),
    _CmmStackUnitUpTime_Type()
)
cmmStackUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitUpTime.setStatus("current")
_CmmStackUnitMfgDate_Type = DateAndTime
_CmmStackUnitMfgDate_Object = MibTableColumn
cmmStackUnitMfgDate = _CmmStackUnitMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 5),
    _CmmStackUnitMfgDate_Type()
)
cmmStackUnitMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitMfgDate.setStatus("current")
_CmmStackUnitMacAddress_Type = MacAddress
_CmmStackUnitMacAddress_Object = MibTableColumn
cmmStackUnitMacAddress = _CmmStackUnitMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 6),
    _CmmStackUnitMacAddress_Type()
)
cmmStackUnitMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitMacAddress.setStatus("current")
_CmmStackUnitPartNum_Type = DisplayString
_CmmStackUnitPartNum_Object = MibTableColumn
cmmStackUnitPartNum = _CmmStackUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 7),
    _CmmStackUnitPartNum_Type()
)
cmmStackUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitPartNum.setStatus("current")
_CmmStackLabelRevision_Type = DisplayString
_CmmStackLabelRevision_Object = MibTableColumn
cmmStackLabelRevision = _CmmStackLabelRevision_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 8),
    _CmmStackLabelRevision_Type()
)
cmmStackLabelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackLabelRevision.setStatus("current")


class _CmmStackUnitCountryCode_Type(OctetString):
    """Custom type cmmStackUnitCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CmmStackUnitCountryCode_Type.__name__ = "OctetString"
_CmmStackUnitCountryCode_Object = MibTableColumn
cmmStackUnitCountryCode = _CmmStackUnitCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 9),
    _CmmStackUnitCountryCode_Type()
)
cmmStackUnitCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCountryCode.setStatus("current")


class _CmmStackUnitServiceTag_Type(DisplayString):
    """Custom type cmmStackUnitServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_CmmStackUnitServiceTag_Type.__name__ = "DisplayString"
_CmmStackUnitServiceTag_Object = MibTableColumn
cmmStackUnitServiceTag = _CmmStackUnitServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 10),
    _CmmStackUnitServiceTag_Type()
)
cmmStackUnitServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitServiceTag.setStatus("current")
_CmmStackPlatformName_Type = DisplayString
_CmmStackPlatformName_Object = MibTableColumn
cmmStackPlatformName = _CmmStackPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 11),
    _CmmStackPlatformName_Type()
)
cmmStackPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackPlatformName.setStatus("current")
_CmmStackOnieVersion_Type = DisplayString
_CmmStackOnieVersion_Object = MibTableColumn
cmmStackOnieVersion = _CmmStackOnieVersion_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 12),
    _CmmStackOnieVersion_Type()
)
cmmStackOnieVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackOnieVersion.setStatus("current")
_CmmStackMfgName_Type = DisplayString
_CmmStackMfgName_Object = MibTableColumn
cmmStackMfgName = _CmmStackMfgName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 13),
    _CmmStackMfgName_Type()
)
cmmStackMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackMfgName.setStatus("current")
_CmmStackVendorName_Type = DisplayString
_CmmStackVendorName_Object = MibTableColumn
cmmStackVendorName = _CmmStackVendorName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 14),
    _CmmStackVendorName_Type()
)
cmmStackVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackVendorName.setStatus("current")
_CmmStackDiagVersion_Type = DisplayString
_CmmStackDiagVersion_Object = MibTableColumn
cmmStackDiagVersion = _CmmStackDiagVersion_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 15),
    _CmmStackDiagVersion_Type()
)
cmmStackDiagVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackDiagVersion.setStatus("current")


class _CmmStackCrc32_Type(OctetString):
    """Custom type cmmStackCrc32 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_CmmStackCrc32_Type.__name__ = "OctetString"
_CmmStackCrc32_Object = MibTableColumn
cmmStackCrc32 = _CmmStackCrc32_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 16),
    _CmmStackCrc32_Type()
)
cmmStackCrc32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCrc32.setStatus("current")
_CmmStackUnitNumFanControllers_Type = Integer32
_CmmStackUnitNumFanControllers_Object = MibTableColumn
cmmStackUnitNumFanControllers = _CmmStackUnitNumFanControllers_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 17),
    _CmmStackUnitNumFanControllers_Type()
)
cmmStackUnitNumFanControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumFanControllers.setStatus("current")
_CmmStackUnitNumFanTrays_Type = Integer32
_CmmStackUnitNumFanTrays_Object = MibTableColumn
cmmStackUnitNumFanTrays = _CmmStackUnitNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 18),
    _CmmStackUnitNumFanTrays_Type()
)
cmmStackUnitNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumFanTrays.setStatus("current")
_CmmStackUnitNumPowerSupplies_Type = Integer32
_CmmStackUnitNumPowerSupplies_Object = MibTableColumn
cmmStackUnitNumPowerSupplies = _CmmStackUnitNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 19),
    _CmmStackUnitNumPowerSupplies_Type()
)
cmmStackUnitNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumPowerSupplies.setStatus("current")
_CmmStackUnitNumPluggableModules_Type = Integer32
_CmmStackUnitNumPluggableModules_Object = MibTableColumn
cmmStackUnitNumPluggableModules = _CmmStackUnitNumPluggableModules_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 20),
    _CmmStackUnitNumPluggableModules_Type()
)
cmmStackUnitNumPluggableModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumPluggableModules.setStatus("current")
_CmmStackUnitNumFastEtherPorts_Type = Integer32
_CmmStackUnitNumFastEtherPorts_Object = MibTableColumn
cmmStackUnitNumFastEtherPorts = _CmmStackUnitNumFastEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 21),
    _CmmStackUnitNumFastEtherPorts_Type()
)
cmmStackUnitNumFastEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumFastEtherPorts.setStatus("current")
_CmmStackUnitNumGigEtherPorts_Type = Integer32
_CmmStackUnitNumGigEtherPorts_Object = MibTableColumn
cmmStackUnitNumGigEtherPorts = _CmmStackUnitNumGigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 22),
    _CmmStackUnitNumGigEtherPorts_Type()
)
cmmStackUnitNumGigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumGigEtherPorts.setStatus("current")
_CmmStackUnitNum10GigEtherPorts_Type = Integer32
_CmmStackUnitNum10GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum10GigEtherPorts = _CmmStackUnitNum10GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 23),
    _CmmStackUnitNum10GigEtherPorts_Type()
)
cmmStackUnitNum10GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum10GigEtherPorts.setStatus("current")
_CmmStackUnitNum25GigEtherPorts_Type = Integer32
_CmmStackUnitNum25GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum25GigEtherPorts = _CmmStackUnitNum25GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 24),
    _CmmStackUnitNum25GigEtherPorts_Type()
)
cmmStackUnitNum25GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum25GigEtherPorts.setStatus("current")
_CmmStackUnitNum40GigEtherPorts_Type = Integer32
_CmmStackUnitNum40GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum40GigEtherPorts = _CmmStackUnitNum40GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 25),
    _CmmStackUnitNum40GigEtherPorts_Type()
)
cmmStackUnitNum40GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum40GigEtherPorts.setStatus("current")
_CmmStackUnitNum50GigEtherPorts_Type = Integer32
_CmmStackUnitNum50GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum50GigEtherPorts = _CmmStackUnitNum50GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 26),
    _CmmStackUnitNum50GigEtherPorts_Type()
)
cmmStackUnitNum50GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum50GigEtherPorts.setStatus("current")
_CmmStackUnitNum100GigEtherPorts_Type = Integer32
_CmmStackUnitNum100GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum100GigEtherPorts = _CmmStackUnitNum100GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 27),
    _CmmStackUnitNum100GigEtherPorts_Type()
)
cmmStackUnitNum100GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum100GigEtherPorts.setStatus("current")
_CmmStackUnitSwitchChipRev_Type = DisplayString
_CmmStackUnitSwitchChipRev_Object = MibTableColumn
cmmStackUnitSwitchChipRev = _CmmStackUnitSwitchChipRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 28),
    _CmmStackUnitSwitchChipRev_Type()
)
cmmStackUnitSwitchChipRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitSwitchChipRev.setStatus("current")
_CmmStackSupportedLabelRevision_Type = DisplayString
_CmmStackSupportedLabelRevision_Object = MibTableColumn
cmmStackSupportedLabelRevision = _CmmStackSupportedLabelRevision_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 29),
    _CmmStackSupportedLabelRevision_Type()
)
cmmStackSupportedLabelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackSupportedLabelRevision.setStatus("current")
_CmmStackUnitSupportedSwitchChipRev_Type = DisplayString
_CmmStackUnitSupportedSwitchChipRev_Object = MibTableColumn
cmmStackUnitSupportedSwitchChipRev = _CmmStackUnitSupportedSwitchChipRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 30),
    _CmmStackUnitSupportedSwitchChipRev_Type()
)
cmmStackUnitSupportedSwitchChipRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitSupportedSwitchChipRev.setStatus("current")
_CmmTransEEPROMTable_Object = MibTable
cmmTransEEPROMTable = _CmmTransEEPROMTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmmTransEEPROMTable.setStatus("current")
_CmmTransEEPROMEntry_Object = MibTableRow
cmmTransEEPROMEntry = _CmmTransEEPROMEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1)
)
cmmTransEEPROMEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
)
if mibBuilder.loadTexts:
    cmmTransEEPROMEntry.setStatus("current")


class _CmmTransIndex_Type(Integer32):
    """Custom type cmmTransIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmTransIndex_Type.__name__ = "Integer32"
_CmmTransIndex_Object = MibTableColumn
cmmTransIndex = _CmmTransIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 1),
    _CmmTransIndex_Type()
)
cmmTransIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmTransIndex.setStatus("current")


class _CmmTransType_Type(Integer32):
    """Custom type cmmTransType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("sfp", 1),
          ("qsfp", 2),
          ("xfp", 3),
          ("pon-xfp", 4))
    )


_CmmTransType_Type.__name__ = "Integer32"
_CmmTransType_Object = MibTableColumn
cmmTransType = _CmmTransType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 2),
    _CmmTransType_Type()
)
cmmTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransType.setStatus("current")
_CmmTransNoOfChannels_Type = Integer32
_CmmTransNoOfChannels_Object = MibTableColumn
cmmTransNoOfChannels = _CmmTransNoOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 3),
    _CmmTransNoOfChannels_Type()
)
cmmTransNoOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransNoOfChannels.setStatus("current")


class _CmmTransidentifier_Type(Integer32):
    """Custom type cmmTransidentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("id-unknown", 1),
          ("gbic", 2),
          ("soldered-to-motherboard", 3),
          ("sfp-or-sfpplus-or-sfp28", 4),
          ("xbi-300pin", 5),
          ("xenpak", 6),
          ("xfp", 7),
          ("xff", 8),
          ("xfpe", 9),
          ("xpak", 10),
          ("x2", 11),
          ("dwdmsfp-or-dwdmsfpplus", 12),
          ("qsfp", 13),
          ("qsfpplus-or-later", 14),
          ("cxp-or-later", 15),
          ("shielded-mini-multilane-hd4x", 16),
          ("shielded-mini-multilane-hd8x", 17),
          ("qsfp28-or-later", 18),
          ("cxp2-aka-cxp28-or-later", 19),
          ("cdfpstyle1-or-cdfpstyle2", 20),
          ("shielded-mini-multilane-hd4x-fanoutcable", 21),
          ("shielded-mini-multilane-hd8x-fanoutcable", 22),
          ("cdfpstyle3", 23),
          ("microqsfp", 24),
          ("qsfp-doubledensity-8x-pluggable-transceiver", 25),
          ("reserved", 26),
          ("vendor-specific", 27))
    )


_CmmTransidentifier_Type.__name__ = "Integer32"
_CmmTransidentifier_Object = MibTableColumn
cmmTransidentifier = _CmmTransidentifier_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 4),
    _CmmTransidentifier_Type()
)
cmmTransidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransidentifier.setStatus("current")


class _CmmTransSFPextendedidentifier_Type(Integer32):
    """Custom type cmmTransSFPextendedidentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("gbic-notspecified-or-compliant-with-moddef", 1),
          ("gbic-compliant-with-moddef1", 2),
          ("gbic-compliant-with-moddef2", 3),
          ("gbic-compliant-with-moddef3", 4),
          ("gbic-or-sfp-definedby-twowire-interfaceid-only", 5),
          ("gbic-compliant-with-moddef5", 6),
          ("gbic-compliant-with-moddef6", 7),
          ("gbic-compliant-with-moddef7", 8),
          ("unallocated", 9))
    )


_CmmTransSFPextendedidentifier_Type.__name__ = "Integer32"
_CmmTransSFPextendedidentifier_Object = MibTableColumn
cmmTransSFPextendedidentifier = _CmmTransSFPextendedidentifier_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 5),
    _CmmTransSFPextendedidentifier_Type()
)
cmmTransSFPextendedidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPextendedidentifier.setStatus("current")


class _CmmTransQSFPextendedidentifier_Type(Bits):
    """Custom type cmmTransQSFPextendedidentifier based on Bits"""
    namedValues = NamedValues(
        *(("powerclass1-1dot5wmax", 0),
          ("powerclass2-2wmax", 1),
          ("powerclass3-2dot5wmax", 2),
          ("powerclass4-3dot5wmax", 3),
          ("cleicode-present", 4),
          ("cdrpresent-in-tx", 5),
          ("cdrpresent-in-rx", 6),
          ("powerclass5-4wmax", 7),
          ("powerclass6-4dot5wmax", 8),
          ("powerclass7-5wmax", 9),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransQSFPextendedidentifier_Type.__name__ = "Bits"
_CmmTransQSFPextendedidentifier_Object = MibTableColumn
cmmTransQSFPextendedidentifier = _CmmTransQSFPextendedidentifier_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 6),
    _CmmTransQSFPextendedidentifier_Type()
)
cmmTransQSFPextendedidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransQSFPextendedidentifier.setStatus("current")


class _CmmTransconnectortype_Type(Integer32):
    """Custom type cmmTransconnectortype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("type-unknown", 1),
          ("subscriber-connector", 2),
          ("fibrechannel-style1-copperconnector", 3),
          ("fibrechannel-style2-copperconnector", 4),
          ("bayonet-or-threaded-neill-concelman", 5),
          ("fibrechannel-coaxheaders", 6),
          ("fiber-jack", 7),
          ("lucent-connector", 8),
          ("mechanical-transfer-registeredjack", 9),
          ("multiple-optical", 10),
          ("sg", 11),
          ("optical-pigtail", 12),
          ("multifiber-paralleloptic-1x12", 13),
          ("multifiber-paralleloptic-1x16", 14),
          ("hssdcii", 15),
          ("copper-pigtail", 16),
          ("rj45", 17),
          ("no-separable-connector", 18),
          ("mxc2-x16", 19),
          ("reserved", 20),
          ("vendor-specific", 21))
    )


_CmmTransconnectortype_Type.__name__ = "Integer32"
_CmmTransconnectortype_Object = MibTableColumn
cmmTransconnectortype = _CmmTransconnectortype_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 7),
    _CmmTransconnectortype_Type()
)
cmmTransconnectortype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransconnectortype.setStatus("current")


class _CmmTransEthCompliance_Type(Integer32):
    """Custom type cmmTransEthCompliance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("ec-unknown", 1),
          ("ec-10gbase-sr", 2),
          ("ec-10gbase-lr", 3),
          ("ec-10gbase-lrm", 4),
          ("ec-10gbase-er", 5),
          ("ec-1000base-sx", 6),
          ("ec-1000base-lx", 7),
          ("ec-1000base-cx", 8),
          ("ec-1000base-t", 9),
          ("ec-100base-lx-or-lx10", 10),
          ("ec-100base-fx", 11),
          ("ec-base-bx10", 12),
          ("ec-base-px", 13),
          ("ec-40gbase-cr4", 14),
          ("ec-40gbase-sr4", 15),
          ("ec-40gbase-lr4", 16),
          ("ec-40g-activecable", 17))
    )


_CmmTransEthCompliance_Type.__name__ = "Integer32"
_CmmTransEthCompliance_Object = MibTableColumn
cmmTransEthCompliance = _CmmTransEthCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 8),
    _CmmTransEthCompliance_Type()
)
cmmTransEthCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransEthCompliance.setStatus("current")


class _CmmTransExtEthCompliance_Type(Integer32):
    """Custom type cmmTransExtEthCompliance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              127,
              128,
              129)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("eec-unspecified", 0),
          ("eec-100g-activeopticalcable-or-25g-auic2maoc", 1),
          ("eec-100gbase-sr4-or-25gbase-sr", 2),
          ("eec-100gbase-lr4-or-25gbase-lr", 3),
          ("eec-100gbase-er4-or-25gbase-er", 4),
          ("eec-100gbase-sr10", 5),
          ("eec-100g-cwdm4", 6),
          ("eec-100g-psm4-parallelsmf", 7),
          ("eec-100g-activecoppercable-or-25g-auic2macc", 8),
          ("eec-obsolete", 9),
          ("eec-reserved", 10),
          ("eec-100gbase-cr4-or-25gbase-crca-l", 11),
          ("eec-25gbase-crca-s", 12),
          ("eec-25gbase-crca-n", 13),
          ("eec-10mb-single-pair-eth", 14),
          ("eec-40gbase-er4", 16),
          ("eec-4x10gbase-sr", 17),
          ("eec-40g-psm4-parallelsmf", 18),
          ("eec-g959-dot1-profilep1-i1-2d1", 19),
          ("eec-g959-dot1-profilep1-s1-2d2", 20),
          ("eec-g959-dot1-profilep1-l1-2d2", 21),
          ("eec-10gbase-t-with-sfi-electricalinterface", 22),
          ("eec-100g-clr4", 23),
          ("eec-100g-aoc-or-25g-auic2maoc", 24),
          ("eec-100g-acc-or-25g-auic2macc", 25),
          ("eec-100ge-dwdm2", 26),
          ("eec-100g-1550nm-wdm", 27),
          ("eec-10gbaset-short-reach", 28),
          ("eec-5gbaset", 29),
          ("eec-2point5gbaset", 30),
          ("eec-40g-swdm4", 31),
          ("eec-100g-swdm4", 32),
          ("eec-100g-pam4-bidi", 33),
          ("eec-100g-4wdm-10msa", 34),
          ("eec-100g-4wdm-20msa", 35),
          ("eec-100g-4wdm-40msa", 36),
          ("eec-100gbase-dr-clause140", 37),
          ("eec-100g-fr-or-fr1-clause140", 38),
          ("eec-100g-lr-or-lr1-clause140", 39),
          ("eec-100gbase-sr1-p802-clause167", 40),
          ("eec-100gbase-sr1-200gbase-sr2-400gbase-sr4-clause167", 41),
          ("eec-100gbase-fr1-clause140", 42),
          ("eec-100gbase-lr1-clause140", 43),
          ("eec-100g-lr1-20msa-and-caui4", 44),
          ("eec-100g-er1-30msa-and-caui4", 45),
          ("eec-100g-er1-40msa-and-caui4", 46),
          ("eec-100g-lr1-20msa", 47),
          ("eec-acc-with-50gaui-100gaui2-200gaui4-c2m-worst-ber-10minus6", 48),
          ("eec-aoc-with-50gaui-100gaui2-200gaui4-c2m-worst-ber-10minus6", 49),
          ("eec-acc-with-50gaui-100gaui2-200gaui4-c2m-worst-ber-10minus5", 50),
          ("eec-aoc-with-50gaui-100gaui2-200gaui4-c2m-worst-ber-10-minus5", 51),
          ("eec-100g-er1-30msa", 52),
          ("eec-100g-er1-40msa", 53),
          ("eec-100gbase-vr1-200gbase-vr2-400gbase-sr4-clause167", 54),
          ("eec-10gbase-br", 55),
          ("eec-25gbase-br", 56),
          ("eec-50gbase-br", 57),
          ("eec-100gbase-vr1-p802-clause167", 58),
          ("eec-100gbase-cr1-200gbase-cr2-400gbase-cr4-clause162", 63),
          ("eec-50gbase-cr-100gbase-cr2-200gbase-cr4", 64),
          ("eec-50gbase-sr-100gbase-sr2-200gbase-sr4", 65),
          ("eec-50gbase-fr-200gbase-dr4", 66),
          ("eec-200gbase-fr4", 67),
          ("eec-200g-1550nm-psm4", 68),
          ("eec-50gbase-lr", 69),
          ("eec-200gbase-lr4", 70),
          ("eec-400gbase-dr4-clause124", 71),
          ("eec-400gbase-fr4-clause151", 72),
          ("eec-400gbase-fr46-clause151", 73),
          ("eec-50gbase-er-clause139", 74),
          ("eec-400g-lr410", 75),
          ("eec-400gbase-zr-clause156", 76),
          ("eec-256gfc-sw4", 127),
          ("eec-64gfc", 128),
          ("eec-128gfc", 129))
    )


_CmmTransExtEthCompliance_Type.__name__ = "Integer32"
_CmmTransExtEthCompliance_Object = MibTableColumn
cmmTransExtEthCompliance = _CmmTransExtEthCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 9),
    _CmmTransExtEthCompliance_Type()
)
cmmTransExtEthCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransExtEthCompliance.setStatus("current")


class _CmmTransSonetCompliance_Type(Bits):
    """Custom type cmmTransSonetCompliance based on Bits"""
    namedValues = NamedValues(
        *(("oc192-shortreach", 0),
          ("sonet-reachspecifier-bit1", 1),
          ("sonet-reachspecifier-bit2", 2),
          ("oc48-longreach", 3),
          ("oc48-intermediatereach", 4),
          ("oc48-shortreach", 5),
          ("oc12-singlemode-longreach", 6),
          ("oc12-singlemode-intermediatereach", 7),
          ("oc12-singlemode-shortreach", 8),
          ("oc3-singlemode-longreach", 9),
          ("oc3-singlemode-intermediatereach", 10),
          ("oc3-singlemode-shortreach", 11),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransSonetCompliance_Type.__name__ = "Bits"
_CmmTransSonetCompliance_Object = MibTableColumn
cmmTransSonetCompliance = _CmmTransSonetCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 10),
    _CmmTransSonetCompliance_Type()
)
cmmTransSonetCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSonetCompliance.setStatus("current")


class _CmmTransFiberChnlLinkLen_Type(Bits):
    """Custom type cmmTransFiberChnlLinkLen based on Bits"""
    namedValues = NamedValues(
        *(("short", 0),
          ("medium", 1),
          ("intermediate", 2),
          ("long", 3),
          ("verylong", 4),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransFiberChnlLinkLen_Type.__name__ = "Bits"
_CmmTransFiberChnlLinkLen_Object = MibTableColumn
cmmTransFiberChnlLinkLen = _CmmTransFiberChnlLinkLen_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 11),
    _CmmTransFiberChnlLinkLen_Type()
)
cmmTransFiberChnlLinkLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFiberChnlLinkLen.setStatus("current")


class _CmmTransFiberChnlTransTech_Type(Bits):
    """Custom type cmmTransFiberChnlTransTech based on Bits"""
    namedValues = NamedValues(
        *(("shortwaveLaserLinearRx", 0),
          ("longwaveLaserLC", 1),
          ("electricalInter-Enclosure", 2),
          ("electricalIntra-Enclosure", 3),
          ("shortwaveLaserWithOutOFC", 4),
          ("shortwaveLaserwithOFC", 5),
          ("longwaveLaserLL", 6),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransFiberChnlTransTech_Type.__name__ = "Bits"
_CmmTransFiberChnlTransTech_Object = MibTableColumn
cmmTransFiberChnlTransTech = _CmmTransFiberChnlTransTech_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 12),
    _CmmTransFiberChnlTransTech_Type()
)
cmmTransFiberChnlTransTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFiberChnlTransTech.setStatus("current")


class _CmmTransFiberChnlTransMedia_Type(Bits):
    """Custom type cmmTransFiberChnlTransMedia based on Bits"""
    namedValues = NamedValues(
        *(("twinaxial-pair", 0),
          ("twisted-pair", 1),
          ("miniature-coax", 2),
          ("video-coax", 3),
          ("multi-mode62dot5m", 4),
          ("multi-mode50m", 5),
          ("multi-mode50um", 6),
          ("single-mode", 7),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransFiberChnlTransMedia_Type.__name__ = "Bits"
_CmmTransFiberChnlTransMedia_Object = MibTableColumn
cmmTransFiberChnlTransMedia = _CmmTransFiberChnlTransMedia_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 13),
    _CmmTransFiberChnlTransMedia_Type()
)
cmmTransFiberChnlTransMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFiberChnlTransMedia.setStatus("current")


class _CmmTransSFPFiberChnlSpeed_Type(Bits):
    """Custom type cmmTransSFPFiberChnlSpeed based on Bits"""
    namedValues = NamedValues(
        *(("fcs-3200mbps", 0),
          ("fcs-1600mbps", 1),
          ("fcs-1200mbps", 2),
          ("fcs-800mbps", 3),
          ("fcs-400mbps", 4),
          ("fcs-200mbps", 5),
          ("fcs-100mbps", 6),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransSFPFiberChnlSpeed_Type.__name__ = "Bits"
_CmmTransSFPFiberChnlSpeed_Object = MibTableColumn
cmmTransSFPFiberChnlSpeed = _CmmTransSFPFiberChnlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 14),
    _CmmTransSFPFiberChnlSpeed_Type()
)
cmmTransSFPFiberChnlSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPFiberChnlSpeed.setStatus("current")


class _CmmTransQSFPFiberChnlSpeed_Type(Bits):
    """Custom type cmmTransQSFPFiberChnlSpeed based on Bits"""
    namedValues = NamedValues(
        *(("fcs-3200mbps", 0),
          ("fcs-1600mbps", 1),
          ("fcs-1200mbps", 2),
          ("fcs-800mbps", 3),
          ("fcs-400mbps", 4),
          ("fcs-200mbps", 5),
          ("fcs-100mbps", 6),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransQSFPFiberChnlSpeed_Type.__name__ = "Bits"
_CmmTransQSFPFiberChnlSpeed_Object = MibTableColumn
cmmTransQSFPFiberChnlSpeed = _CmmTransQSFPFiberChnlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 15),
    _CmmTransQSFPFiberChnlSpeed_Type()
)
cmmTransQSFPFiberChnlSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransQSFPFiberChnlSpeed.setStatus("current")


class _CmmTransSFPInfiniBandCompliance_Type(Integer32):
    """Custom type cmmTransSFPInfiniBandCompliance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("ibc-1xsx", 1),
          ("ibc-1xlx", 2),
          ("ibc-1xcopperactive", 3),
          ("ibc-1xcopperpassive", 4))
    )


_CmmTransSFPInfiniBandCompliance_Type.__name__ = "Integer32"
_CmmTransSFPInfiniBandCompliance_Object = MibTableColumn
cmmTransSFPInfiniBandCompliance = _CmmTransSFPInfiniBandCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 16),
    _CmmTransSFPInfiniBandCompliance_Type()
)
cmmTransSFPInfiniBandCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPInfiniBandCompliance.setStatus("current")


class _CmmTransSFPEsconCompliance_Type(Integer32):
    """Custom type cmmTransSFPEsconCompliance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("escon-mmf-1310nm-led", 1),
          ("escon-smf-1310nm-laser", 2))
    )


_CmmTransSFPEsconCompliance_Type.__name__ = "Integer32"
_CmmTransSFPEsconCompliance_Object = MibTableColumn
cmmTransSFPEsconCompliance = _CmmTransSFPEsconCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 17),
    _CmmTransSFPEsconCompliance_Type()
)
cmmTransSFPEsconCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPEsconCompliance.setStatus("current")


class _CmmTransSfpPlusCableTech_Type(Integer32):
    """Custom type cmmTransSfpPlusCableTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("active", 1),
          ("passive", 2))
    )


_CmmTransSfpPlusCableTech_Type.__name__ = "Integer32"
_CmmTransSfpPlusCableTech_Object = MibTableColumn
cmmTransSfpPlusCableTech = _CmmTransSfpPlusCableTech_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 18),
    _CmmTransSfpPlusCableTech_Type()
)
cmmTransSfpPlusCableTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSfpPlusCableTech.setStatus("current")


class _CmmTransEncoding_Type(Integer32):
    """Custom type cmmTransEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("enc-unspecified", 1),
          ("enc-8b-or-10b", 2),
          ("enc-4b-or-5b", 3),
          ("enc-nrz", 4),
          ("enc-manchester", 5),
          ("enc-sonet-scrambled", 6),
          ("enc-64b-or-66b", 7),
          ("enc-256b-or-257b", 8),
          ("enc-pam4", 9),
          ("enc-reserved", 10))
    )


_CmmTransEncoding_Type.__name__ = "Integer32"
_CmmTransEncoding_Object = MibTableColumn
cmmTransEncoding = _CmmTransEncoding_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 19),
    _CmmTransEncoding_Type()
)
cmmTransEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransEncoding.setStatus("current")
_CmmTransLengthKmtrs_Type = Integer32
_CmmTransLengthKmtrs_Object = MibTableColumn
cmmTransLengthKmtrs = _CmmTransLengthKmtrs_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 20),
    _CmmTransLengthKmtrs_Type()
)
cmmTransLengthKmtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthKmtrs.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthKmtrs.setUnits("km")
_CmmTransLengthMtrs_Type = Integer32
_CmmTransLengthMtrs_Object = MibTableColumn
cmmTransLengthMtrs = _CmmTransLengthMtrs_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 21),
    _CmmTransLengthMtrs_Type()
)
cmmTransLengthMtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthMtrs.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthMtrs.setUnits("100 m")
_CmmTransLengthOM1_Type = Integer32
_CmmTransLengthOM1_Object = MibTableColumn
cmmTransLengthOM1 = _CmmTransLengthOM1_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 22),
    _CmmTransLengthOM1_Type()
)
cmmTransLengthOM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM1.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM1.setUnits("10 m")
_CmmTransLengthOM2_Type = Integer32
_CmmTransLengthOM2_Object = MibTableColumn
cmmTransLengthOM2 = _CmmTransLengthOM2_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 23),
    _CmmTransLengthOM2_Type()
)
cmmTransLengthOM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM2.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM2.setUnits("10 m")
_CmmTransLengthOM3_Type = Integer32
_CmmTransLengthOM3_Object = MibTableColumn
cmmTransLengthOM3 = _CmmTransLengthOM3_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 24),
    _CmmTransLengthOM3_Type()
)
cmmTransLengthOM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM3.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM3.setUnits("10 m")
_CmmTransLengthOM4_Type = Integer32
_CmmTransLengthOM4_Object = MibTableColumn
cmmTransLengthOM4 = _CmmTransLengthOM4_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 25),
    _CmmTransLengthOM4_Type()
)
cmmTransLengthOM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM4.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM4.setUnits("10 m")
_CmmTransVendorName_Type = DisplayString
_CmmTransVendorName_Object = MibTableColumn
cmmTransVendorName = _CmmTransVendorName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 26),
    _CmmTransVendorName_Type()
)
cmmTransVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorName.setStatus("current")
_CmmTransVendorOUI_Type = DisplayString
_CmmTransVendorOUI_Object = MibTableColumn
cmmTransVendorOUI = _CmmTransVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 27),
    _CmmTransVendorOUI_Type()
)
cmmTransVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorOUI.setStatus("current")
_CmmTransVendorPartNumber_Type = DisplayString
_CmmTransVendorPartNumber_Object = MibTableColumn
cmmTransVendorPartNumber = _CmmTransVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 28),
    _CmmTransVendorPartNumber_Type()
)
cmmTransVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorPartNumber.setStatus("current")
_CmmTransVendorRevision_Type = DisplayString
_CmmTransVendorRevision_Object = MibTableColumn
cmmTransVendorRevision = _CmmTransVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 29),
    _CmmTransVendorRevision_Type()
)
cmmTransVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorRevision.setStatus("current")


class _CmmTransCheckCode_Type(OctetString):
    """Custom type cmmTransCheckCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CmmTransCheckCode_Type.__name__ = "OctetString"
_CmmTransCheckCode_Object = MibTableColumn
cmmTransCheckCode = _CmmTransCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 30),
    _CmmTransCheckCode_Type()
)
cmmTransCheckCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransCheckCode.setStatus("current")


class _CmmTransCheckCodeExtended_Type(OctetString):
    """Custom type cmmTransCheckCodeExtended based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CmmTransCheckCodeExtended_Type.__name__ = "OctetString"
_CmmTransCheckCodeExtended_Object = MibTableColumn
cmmTransCheckCodeExtended = _CmmTransCheckCodeExtended_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 31),
    _CmmTransCheckCodeExtended_Type()
)
cmmTransCheckCodeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransCheckCodeExtended.setStatus("current")
_CmmTransNominalBitRate_Type = Integer32
_CmmTransNominalBitRate_Object = MibTableColumn
cmmTransNominalBitRate = _CmmTransNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 32),
    _CmmTransNominalBitRate_Type()
)
cmmTransNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransNominalBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransNominalBitRate.setUnits("100MBd")
_CmmTransBitRateMax_Type = Integer32
_CmmTransBitRateMax_Object = MibTableColumn
cmmTransBitRateMax = _CmmTransBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 33),
    _CmmTransBitRateMax_Type()
)
cmmTransBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransBitRateMax.setStatus("current")
_CmmTransBitRateMin_Type = Integer32
_CmmTransBitRateMin_Object = MibTableColumn
cmmTransBitRateMin = _CmmTransBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 34),
    _CmmTransBitRateMin_Type()
)
cmmTransBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransBitRateMin.setStatus("current")
_CmmTransVendorSerialNumber_Type = DisplayString
_CmmTransVendorSerialNumber_Object = MibTableColumn
cmmTransVendorSerialNumber = _CmmTransVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 35),
    _CmmTransVendorSerialNumber_Type()
)
cmmTransVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorSerialNumber.setStatus("current")
_CmmTransDateCode_Type = DisplayString
_CmmTransDateCode_Object = MibTableColumn
cmmTransDateCode = _CmmTransDateCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 36),
    _CmmTransDateCode_Type()
)
cmmTransDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransDateCode.setStatus("current")


class _CmmTransDDMSupport_Type(Integer32):
    """Custom type cmmTransDDMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("yes", 1),
          ("no", 2))
    )


_CmmTransDDMSupport_Type.__name__ = "Integer32"
_CmmTransDDMSupport_Object = MibTableColumn
cmmTransDDMSupport = _CmmTransDDMSupport_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 37),
    _CmmTransDDMSupport_Type()
)
cmmTransDDMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransDDMSupport.setStatus("current")
_CmmTransMaxCaseTemp_Type = Integer32
_CmmTransMaxCaseTemp_Object = MibTableColumn
cmmTransMaxCaseTemp = _CmmTransMaxCaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 38),
    _CmmTransMaxCaseTemp_Type()
)
cmmTransMaxCaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransMaxCaseTemp.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransMaxCaseTemp.setUnits(" 0.01 C ")


class _CmmTransSFPOptionsImp_Type(Bits):
    """Custom type cmmTransSFPOptionsImp based on Bits"""
    namedValues = NamedValues(
        *(("reserved", 0),
          ("power-level3", 1),
          ("paging", 2),
          ("internal-retimer-or-cdr", 3),
          ("cooled-laser-transmitter", 4),
          ("power-level2", 5),
          ("power-level1", 6),
          ("linear-receiver-output", 7),
          ("receiver-decision-threshold", 8),
          ("transmitter-wavelength-or-tunable-frequency", 9),
          ("rate-select", 10),
          ("tx-disable", 11),
          ("tx-fault", 12),
          ("rx-loss-of-signal", 13),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransSFPOptionsImp_Type.__name__ = "Bits"
_CmmTransSFPOptionsImp_Object = MibTableColumn
cmmTransSFPOptionsImp = _CmmTransSFPOptionsImp_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 39),
    _CmmTransSFPOptionsImp_Type()
)
cmmTransSFPOptionsImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPOptionsImp.setStatus("current")


class _CmmTransQSFPOptionsImp_Type(Bits):
    """Custom type cmmTransQSFPOptionsImp based on Bits"""
    namedValues = NamedValues(
        *(("reserved", 0),
          ("tx-inputequalization-auto-adaptive", 1),
          ("tx-inputequalization-fixed-programmable", 2),
          ("tx-outputemphasis-fixed-programmable", 3),
          ("tx-outputamplitude-fixed-programmable", 4),
          ("tx-cdr-on-or-off-controllable", 5),
          ("tx-cdr-on-or-off-fixed", 6),
          ("rx-cdr-on-or-off-controllable", 7),
          ("rx-cdr-on-or-off-fixed", 8),
          ("tx-cdr-lossoflock", 9),
          ("rx-cdr-lossoflock", 10),
          ("rx-squelch-disable", 11),
          ("rx-output-disable", 12),
          ("tx-squelch-disable", 13),
          ("tx-squelch", 14),
          ("page2-provided", 15),
          ("page1-provided", 16),
          ("rateselect-controllable", 17),
          ("rateselect-fixed", 18),
          ("tx-disable", 19),
          ("tx-fault", 20),
          ("tx-squelch-to-reduce-pave", 21),
          ("tx-squelch-to-reduce-oma", 22),
          ("tx-loss-of-signal", 23),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransQSFPOptionsImp_Type.__name__ = "Bits"
_CmmTransQSFPOptionsImp_Object = MibTableColumn
cmmTransQSFPOptionsImp = _CmmTransQSFPOptionsImp_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 40),
    _CmmTransQSFPOptionsImp_Type()
)
cmmTransQSFPOptionsImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransQSFPOptionsImp.setStatus("current")


class _CmmTransPresence_Type(Integer32):
    """Custom type cmmTransPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("present", 1),
          ("notpresent", 2))
    )


_CmmTransPresence_Type.__name__ = "Integer32"
_CmmTransPresence_Object = MibTableColumn
cmmTransPresence = _CmmTransPresence_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 41),
    _CmmTransPresence_Type()
)
cmmTransPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPresence.setStatus("current")
_CmmTransFrontPanelPortNumber_Type = Integer32
_CmmTransFrontPanelPortNumber_Object = MibTableColumn
cmmTransFrontPanelPortNumber = _CmmTransFrontPanelPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 42),
    _CmmTransFrontPanelPortNumber_Type()
)
cmmTransFrontPanelPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFrontPanelPortNumber.setStatus("current")


class _CmmTransXFPextendedidentifier_Type(Bits):
    """Custom type cmmTransXFPextendedidentifier based on Bits"""
    namedValues = NamedValues(
        *(("powerlevel1-1dot5wmax", 0),
          ("powerlevel2-2dot5wmax", 1),
          ("powerlevel3-3dot5wmax", 2),
          ("powerlevel4-over3dot5w", 3),
          ("cdr-none", 4),
          ("tx-refclk-input-notrequired", 5),
          ("cleicode-present", 6),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPextendedidentifier_Type.__name__ = "Bits"
_CmmTransXFPextendedidentifier_Object = MibTableColumn
cmmTransXFPextendedidentifier = _CmmTransXFPextendedidentifier_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 43),
    _CmmTransXFPextendedidentifier_Type()
)
cmmTransXFPextendedidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPextendedidentifier.setStatus("current")


class _CmmTransXFP10GEthCompliance_Type(Bits):
    """Custom type cmmTransXFP10GEthCompliance based on Bits"""
    namedValues = NamedValues(
        *(("xec-10gbase-sr", 0),
          ("xec-10gbase-lr", 1),
          ("xec-10gbase-er", 2),
          ("xec-10gbase-lrm", 3),
          ("xec-10gbase-sw", 4),
          ("xec-10gbase-lw", 5),
          ("xec-10gbase-ew", 6),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFP10GEthCompliance_Type.__name__ = "Bits"
_CmmTransXFP10GEthCompliance_Object = MibTableColumn
cmmTransXFP10GEthCompliance = _CmmTransXFP10GEthCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 44),
    _CmmTransXFP10GEthCompliance_Type()
)
cmmTransXFP10GEthCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFP10GEthCompliance.setStatus("current")


class _CmmTransXFP10GFiberChnCompliance_Type(Bits):
    """Custom type cmmTransXFP10GFiberChnCompliance based on Bits"""
    namedValues = NamedValues(
        *(("xfcc-1200-mx-sn-I", 0),
          ("xfcc-1200-sm-ll-l", 1),
          ("xfcc-exended-reach-1550nm", 2),
          ("xfcc-exen-reach-1300nm-fp", 3),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFP10GFiberChnCompliance_Type.__name__ = "Bits"
_CmmTransXFP10GFiberChnCompliance_Object = MibTableColumn
cmmTransXFP10GFiberChnCompliance = _CmmTransXFP10GFiberChnCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 45),
    _CmmTransXFP10GFiberChnCompliance_Type()
)
cmmTransXFP10GFiberChnCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFP10GFiberChnCompliance.setStatus("current")


class _CmmTransXFP10GCopperLinksRsvd_Type(Bits):
    """Custom type cmmTransXFP10GCopperLinksRsvd based on Bits"""
    namedValues = NamedValues(
        *(("xcl-rsvd", 0),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFP10GCopperLinksRsvd_Type.__name__ = "Bits"
_CmmTransXFP10GCopperLinksRsvd_Object = MibTableColumn
cmmTransXFP10GCopperLinksRsvd = _CmmTransXFP10GCopperLinksRsvd_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 46),
    _CmmTransXFP10GCopperLinksRsvd_Type()
)
cmmTransXFP10GCopperLinksRsvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFP10GCopperLinksRsvd.setStatus("current")


class _CmmTransXFPLowerSpeedLinks_Type(Bits):
    """Custom type cmmTransXFPLowerSpeedLinks based on Bits"""
    namedValues = NamedValues(
        *(("xlsl-1000base-sx", 0),
          ("xlsl-1000base-lx", 1),
          ("xlsl-2xfc-mmf", 2),
          ("xlsl-2xfc-smf", 3),
          ("xlsl-oc48-sr", 4),
          ("xlsl-oc48-ir", 5),
          ("xlsl-oc48-lr", 6),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPLowerSpeedLinks_Type.__name__ = "Bits"
_CmmTransXFPLowerSpeedLinks_Object = MibTableColumn
cmmTransXFPLowerSpeedLinks = _CmmTransXFPLowerSpeedLinks_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 47),
    _CmmTransXFPLowerSpeedLinks_Type()
)
cmmTransXFPLowerSpeedLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPLowerSpeedLinks.setStatus("current")


class _CmmTransXFPSonetInterconnect_Type(Bits):
    """Custom type cmmTransXFPSonetInterconnect based on Bits"""
    namedValues = NamedValues(
        *(("xsi-i-64-lr", 0),
          ("xsi-i-64-l", 1),
          ("xsi-i-64-2r", 2),
          ("xsi-i-64-2", 3),
          ("xsi-i-64-3", 4),
          ("xsi-i-64-5", 5),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPSonetInterconnect_Type.__name__ = "Bits"
_CmmTransXFPSonetInterconnect_Object = MibTableColumn
cmmTransXFPSonetInterconnect = _CmmTransXFPSonetInterconnect_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 48),
    _CmmTransXFPSonetInterconnect_Type()
)
cmmTransXFPSonetInterconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPSonetInterconnect.setStatus("current")


class _CmmTransXFPSonetShortHaul_Type(Bits):
    """Custom type cmmTransXFPSonetShortHaul based on Bits"""
    namedValues = NamedValues(
        *(("xssh-s-64-l", 0),
          ("xssh-s-64-2a", 1),
          ("xssh-s-64-2b", 2),
          ("xssh-s-64-3a", 3),
          ("xssh-s-64-3b", 4),
          ("xssh-s-64-5a", 5),
          ("xssh-s-64-5b", 6),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPSonetShortHaul_Type.__name__ = "Bits"
_CmmTransXFPSonetShortHaul_Object = MibTableColumn
cmmTransXFPSonetShortHaul = _CmmTransXFPSonetShortHaul_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 49),
    _CmmTransXFPSonetShortHaul_Type()
)
cmmTransXFPSonetShortHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPSonetShortHaul.setStatus("current")


class _CmmTransXFPSonetLongHaul_Type(Bits):
    """Custom type cmmTransXFPSonetLongHaul based on Bits"""
    namedValues = NamedValues(
        *(("xslh-l-64-l", 0),
          ("xslh-l-64-2a", 1),
          ("xslh-l-64-2b", 2),
          ("xslh-l-64-2c", 3),
          ("xslh-l-64-3", 4),
          ("xlsh-l-g959-1-p1l1-2d2", 5),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPSonetLongHaul_Type.__name__ = "Bits"
_CmmTransXFPSonetLongHaul_Object = MibTableColumn
cmmTransXFPSonetLongHaul = _CmmTransXFPSonetLongHaul_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 50),
    _CmmTransXFPSonetLongHaul_Type()
)
cmmTransXFPSonetLongHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPSonetLongHaul.setStatus("current")


class _CmmTransXFPSonetVeryLongHaul_Type(Bits):
    """Custom type cmmTransXFPSonetVeryLongHaul based on Bits"""
    namedValues = NamedValues(
        *(("xsvh-v-64-2a", 0),
          ("xsvh-v-64-2b", 1),
          ("xsvh-v-64-3", 2),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPSonetVeryLongHaul_Type.__name__ = "Bits"
_CmmTransXFPSonetVeryLongHaul_Object = MibTableColumn
cmmTransXFPSonetVeryLongHaul = _CmmTransXFPSonetVeryLongHaul_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 51),
    _CmmTransXFPSonetVeryLongHaul_Type()
)
cmmTransXFPSonetVeryLongHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPSonetVeryLongHaul.setStatus("current")


class _CmmTransXFPOptionsImp_Type(Bits):
    """Custom type cmmTransXFPOptionsImp based on Bits"""
    namedValues = NamedValues(
        *(("xfp-vps", 0),
          ("xfp-tx-disable", 1),
          ("xfp-p-down", 2),
          ("xfp-vps-lv", 3),
          ("xfp-vps-bypass", 4),
          ("xfp-active-fec", 5),
          ("xfp-wavelength-tunability", 6),
          ("xfp-cmu", 7),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPOptionsImp_Type.__name__ = "Bits"
_CmmTransXFPOptionsImp_Object = MibTableColumn
cmmTransXFPOptionsImp = _CmmTransXFPOptionsImp_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 52),
    _CmmTransXFPOptionsImp_Type()
)
cmmTransXFPOptionsImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPOptionsImp.setStatus("current")


class _CmmTransXFPVoltageAuxMonitor_Type(Bits):
    """Custom type cmmTransXFPVoltageAuxMonitor based on Bits"""
    namedValues = NamedValues(
        *(("xfp-vcc-5", 0),
          ("xfp-vcc-3", 1),
          ("xfp-vcc-2", 2),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPVoltageAuxMonitor_Type.__name__ = "Bits"
_CmmTransXFPVoltageAuxMonitor_Object = MibTableColumn
cmmTransXFPVoltageAuxMonitor = _CmmTransXFPVoltageAuxMonitor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 53),
    _CmmTransXFPVoltageAuxMonitor_Type()
)
cmmTransXFPVoltageAuxMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPVoltageAuxMonitor.setStatus("current")


class _CmmTransXFPEncoding_Type(Bits):
    """Custom type cmmTransXFPEncoding based on Bits"""
    namedValues = NamedValues(
        *(("enc-rsvd0", 0),
          ("enc-rsvd1", 1),
          ("enc-rsvd2", 2),
          ("enc-rz", 3),
          ("enc-nrz", 4),
          ("enc-sonet-scrambled", 5),
          ("enc-8b10b", 6),
          ("enc-64b66b", 7),
          ("unavailable", 30),
          ("not-applicable", 31))
    )

_CmmTransXFPEncoding_Type.__name__ = "Bits"
_CmmTransXFPEncoding_Object = MibTableColumn
cmmTransXFPEncoding = _CmmTransXFPEncoding_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 54),
    _CmmTransXFPEncoding_Type()
)
cmmTransXFPEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPEncoding.setStatus("current")
_CmmTransWavelength_Type = Integer32
_CmmTransWavelength_Object = MibTableColumn
cmmTransWavelength = _CmmTransWavelength_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 55),
    _CmmTransWavelength_Type()
)
cmmTransWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransWavelength.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransWavelength.setUnits("0.001 nm")
_CmmTransChannelNumber_Type = Integer32
_CmmTransChannelNumber_Object = MibTableColumn
cmmTransChannelNumber = _CmmTransChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 56),
    _CmmTransChannelNumber_Type()
)
cmmTransChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransChannelNumber.setStatus("current")
_CmmTransGridSpacing_Type = Integer32
_CmmTransGridSpacing_Object = MibTableColumn
cmmTransGridSpacing = _CmmTransGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 57),
    _CmmTransGridSpacing_Type()
)
cmmTransGridSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransGridSpacing.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransGridSpacing.setUnits("0.01 GHz")
_CmmTransLaserFirstFrequency_Type = Integer32
_CmmTransLaserFirstFrequency_Object = MibTableColumn
cmmTransLaserFirstFrequency = _CmmTransLaserFirstFrequency_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 58),
    _CmmTransLaserFirstFrequency_Type()
)
cmmTransLaserFirstFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserFirstFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserFirstFrequency.setUnits("0.01 GHz")
_CmmTransLaserLastFrequency_Type = Integer32
_CmmTransLaserLastFrequency_Object = MibTableColumn
cmmTransLaserLastFrequency = _CmmTransLaserLastFrequency_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 59),
    _CmmTransLaserLastFrequency_Type()
)
cmmTransLaserLastFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserLastFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserLastFrequency.setUnits("0.01 GHz")
_CmmTransDDMTable_Object = MibTable
cmmTransDDMTable = _CmmTransDDMTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cmmTransDDMTable.setStatus("current")
_CmmTransDDMEntry_Object = MibTableRow
cmmTransDDMEntry = _CmmTransDDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1)
)
cmmTransDDMEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
)
if mibBuilder.loadTexts:
    cmmTransDDMEntry.setStatus("current")


class _CmmTransChannelIndex_Type(Integer32):
    """Custom type cmmTransChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmTransChannelIndex_Type.__name__ = "Integer32"
_CmmTransChannelIndex_Object = MibTableColumn
cmmTransChannelIndex = _CmmTransChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 1),
    _CmmTransChannelIndex_Type()
)
cmmTransChannelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmTransChannelIndex.setStatus("current")
_CmmTransTemperature_Type = Integer32
_CmmTransTemperature_Object = MibTableColumn
cmmTransTemperature = _CmmTransTemperature_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 2),
    _CmmTransTemperature_Type()
)
cmmTransTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTemperature.setUnits("0.01 C")
_CmmTransTempAlertThresholdMin_Type = Integer32
_CmmTransTempAlertThresholdMin_Object = MibTableColumn
cmmTransTempAlertThresholdMin = _CmmTransTempAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 3),
    _CmmTransTempAlertThresholdMin_Type()
)
cmmTransTempAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMin.setUnits("0.01 C")
_CmmTransTempAlertThresholdMax_Type = Integer32
_CmmTransTempAlertThresholdMax_Object = MibTableColumn
cmmTransTempAlertThresholdMax = _CmmTransTempAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 4),
    _CmmTransTempAlertThresholdMax_Type()
)
cmmTransTempAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMax.setUnits("0.01 C")
_CmmTransTempCriticalThresholdMin_Type = Integer32
_CmmTransTempCriticalThresholdMin_Object = MibTableColumn
cmmTransTempCriticalThresholdMin = _CmmTransTempCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 5),
    _CmmTransTempCriticalThresholdMin_Type()
)
cmmTransTempCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMin.setUnits("0.01 C")
_CmmTransTempCriticalThresholdMax_Type = Integer32
_CmmTransTempCriticalThresholdMax_Object = MibTableColumn
cmmTransTempCriticalThresholdMax = _CmmTransTempCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 6),
    _CmmTransTempCriticalThresholdMax_Type()
)
cmmTransTempCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMax.setUnits("0.01 C")
_CmmTransVoltage_Type = Integer32
_CmmTransVoltage_Object = MibTableColumn
cmmTransVoltage = _CmmTransVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 7),
    _CmmTransVoltage_Type()
)
cmmTransVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltage.setUnits("0.001 V")
_CmmTransVoltAlertThresholdMin_Type = Integer32
_CmmTransVoltAlertThresholdMin_Object = MibTableColumn
cmmTransVoltAlertThresholdMin = _CmmTransVoltAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 8),
    _CmmTransVoltAlertThresholdMin_Type()
)
cmmTransVoltAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMin.setUnits("0.001 V")
_CmmTransVoltAlertThresholdMax_Type = Integer32
_CmmTransVoltAlertThresholdMax_Object = MibTableColumn
cmmTransVoltAlertThresholdMax = _CmmTransVoltAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 9),
    _CmmTransVoltAlertThresholdMax_Type()
)
cmmTransVoltAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMax.setUnits("0.001 V")
_CmmTransVoltCriticalThresholdMin_Type = Integer32
_CmmTransVoltCriticalThresholdMin_Object = MibTableColumn
cmmTransVoltCriticalThresholdMin = _CmmTransVoltCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 10),
    _CmmTransVoltCriticalThresholdMin_Type()
)
cmmTransVoltCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMin.setUnits("0.001 V")
_CmmTransVoltCriticalThresholdMax_Type = Integer32
_CmmTransVoltCriticalThresholdMax_Object = MibTableColumn
cmmTransVoltCriticalThresholdMax = _CmmTransVoltCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 11),
    _CmmTransVoltCriticalThresholdMax_Type()
)
cmmTransVoltCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMax.setUnits("0.001 V")
_CmmTransLaserBiasCurrent_Type = Integer32
_CmmTransLaserBiasCurrent_Object = MibTableColumn
cmmTransLaserBiasCurrent = _CmmTransLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 12),
    _CmmTransLaserBiasCurrent_Type()
)
cmmTransLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrent.setUnits("0.001 mA")
_CmmTransLaserBiasCurrAlertThresholdMin_Type = Integer32
_CmmTransLaserBiasCurrAlertThresholdMin_Object = MibTableColumn
cmmTransLaserBiasCurrAlertThresholdMin = _CmmTransLaserBiasCurrAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 13),
    _CmmTransLaserBiasCurrAlertThresholdMin_Type()
)
cmmTransLaserBiasCurrAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMin.setUnits("0.001 mA")
_CmmTransLaserBiasCurrAlertThresholdMax_Type = Integer32
_CmmTransLaserBiasCurrAlertThresholdMax_Object = MibTableColumn
cmmTransLaserBiasCurrAlertThresholdMax = _CmmTransLaserBiasCurrAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 14),
    _CmmTransLaserBiasCurrAlertThresholdMax_Type()
)
cmmTransLaserBiasCurrAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMax.setUnits("0.001 mA")
_CmmTransLaserBiasCurrCriticalThresholdMin_Type = Integer32
_CmmTransLaserBiasCurrCriticalThresholdMin_Object = MibTableColumn
cmmTransLaserBiasCurrCriticalThresholdMin = _CmmTransLaserBiasCurrCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 15),
    _CmmTransLaserBiasCurrCriticalThresholdMin_Type()
)
cmmTransLaserBiasCurrCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMin.setUnits("0.001 mA")
_CmmTransLaserBiasCurrCriticalThresholdMax_Type = Integer32
_CmmTransLaserBiasCurrCriticalThresholdMax_Object = MibTableColumn
cmmTransLaserBiasCurrCriticalThresholdMax = _CmmTransLaserBiasCurrCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 16),
    _CmmTransLaserBiasCurrCriticalThresholdMax_Type()
)
cmmTransLaserBiasCurrCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMax.setUnits("0.001 mA")
_CmmTransTxPower_Type = Integer32
_CmmTransTxPower_Object = MibTableColumn
cmmTransTxPower = _CmmTransTxPower_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 17),
    _CmmTransTxPower_Type()
)
cmmTransTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPower.setUnits("0.001 dBm")
_CmmTransTxPowerAlertThresholdMin_Type = Integer32
_CmmTransTxPowerAlertThresholdMin_Object = MibTableColumn
cmmTransTxPowerAlertThresholdMin = _CmmTransTxPowerAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 18),
    _CmmTransTxPowerAlertThresholdMin_Type()
)
cmmTransTxPowerAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMin.setUnits("0.001 dBm")
_CmmTransTxPowerAlertThresholdMax_Type = Integer32
_CmmTransTxPowerAlertThresholdMax_Object = MibTableColumn
cmmTransTxPowerAlertThresholdMax = _CmmTransTxPowerAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 19),
    _CmmTransTxPowerAlertThresholdMax_Type()
)
cmmTransTxPowerAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMax.setUnits("0.001 dBm")
_CmmTransTxPowerCriticalThresholdMin_Type = Integer32
_CmmTransTxPowerCriticalThresholdMin_Object = MibTableColumn
cmmTransTxPowerCriticalThresholdMin = _CmmTransTxPowerCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 20),
    _CmmTransTxPowerCriticalThresholdMin_Type()
)
cmmTransTxPowerCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMin.setUnits("0.001 dBm")
_CmmTransTxPowerCriticalThresholdMax_Type = Integer32
_CmmTransTxPowerCriticalThresholdMax_Object = MibTableColumn
cmmTransTxPowerCriticalThresholdMax = _CmmTransTxPowerCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 21),
    _CmmTransTxPowerCriticalThresholdMax_Type()
)
cmmTransTxPowerCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMax.setUnits("0.001 dBm")
_CmmTransRxPower_Type = Integer32
_CmmTransRxPower_Object = MibTableColumn
cmmTransRxPower = _CmmTransRxPower_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 22),
    _CmmTransRxPower_Type()
)
cmmTransRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPower.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPower.setUnits("0.001 dBm")
_CmmTransRxPowerAlertThresholdMin_Type = Integer32
_CmmTransRxPowerAlertThresholdMin_Object = MibTableColumn
cmmTransRxPowerAlertThresholdMin = _CmmTransRxPowerAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 23),
    _CmmTransRxPowerAlertThresholdMin_Type()
)
cmmTransRxPowerAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMin.setUnits("0.001 dBm")
_CmmTransRxPowerAlertThresholdMax_Type = Integer32
_CmmTransRxPowerAlertThresholdMax_Object = MibTableColumn
cmmTransRxPowerAlertThresholdMax = _CmmTransRxPowerAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 24),
    _CmmTransRxPowerAlertThresholdMax_Type()
)
cmmTransRxPowerAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMax.setUnits("0.001 dBm")
_CmmTransRxPowerCriticalThresholdMin_Type = Integer32
_CmmTransRxPowerCriticalThresholdMin_Object = MibTableColumn
cmmTransRxPowerCriticalThresholdMin = _CmmTransRxPowerCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 25),
    _CmmTransRxPowerCriticalThresholdMin_Type()
)
cmmTransRxPowerCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMin.setUnits("0.001 dBm")
_CmmTransRxPowerCriticalThresholdMax_Type = Integer32
_CmmTransRxPowerCriticalThresholdMax_Object = MibTableColumn
cmmTransRxPowerCriticalThresholdMax = _CmmTransRxPowerCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 26),
    _CmmTransRxPowerCriticalThresholdMax_Type()
)
cmmTransRxPowerCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMax.setUnits("0.001 dBm")


class _CmmTransTxPowerSupported_Type(Integer32):
    """Custom type cmmTransTxPowerSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("supported", 1),
          ("unsupported", 2))
    )


_CmmTransTxPowerSupported_Type.__name__ = "Integer32"
_CmmTransTxPowerSupported_Object = MibTableColumn
cmmTransTxPowerSupported = _CmmTransTxPowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 27),
    _CmmTransTxPowerSupported_Type()
)
cmmTransTxPowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerSupported.setStatus("current")


class _CmmTransRxPowerSupported_Type(Integer32):
    """Custom type cmmTransRxPowerSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("supported", 1),
          ("unsupported", 2))
    )


_CmmTransRxPowerSupported_Type.__name__ = "Integer32"
_CmmTransRxPowerSupported_Object = MibTableColumn
cmmTransRxPowerSupported = _CmmTransRxPowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 28),
    _CmmTransRxPowerSupported_Type()
)
cmmTransRxPowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerSupported.setStatus("current")


class _CmmTransDDMStatus_Type(Integer32):
    """Custom type cmmTransDDMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("active", 1),
          ("activeunsupported", 2),
          ("inactive", 3),
          ("inactiveunsupported", 4))
    )


_CmmTransDDMStatus_Type.__name__ = "Integer32"
_CmmTransDDMStatus_Object = MibTableColumn
cmmTransDDMStatus = _CmmTransDDMStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 29),
    _CmmTransDDMStatus_Type()
)
cmmTransDDMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransDDMStatus.setStatus("current")


class _CmmTransTxState_Type(Integer32):
    """Custom type cmmTransTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("enable", 1),
          ("disable", 2))
    )


_CmmTransTxState_Type.__name__ = "Integer32"
_CmmTransTxState_Object = MibTableColumn
cmmTransTxState = _CmmTransTxState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 30),
    _CmmTransTxState_Type()
)
cmmTransTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxState.setStatus("current")


class _CmmTransRxLosState_Type(Integer32):
    """Custom type cmmTransRxLosState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("enable", 1),
          ("disable", 2))
    )


_CmmTransRxLosState_Type.__name__ = "Integer32"
_CmmTransRxLosState_Object = MibTableColumn
cmmTransRxLosState = _CmmTransRxLosState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 31),
    _CmmTransRxLosState_Type()
)
cmmTransRxLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxLosState.setStatus("current")


class _CmmTransTxLosState_Type(Integer32):
    """Custom type cmmTransTxLosState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("enable", 1),
          ("disable", 2))
    )


_CmmTransTxLosState_Type.__name__ = "Integer32"
_CmmTransTxLosState_Object = MibTableColumn
cmmTransTxLosState = _CmmTransTxLosState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 32),
    _CmmTransTxLosState_Type()
)
cmmTransTxLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxLosState.setStatus("current")


class _CmmTransResetState_Type(Integer32):
    """Custom type cmmTransResetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("normal", 1),
          ("reset", 2))
    )


_CmmTransResetState_Type.__name__ = "Integer32"
_CmmTransResetState_Object = MibTableColumn
cmmTransResetState = _CmmTransResetState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 33),
    _CmmTransResetState_Type()
)
cmmTransResetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransResetState.setStatus("current")


class _CmmTransPowerMode_Type(Integer32):
    """Custom type cmmTransPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("low", 1),
          ("high", 2))
    )


_CmmTransPowerMode_Type.__name__ = "Integer32"
_CmmTransPowerMode_Object = MibTableColumn
cmmTransPowerMode = _CmmTransPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 34),
    _CmmTransPowerMode_Type()
)
cmmTransPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPowerMode.setStatus("current")
_CmmTransXFPVoltage2_Type = Integer32
_CmmTransXFPVoltage2_Object = MibTableColumn
cmmTransXFPVoltage2 = _CmmTransXFPVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 35),
    _CmmTransXFPVoltage2_Type()
)
cmmTransXFPVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPVoltage2.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransXFPVoltage2.setUnits("0.001 V")
_CmmTransXFPVolt2AlertThresholdMin_Type = Integer32
_CmmTransXFPVolt2AlertThresholdMin_Object = MibTableColumn
cmmTransXFPVolt2AlertThresholdMin = _CmmTransXFPVolt2AlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 36),
    _CmmTransXFPVolt2AlertThresholdMin_Type()
)
cmmTransXFPVolt2AlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2AlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2AlertThresholdMin.setUnits("0.001 V")
_CmmTransXFPVolt2AlertThresholdMax_Type = Integer32
_CmmTransXFPVolt2AlertThresholdMax_Object = MibTableColumn
cmmTransXFPVolt2AlertThresholdMax = _CmmTransXFPVolt2AlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 37),
    _CmmTransXFPVolt2AlertThresholdMax_Type()
)
cmmTransXFPVolt2AlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2AlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2AlertThresholdMax.setUnits("0.001 V")
_CmmTransXFPVolt2CriticalThresholdMin_Type = Integer32
_CmmTransXFPVolt2CriticalThresholdMin_Object = MibTableColumn
cmmTransXFPVolt2CriticalThresholdMin = _CmmTransXFPVolt2CriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 38),
    _CmmTransXFPVolt2CriticalThresholdMin_Type()
)
cmmTransXFPVolt2CriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2CriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2CriticalThresholdMin.setUnits("0.001 V")
_CmmTransXFPVolt2CriticalThresholdMax_Type = Integer32
_CmmTransXFPVolt2CriticalThresholdMax_Object = MibTableColumn
cmmTransXFPVolt2CriticalThresholdMax = _CmmTransXFPVolt2CriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 39),
    _CmmTransXFPVolt2CriticalThresholdMax_Type()
)
cmmTransXFPVolt2CriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2CriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransXFPVolt2CriticalThresholdMax.setUnits("0.001 V")
_CmmTransFrequencyError_Type = Integer32
_CmmTransFrequencyError_Object = MibTableColumn
cmmTransFrequencyError = _CmmTransFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 40),
    _CmmTransFrequencyError_Type()
)
cmmTransFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransFrequencyError.setUnits("0.01 GHZ")
_CmmTransFrequencyErrorAlertThresholdMin_Type = Integer32
_CmmTransFrequencyErrorAlertThresholdMin_Object = MibTableColumn
cmmTransFrequencyErrorAlertThresholdMin = _CmmTransFrequencyErrorAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 41),
    _CmmTransFrequencyErrorAlertThresholdMin_Type()
)
cmmTransFrequencyErrorAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorAlertThresholdMin.setUnits("0.01 GHz")
_CmmTransFrequencyErrorAlertThresholdMax_Type = Integer32
_CmmTransFrequencyErrorAlertThresholdMax_Object = MibTableColumn
cmmTransFrequencyErrorAlertThresholdMax = _CmmTransFrequencyErrorAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 42),
    _CmmTransFrequencyErrorAlertThresholdMax_Type()
)
cmmTransFrequencyErrorAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorAlertThresholdMax.setUnits("0.01 GHz")
_CmmTransFrequencyErrorCriticalThresholdMin_Type = Integer32
_CmmTransFrequencyErrorCriticalThresholdMin_Object = MibTableColumn
cmmTransFrequencyErrorCriticalThresholdMin = _CmmTransFrequencyErrorCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 43),
    _CmmTransFrequencyErrorCriticalThresholdMin_Type()
)
cmmTransFrequencyErrorCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorCriticalThresholdMin.setUnits("0.01 GHz")
_CmmTransFrequencyErrorCriticalThresholdMax_Type = Integer32
_CmmTransFrequencyErrorCriticalThresholdMax_Object = MibTableColumn
cmmTransFrequencyErrorCriticalThresholdMax = _CmmTransFrequencyErrorCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 44),
    _CmmTransFrequencyErrorCriticalThresholdMax_Type()
)
cmmTransFrequencyErrorCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorCriticalThresholdMax.setUnits("0.01 GHz")
_CmmTransWavelengthError_Type = Integer32
_CmmTransWavelengthError_Object = MibTableColumn
cmmTransWavelengthError = _CmmTransWavelengthError_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 45),
    _CmmTransWavelengthError_Type()
)
cmmTransWavelengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransWavelengthError.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransWavelengthError.setUnits("0.00001 nm")
_CmmTransWavelengthErrorAlertThresholdMin_Type = Integer32
_CmmTransWavelengthErrorAlertThresholdMin_Object = MibTableColumn
cmmTransWavelengthErrorAlertThresholdMin = _CmmTransWavelengthErrorAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 46),
    _CmmTransWavelengthErrorAlertThresholdMin_Type()
)
cmmTransWavelengthErrorAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorAlertThresholdMin.setUnits("0.00001 nm")
_CmmTransWavelengthErrorAlertThresholdMax_Type = Integer32
_CmmTransWavelengthErrorAlertThresholdMax_Object = MibTableColumn
cmmTransWavelengthErrorAlertThresholdMax = _CmmTransWavelengthErrorAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 47),
    _CmmTransWavelengthErrorAlertThresholdMax_Type()
)
cmmTransWavelengthErrorAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorAlertThresholdMax.setUnits("0.00001 nm")
_CmmTransWavelengthErrorCriticalThresholdMin_Type = Integer32
_CmmTransWavelengthErrorCriticalThresholdMin_Object = MibTableColumn
cmmTransWavelengthErrorCriticalThresholdMin = _CmmTransWavelengthErrorCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 48),
    _CmmTransWavelengthErrorCriticalThresholdMin_Type()
)
cmmTransWavelengthErrorCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorCriticalThresholdMin.setUnits("0.00001 nm")
_CmmTransWavelengthErrorCriticalThresholdMax_Type = Integer32
_CmmTransWavelengthErrorCriticalThresholdMax_Object = MibTableColumn
cmmTransWavelengthErrorCriticalThresholdMax = _CmmTransWavelengthErrorCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 49),
    _CmmTransWavelengthErrorCriticalThresholdMax_Type()
)
cmmTransWavelengthErrorCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorCriticalThresholdMax.setUnits("0.00001 nm")


class _CmmTransCurrentStatus_Type(Bits):
    """Custom type cmmTransCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("tx-tune", 0),
          ("wavelength-unlocked", 1),
          ("tec-fault", 2),
          ("reserved", 4))
    )

_CmmTransCurrentStatus_Type.__name__ = "Bits"
_CmmTransCurrentStatus_Object = MibTableColumn
cmmTransCurrentStatus = _CmmTransCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 50),
    _CmmTransCurrentStatus_Type()
)
cmmTransCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransCurrentStatus.setStatus("current")
_CmmSysRamTable_Object = MibTable
cmmSysRamTable = _CmmSysRamTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cmmSysRamTable.setStatus("current")
_CmmSysRamEntry_Object = MibTableRow
cmmSysRamEntry = _CmmSysRamEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1)
)
cmmSysRamEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysRamEntry.setStatus("current")
_CmmSysRamTotalMem_Type = Integer32
_CmmSysRamTotalMem_Object = MibTableColumn
cmmSysRamTotalMem = _CmmSysRamTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 1),
    _CmmSysRamTotalMem_Type()
)
cmmSysRamTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamTotalMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamTotalMem.setUnits(" MBytes ")
_CmmSysRamUsedMem_Type = Integer32
_CmmSysRamUsedMem_Object = MibTableColumn
cmmSysRamUsedMem = _CmmSysRamUsedMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 2),
    _CmmSysRamUsedMem_Type()
)
cmmSysRamUsedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamUsedMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamUsedMem.setUnits(" % ")
_CmmSysRamFreeMem_Type = Integer32
_CmmSysRamFreeMem_Object = MibTableColumn
cmmSysRamFreeMem = _CmmSysRamFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 3),
    _CmmSysRamFreeMem_Type()
)
cmmSysRamFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamFreeMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamFreeMem.setUnits(" % ")
_CmmSysRamAlertThreshold_Type = Integer32
_CmmSysRamAlertThreshold_Object = MibTableColumn
cmmSysRamAlertThreshold = _CmmSysRamAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 4),
    _CmmSysRamAlertThreshold_Type()
)
cmmSysRamAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamAlertThreshold.setUnits(" % ")
_CmmSysRamCriticalThreshold_Type = Integer32
_CmmSysRamCriticalThreshold_Object = MibTableColumn
cmmSysRamCriticalThreshold = _CmmSysRamCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 5),
    _CmmSysRamCriticalThreshold_Type()
)
cmmSysRamCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamCriticalThreshold.setUnits(" % ")
_CmmStackCpuTable_Object = MibTable
cmmStackCpuTable = _CmmStackCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cmmStackCpuTable.setStatus("current")
_CmmStackCpuEntry_Object = MibTableRow
cmmStackCpuEntry = _CmmStackCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1)
)
cmmStackCpuEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmStackCpuEntry.setStatus("current")
_CmmStackUnitNumCpuProcessor_Type = Integer32
_CmmStackUnitNumCpuProcessor_Object = MibTableColumn
cmmStackUnitNumCpuProcessor = _CmmStackUnitNumCpuProcessor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 1),
    _CmmStackUnitNumCpuProcessor_Type()
)
cmmStackUnitNumCpuProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumCpuProcessor.setStatus("current")
_CmmStackUnitCpuLoad1Min_Type = Integer32
_CmmStackUnitCpuLoad1Min_Object = MibTableColumn
cmmStackUnitCpuLoad1Min = _CmmStackUnitCpuLoad1Min_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 2),
    _CmmStackUnitCpuLoad1Min_Type()
)
cmmStackUnitCpuLoad1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad1Min.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad1Min.setUnits("0.01 %")
_CmmStackUnitCpuLoad5Min_Type = Integer32
_CmmStackUnitCpuLoad5Min_Object = MibTableColumn
cmmStackUnitCpuLoad5Min = _CmmStackUnitCpuLoad5Min_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 3),
    _CmmStackUnitCpuLoad5Min_Type()
)
cmmStackUnitCpuLoad5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad5Min.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad5Min.setUnits("0.01 %")
_CmmStackUnitCpuLoad15Min_Type = Integer32
_CmmStackUnitCpuLoad15Min_Object = MibTableColumn
cmmStackUnitCpuLoad15Min = _CmmStackUnitCpuLoad15Min_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 4),
    _CmmStackUnitCpuLoad15Min_Type()
)
cmmStackUnitCpuLoad15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad15Min.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad15Min.setUnits("0.01 %")
_CmmStackCpuLoad1minCriticalThreshold_Type = Integer32
_CmmStackCpuLoad1minCriticalThreshold_Object = MibTableColumn
cmmStackCpuLoad1minCriticalThreshold = _CmmStackCpuLoad1minCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 5),
    _CmmStackCpuLoad1minCriticalThreshold_Type()
)
cmmStackCpuLoad1minCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minCriticalThreshold.setUnits("0.01 %")
_CmmStackCpuLoad1minAlertThreshold_Type = Integer32
_CmmStackCpuLoad1minAlertThreshold_Object = MibTableColumn
cmmStackCpuLoad1minAlertThreshold = _CmmStackCpuLoad1minAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 6),
    _CmmStackCpuLoad1minAlertThreshold_Type()
)
cmmStackCpuLoad1minAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minAlertThreshold.setUnits("0.01 %")
_CmmStackCpuLoad5minAlertThreshold_Type = Integer32
_CmmStackCpuLoad5minAlertThreshold_Object = MibTableColumn
cmmStackCpuLoad5minAlertThreshold = _CmmStackCpuLoad5minAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 7),
    _CmmStackCpuLoad5minAlertThreshold_Type()
)
cmmStackCpuLoad5minAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad5minAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad5minAlertThreshold.setUnits("0.01 %")
_CmmStackCpuLoad15minAlertThreshold_Type = Integer32
_CmmStackCpuLoad15minAlertThreshold_Object = MibTableColumn
cmmStackCpuLoad15minAlertThreshold = _CmmStackCpuLoad15minAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 8),
    _CmmStackCpuLoad15minAlertThreshold_Type()
)
cmmStackCpuLoad15minAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad15minAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad15minAlertThreshold.setUnits("0.01 %")
_CmmStackUnitCpuUtilization_Type = Integer32
_CmmStackUnitCpuUtilization_Object = MibTableColumn
cmmStackUnitCpuUtilization = _CmmStackUnitCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 9),
    _CmmStackUnitCpuUtilization_Type()
)
cmmStackUnitCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilization.setUnits("0.01 %")
_CmmStackUnitCpuUtilCriticalThreshold_Type = Integer32
_CmmStackUnitCpuUtilCriticalThreshold_Object = MibTableColumn
cmmStackUnitCpuUtilCriticalThreshold = _CmmStackUnitCpuUtilCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 10),
    _CmmStackUnitCpuUtilCriticalThreshold_Type()
)
cmmStackUnitCpuUtilCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilCriticalThreshold.setUnits("0.01 %")
_CmmStackUnitCpuUtilAlertThreshold_Type = Integer32
_CmmStackUnitCpuUtilAlertThreshold_Object = MibTableColumn
cmmStackUnitCpuUtilAlertThreshold = _CmmStackUnitCpuUtilAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 11),
    _CmmStackUnitCpuUtilAlertThreshold_Type()
)
cmmStackUnitCpuUtilAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilAlertThreshold.setUnits("0.01 %")
_CmmSysPowerSupplyTable_Object = MibTable
cmmSysPowerSupplyTable = _CmmSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cmmSysPowerSupplyTable.setStatus("current")
_CmmSysPowerSupplyEntry_Object = MibTableRow
cmmSysPowerSupplyEntry = _CmmSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1)
)
cmmSysPowerSupplyEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
)
if mibBuilder.loadTexts:
    cmmSysPowerSupplyEntry.setStatus("current")


class _CmmSysPSUIndex_Type(Integer32):
    """Custom type cmmSysPSUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmSysPSUIndex_Type.__name__ = "Integer32"
_CmmSysPSUIndex_Object = MibTableColumn
cmmSysPSUIndex = _CmmSysPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 1),
    _CmmSysPSUIndex_Type()
)
cmmSysPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSUIndex.setStatus("current")


class _CmmSysPowerSupplyOperStatus_Type(Integer32):
    """Custom type cmmSysPowerSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("notpresent", 1),
          ("running", 2),
          ("faulty", 3))
    )


_CmmSysPowerSupplyOperStatus_Type.__name__ = "Integer32"
_CmmSysPowerSupplyOperStatus_Object = MibTableColumn
cmmSysPowerSupplyOperStatus = _CmmSysPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 2),
    _CmmSysPowerSupplyOperStatus_Type()
)
cmmSysPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPowerSupplyOperStatus.setStatus("current")


class _CmmSysPowerSupplyType_Type(Integer32):
    """Custom type cmmSysPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("ac-normal", 1),
          ("ac-reverse", 2),
          ("dc-normal", 3),
          ("dc-reverse", 4))
    )


_CmmSysPowerSupplyType_Type.__name__ = "Integer32"
_CmmSysPowerSupplyType_Object = MibTableColumn
cmmSysPowerSupplyType = _CmmSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 3),
    _CmmSysPowerSupplyType_Type()
)
cmmSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPowerSupplyType.setStatus("current")


class _CmmSysHotSwapStat_Type(Integer32):
    """Custom type cmmSysHotSwapStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysHotSwapStat_Type.__name__ = "Integer32"
_CmmSysHotSwapStat_Object = MibTableColumn
cmmSysHotSwapStat = _CmmSysHotSwapStat_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 4),
    _CmmSysHotSwapStat_Type()
)
cmmSysHotSwapStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHotSwapStat.setStatus("current")
_CmmSysPSConsumption_Type = Integer32
_CmmSysPSConsumption_Object = MibTableColumn
cmmSysPSConsumption = _CmmSysPSConsumption_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 5),
    _CmmSysPSConsumption_Type()
)
cmmSysPSConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSConsumption.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSConsumption.setUnits("0.01 W")
_CmmSysInputPower_Type = Integer32
_CmmSysInputPower_Object = MibTableColumn
cmmSysInputPower = _CmmSysInputPower_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 6),
    _CmmSysInputPower_Type()
)
cmmSysInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPower.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPower.setUnits("0.01 W")
_CmmSysInputVoltage_Type = Integer32
_CmmSysInputVoltage_Object = MibTableColumn
cmmSysInputVoltage = _CmmSysInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 7),
    _CmmSysInputVoltage_Type()
)
cmmSysInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltage.setUnits("0.01 V")
_CmmSysOutputVoltage_Type = Integer32
_CmmSysOutputVoltage_Object = MibTableColumn
cmmSysOutputVoltage = _CmmSysOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 8),
    _CmmSysOutputVoltage_Type()
)
cmmSysOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltage.setUnits("0.01 V")
_CmmSysInputCurrent_Type = Integer32
_CmmSysInputCurrent_Object = MibTableColumn
cmmSysInputCurrent = _CmmSysInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 9),
    _CmmSysInputCurrent_Type()
)
cmmSysInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrent.setUnits("0.01 A")
_CmmSysOutputCurrent_Type = Integer32
_CmmSysOutputCurrent_Object = MibTableColumn
cmmSysOutputCurrent = _CmmSysOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 10),
    _CmmSysOutputCurrent_Type()
)
cmmSysOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrent.setUnits("0.01 A")
_CmmSysPSTemperature1_Type = Integer32
_CmmSysPSTemperature1_Object = MibTableColumn
cmmSysPSTemperature1 = _CmmSysPSTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 11),
    _CmmSysPSTemperature1_Type()
)
cmmSysPSTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1.setUnits("0.01 C")
_CmmSysPSTemperature2_Type = Integer32
_CmmSysPSTemperature2_Object = MibTableColumn
cmmSysPSTemperature2 = _CmmSysPSTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 12),
    _CmmSysPSTemperature2_Type()
)
cmmSysPSTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2.setUnits("0.01 C")
_CmmSysPSFan1Rpm_Type = Integer32
_CmmSysPSFan1Rpm_Object = MibTableColumn
cmmSysPSFan1Rpm = _CmmSysPSFan1Rpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 13),
    _CmmSysPSFan1Rpm_Type()
)
cmmSysPSFan1Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSFan1Rpm.setStatus("current")
_CmmSysPSFan2Rpm_Type = Integer32
_CmmSysPSFan2Rpm_Object = MibTableColumn
cmmSysPSFan2Rpm = _CmmSysPSFan2Rpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 14),
    _CmmSysPSFan2Rpm_Type()
)
cmmSysPSFan2Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSFan2Rpm.setStatus("current")


class _CmmSysPS12VPg_Type(Integer32):
    """Custom type cmmSysPS12VPg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS12VPg_Type.__name__ = "Integer32"
_CmmSysPS12VPg_Object = MibTableColumn
cmmSysPS12VPg = _CmmSysPS12VPg_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 15),
    _CmmSysPS12VPg_Type()
)
cmmSysPS12VPg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS12VPg.setStatus("current")


class _CmmSysPSAcCritical_Type(Integer32):
    """Custom type cmmSysPSAcCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPSAcCritical_Type.__name__ = "Integer32"
_CmmSysPSAcCritical_Object = MibTableColumn
cmmSysPSAcCritical = _CmmSysPSAcCritical_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 16),
    _CmmSysPSAcCritical_Type()
)
cmmSysPSAcCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSAcCritical.setStatus("current")


class _CmmSysPSParamsSupport_Type(Bits):
    """Custom type cmmSysPSParamsSupport based on Bits"""
    namedValues = NamedValues(
        *(("volt-in", 0),
          ("volt-out", 1),
          ("curr-in", 2),
          ("curr-out", 3),
          ("power-in", 4),
          ("power-out", 5),
          ("temp-1", 6),
          ("temp-2", 7),
          ("fan-1", 8),
          ("fan-2", 9),
          ("not-applicable", 31))
    )

_CmmSysPSParamsSupport_Type.__name__ = "Bits"
_CmmSysPSParamsSupport_Object = MibTableColumn
cmmSysPSParamsSupport = _CmmSysPSParamsSupport_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 17),
    _CmmSysPSParamsSupport_Type()
)
cmmSysPSParamsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSParamsSupport.setStatus("current")
_CmmSysPSCapacity_Type = Integer32
_CmmSysPSCapacity_Object = MibTableColumn
cmmSysPSCapacity = _CmmSysPSCapacity_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 18),
    _CmmSysPSCapacity_Type()
)
cmmSysPSCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSCapacity.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSCapacity.setUnits("W")
_CmmSysPSConsumptionAlertThresholdMin_Type = Integer32
_CmmSysPSConsumptionAlertThresholdMin_Object = MibTableColumn
cmmSysPSConsumptionAlertThresholdMin = _CmmSysPSConsumptionAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 19),
    _CmmSysPSConsumptionAlertThresholdMin_Type()
)
cmmSysPSConsumptionAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionAlertThresholdMin.setUnits("0.01 W")
_CmmSysPSConsumptionAlertThresholdMax_Type = Integer32
_CmmSysPSConsumptionAlertThresholdMax_Object = MibTableColumn
cmmSysPSConsumptionAlertThresholdMax = _CmmSysPSConsumptionAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 20),
    _CmmSysPSConsumptionAlertThresholdMax_Type()
)
cmmSysPSConsumptionAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionAlertThresholdMax.setUnits("0.01 W")
_CmmSysInputPowerAlertThresholdMin_Type = Integer32
_CmmSysInputPowerAlertThresholdMin_Object = MibTableColumn
cmmSysInputPowerAlertThresholdMin = _CmmSysInputPowerAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 21),
    _CmmSysInputPowerAlertThresholdMin_Type()
)
cmmSysInputPowerAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerAlertThresholdMin.setUnits("0.01 W")
_CmmSysInputPowerAlertThresholdMax_Type = Integer32
_CmmSysInputPowerAlertThresholdMax_Object = MibTableColumn
cmmSysInputPowerAlertThresholdMax = _CmmSysInputPowerAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 22),
    _CmmSysInputPowerAlertThresholdMax_Type()
)
cmmSysInputPowerAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerAlertThresholdMax.setUnits("0.01 W")
_CmmSysInputVoltageAlertThresholdMin_Type = Integer32
_CmmSysInputVoltageAlertThresholdMin_Object = MibTableColumn
cmmSysInputVoltageAlertThresholdMin = _CmmSysInputVoltageAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 23),
    _CmmSysInputVoltageAlertThresholdMin_Type()
)
cmmSysInputVoltageAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageAlertThresholdMin.setUnits("0.01 V")
_CmmSysInputVoltageAlertThresholdMax_Type = Integer32
_CmmSysInputVoltageAlertThresholdMax_Object = MibTableColumn
cmmSysInputVoltageAlertThresholdMax = _CmmSysInputVoltageAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 24),
    _CmmSysInputVoltageAlertThresholdMax_Type()
)
cmmSysInputVoltageAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageAlertThresholdMax.setUnits("0.01 V")
_CmmSysOutputVoltageAlertThresholdMin_Type = Integer32
_CmmSysOutputVoltageAlertThresholdMin_Object = MibTableColumn
cmmSysOutputVoltageAlertThresholdMin = _CmmSysOutputVoltageAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 25),
    _CmmSysOutputVoltageAlertThresholdMin_Type()
)
cmmSysOutputVoltageAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageAlertThresholdMin.setUnits("0.01 V")
_CmmSysOutputVoltageAlertThresholdMax_Type = Integer32
_CmmSysOutputVoltageAlertThresholdMax_Object = MibTableColumn
cmmSysOutputVoltageAlertThresholdMax = _CmmSysOutputVoltageAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 26),
    _CmmSysOutputVoltageAlertThresholdMax_Type()
)
cmmSysOutputVoltageAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageAlertThresholdMax.setUnits("0.01 V")
_CmmSysInputCurrentAlertThresholdMin_Type = Integer32
_CmmSysInputCurrentAlertThresholdMin_Object = MibTableColumn
cmmSysInputCurrentAlertThresholdMin = _CmmSysInputCurrentAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 27),
    _CmmSysInputCurrentAlertThresholdMin_Type()
)
cmmSysInputCurrentAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentAlertThresholdMin.setUnits("0.01 A")
_CmmSysInputCurrentAlertThresholdMax_Type = Integer32
_CmmSysInputCurrentAlertThresholdMax_Object = MibTableColumn
cmmSysInputCurrentAlertThresholdMax = _CmmSysInputCurrentAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 28),
    _CmmSysInputCurrentAlertThresholdMax_Type()
)
cmmSysInputCurrentAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentAlertThresholdMax.setUnits("0.01 A")
_CmmSysOutputCurrentAlertThresholdMin_Type = Integer32
_CmmSysOutputCurrentAlertThresholdMin_Object = MibTableColumn
cmmSysOutputCurrentAlertThresholdMin = _CmmSysOutputCurrentAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 29),
    _CmmSysOutputCurrentAlertThresholdMin_Type()
)
cmmSysOutputCurrentAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentAlertThresholdMin.setUnits("0.01 A")
_CmmSysOutputCurrentAlertThresholdMax_Type = Integer32
_CmmSysOutputCurrentAlertThresholdMax_Object = MibTableColumn
cmmSysOutputCurrentAlertThresholdMax = _CmmSysOutputCurrentAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 30),
    _CmmSysOutputCurrentAlertThresholdMax_Type()
)
cmmSysOutputCurrentAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentAlertThresholdMax.setUnits("0.01 A")
_CmmSysPSTemperature1AlertThresholdMin_Type = Integer32
_CmmSysPSTemperature1AlertThresholdMin_Object = MibTableColumn
cmmSysPSTemperature1AlertThresholdMin = _CmmSysPSTemperature1AlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 31),
    _CmmSysPSTemperature1AlertThresholdMin_Type()
)
cmmSysPSTemperature1AlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1AlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1AlertThresholdMin.setUnits("0.01 C")
_CmmSysPSTemperature1AlertThresholdMax_Type = Integer32
_CmmSysPSTemperature1AlertThresholdMax_Object = MibTableColumn
cmmSysPSTemperature1AlertThresholdMax = _CmmSysPSTemperature1AlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 32),
    _CmmSysPSTemperature1AlertThresholdMax_Type()
)
cmmSysPSTemperature1AlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1AlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1AlertThresholdMax.setUnits("0.01 C")
_CmmSysPSTemperature2AlertThresholdMin_Type = Integer32
_CmmSysPSTemperature2AlertThresholdMin_Object = MibTableColumn
cmmSysPSTemperature2AlertThresholdMin = _CmmSysPSTemperature2AlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 33),
    _CmmSysPSTemperature2AlertThresholdMin_Type()
)
cmmSysPSTemperature2AlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2AlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2AlertThresholdMin.setUnits("0.01 C")
_CmmSysPSTemperature2AlertThresholdMax_Type = Integer32
_CmmSysPSTemperature2AlertThresholdMax_Object = MibTableColumn
cmmSysPSTemperature2AlertThresholdMax = _CmmSysPSTemperature2AlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 34),
    _CmmSysPSTemperature2AlertThresholdMax_Type()
)
cmmSysPSTemperature2AlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2AlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2AlertThresholdMax.setUnits("0.01 C")
_CmmSysPSConsumptionCriticalThresholdMin_Type = Integer32
_CmmSysPSConsumptionCriticalThresholdMin_Object = MibTableColumn
cmmSysPSConsumptionCriticalThresholdMin = _CmmSysPSConsumptionCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 35),
    _CmmSysPSConsumptionCriticalThresholdMin_Type()
)
cmmSysPSConsumptionCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionCriticalThresholdMin.setUnits("0.01 W")
_CmmSysPSConsumptionCriticalThresholdMax_Type = Integer32
_CmmSysPSConsumptionCriticalThresholdMax_Object = MibTableColumn
cmmSysPSConsumptionCriticalThresholdMax = _CmmSysPSConsumptionCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 36),
    _CmmSysPSConsumptionCriticalThresholdMax_Type()
)
cmmSysPSConsumptionCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSConsumptionCriticalThresholdMax.setUnits("0.01 W")
_CmmSysInputPowerCriticalThresholdMin_Type = Integer32
_CmmSysInputPowerCriticalThresholdMin_Object = MibTableColumn
cmmSysInputPowerCriticalThresholdMin = _CmmSysInputPowerCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 37),
    _CmmSysInputPowerCriticalThresholdMin_Type()
)
cmmSysInputPowerCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerCriticalThresholdMin.setUnits("0.01 W")
_CmmSysInputPowerCriticalThresholdMax_Type = Integer32
_CmmSysInputPowerCriticalThresholdMax_Object = MibTableColumn
cmmSysInputPowerCriticalThresholdMax = _CmmSysInputPowerCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 38),
    _CmmSysInputPowerCriticalThresholdMax_Type()
)
cmmSysInputPowerCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerCriticalThresholdMax.setUnits("0.01 W")
_CmmSysInputVoltageCriticalThresholdMin_Type = Integer32
_CmmSysInputVoltageCriticalThresholdMin_Object = MibTableColumn
cmmSysInputVoltageCriticalThresholdMin = _CmmSysInputVoltageCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 39),
    _CmmSysInputVoltageCriticalThresholdMin_Type()
)
cmmSysInputVoltageCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageCriticalThresholdMin.setUnits("0.01 V")
_CmmSysInputVoltageCriticalThresholdMax_Type = Integer32
_CmmSysInputVoltageCriticalThresholdMax_Object = MibTableColumn
cmmSysInputVoltageCriticalThresholdMax = _CmmSysInputVoltageCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 40),
    _CmmSysInputVoltageCriticalThresholdMax_Type()
)
cmmSysInputVoltageCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageCriticalThresholdMax.setUnits("0.01 V")
_CmmSysOutputVoltageCriticalThresholdMin_Type = Integer32
_CmmSysOutputVoltageCriticalThresholdMin_Object = MibTableColumn
cmmSysOutputVoltageCriticalThresholdMin = _CmmSysOutputVoltageCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 41),
    _CmmSysOutputVoltageCriticalThresholdMin_Type()
)
cmmSysOutputVoltageCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageCriticalThresholdMin.setUnits("0.01 V")
_CmmSysOutputVoltageCriticalThresholdMax_Type = Integer32
_CmmSysOutputVoltageCriticalThresholdMax_Object = MibTableColumn
cmmSysOutputVoltageCriticalThresholdMax = _CmmSysOutputVoltageCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 42),
    _CmmSysOutputVoltageCriticalThresholdMax_Type()
)
cmmSysOutputVoltageCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageCriticalThresholdMax.setUnits("0.01 V")
_CmmSysInputCurrentCriticalThresholdMin_Type = Integer32
_CmmSysInputCurrentCriticalThresholdMin_Object = MibTableColumn
cmmSysInputCurrentCriticalThresholdMin = _CmmSysInputCurrentCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 43),
    _CmmSysInputCurrentCriticalThresholdMin_Type()
)
cmmSysInputCurrentCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentCriticalThresholdMin.setUnits("0.01 A")
_CmmSysInputCurrentCriticalThresholdMax_Type = Integer32
_CmmSysInputCurrentCriticalThresholdMax_Object = MibTableColumn
cmmSysInputCurrentCriticalThresholdMax = _CmmSysInputCurrentCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 44),
    _CmmSysInputCurrentCriticalThresholdMax_Type()
)
cmmSysInputCurrentCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentCriticalThresholdMax.setUnits("0.01 A")
_CmmSysOutputCurrentCriticalThresholdMin_Type = Integer32
_CmmSysOutputCurrentCriticalThresholdMin_Object = MibTableColumn
cmmSysOutputCurrentCriticalThresholdMin = _CmmSysOutputCurrentCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 45),
    _CmmSysOutputCurrentCriticalThresholdMin_Type()
)
cmmSysOutputCurrentCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentCriticalThresholdMin.setUnits("0.01 A")
_CmmSysOutputCurrentCriticalThresholdMax_Type = Integer32
_CmmSysOutputCurrentCriticalThresholdMax_Object = MibTableColumn
cmmSysOutputCurrentCriticalThresholdMax = _CmmSysOutputCurrentCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 46),
    _CmmSysOutputCurrentCriticalThresholdMax_Type()
)
cmmSysOutputCurrentCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentCriticalThresholdMax.setUnits("0.01 A")
_CmmSysPSTemperature1CriticalThresholdMin_Type = Integer32
_CmmSysPSTemperature1CriticalThresholdMin_Object = MibTableColumn
cmmSysPSTemperature1CriticalThresholdMin = _CmmSysPSTemperature1CriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 47),
    _CmmSysPSTemperature1CriticalThresholdMin_Type()
)
cmmSysPSTemperature1CriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1CriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1CriticalThresholdMin.setUnits("0.01 C")
_CmmSysPSTemperature1CriticalThresholdMax_Type = Integer32
_CmmSysPSTemperature1CriticalThresholdMax_Object = MibTableColumn
cmmSysPSTemperature1CriticalThresholdMax = _CmmSysPSTemperature1CriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 48),
    _CmmSysPSTemperature1CriticalThresholdMax_Type()
)
cmmSysPSTemperature1CriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1CriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1CriticalThresholdMax.setUnits("0.01 C")
_CmmSysPSTemperature2CriticalThresholdMin_Type = Integer32
_CmmSysPSTemperature2CriticalThresholdMin_Object = MibTableColumn
cmmSysPSTemperature2CriticalThresholdMin = _CmmSysPSTemperature2CriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 49),
    _CmmSysPSTemperature2CriticalThresholdMin_Type()
)
cmmSysPSTemperature2CriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2CriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2CriticalThresholdMin.setUnits("0.01 C")
_CmmSysPSTemperature2CriticalThresholdMax_Type = Integer32
_CmmSysPSTemperature2CriticalThresholdMax_Object = MibTableColumn
cmmSysPSTemperature2CriticalThresholdMax = _CmmSysPSTemperature2CriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 50),
    _CmmSysPSTemperature2CriticalThresholdMax_Type()
)
cmmSysPSTemperature2CriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2CriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2CriticalThresholdMax.setUnits("0.01 C")
_CmmSysInputVoltageOverShutdown_Type = Integer32
_CmmSysInputVoltageOverShutdown_Object = MibTableColumn
cmmSysInputVoltageOverShutdown = _CmmSysInputVoltageOverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 51),
    _CmmSysInputVoltageOverShutdown_Type()
)
cmmSysInputVoltageOverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageOverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageOverShutdown.setUnits("0.01 V")
_CmmSysInputVoltageUnderShutdown_Type = Integer32
_CmmSysInputVoltageUnderShutdown_Object = MibTableColumn
cmmSysInputVoltageUnderShutdown = _CmmSysInputVoltageUnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 52),
    _CmmSysInputVoltageUnderShutdown_Type()
)
cmmSysInputVoltageUnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageUnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageUnderShutdown.setUnits("0.01 V")
_CmmSysInputVoltageOverResume_Type = Integer32
_CmmSysInputVoltageOverResume_Object = MibTableColumn
cmmSysInputVoltageOverResume = _CmmSysInputVoltageOverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 53),
    _CmmSysInputVoltageOverResume_Type()
)
cmmSysInputVoltageOverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageOverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageOverResume.setUnits("0.01 V")
_CmmSysInputVoltageUnderResume_Type = Integer32
_CmmSysInputVoltageUnderResume_Object = MibTableColumn
cmmSysInputVoltageUnderResume = _CmmSysInputVoltageUnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 54),
    _CmmSysInputVoltageUnderResume_Type()
)
cmmSysInputVoltageUnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltageUnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltageUnderResume.setUnits("0.01 V")
_CmmSysOutputVoltageOverShutdown_Type = Integer32
_CmmSysOutputVoltageOverShutdown_Object = MibTableColumn
cmmSysOutputVoltageOverShutdown = _CmmSysOutputVoltageOverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 55),
    _CmmSysOutputVoltageOverShutdown_Type()
)
cmmSysOutputVoltageOverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageOverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageOverShutdown.setUnits("0.01 V")
_CmmSysOutputVoltageUnderShutdown_Type = Integer32
_CmmSysOutputVoltageUnderShutdown_Object = MibTableColumn
cmmSysOutputVoltageUnderShutdown = _CmmSysOutputVoltageUnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 56),
    _CmmSysOutputVoltageUnderShutdown_Type()
)
cmmSysOutputVoltageUnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageUnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageUnderShutdown.setUnits("0.01 V")
_CmmSysOutputVoltageOverResume_Type = Integer32
_CmmSysOutputVoltageOverResume_Object = MibTableColumn
cmmSysOutputVoltageOverResume = _CmmSysOutputVoltageOverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 57),
    _CmmSysOutputVoltageOverResume_Type()
)
cmmSysOutputVoltageOverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageOverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageOverResume.setUnits("0.01 V")
_CmmSysOutputVoltageUnderResume_Type = Integer32
_CmmSysOutputVoltageUnderResume_Object = MibTableColumn
cmmSysOutputVoltageUnderResume = _CmmSysOutputVoltageUnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 58),
    _CmmSysOutputVoltageUnderResume_Type()
)
cmmSysOutputVoltageUnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageUnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltageUnderResume.setUnits("0.01 V")
_CmmSysInputPowerOverShutdown_Type = Integer32
_CmmSysInputPowerOverShutdown_Object = MibTableColumn
cmmSysInputPowerOverShutdown = _CmmSysInputPowerOverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 59),
    _CmmSysInputPowerOverShutdown_Type()
)
cmmSysInputPowerOverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerOverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerOverShutdown.setUnits("0.01 W")
_CmmSysInputPowerUnderShutdown_Type = Integer32
_CmmSysInputPowerUnderShutdown_Object = MibTableColumn
cmmSysInputPowerUnderShutdown = _CmmSysInputPowerUnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 60),
    _CmmSysInputPowerUnderShutdown_Type()
)
cmmSysInputPowerUnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerUnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerUnderShutdown.setUnits("0.01 W")
_CmmSysInputPowerOverResume_Type = Integer32
_CmmSysInputPowerOverResume_Object = MibTableColumn
cmmSysInputPowerOverResume = _CmmSysInputPowerOverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 61),
    _CmmSysInputPowerOverResume_Type()
)
cmmSysInputPowerOverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerOverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerOverResume.setUnits("0.01 W")
_CmmSysInputPowerUnderResume_Type = Integer32
_CmmSysInputPowerUnderResume_Object = MibTableColumn
cmmSysInputPowerUnderResume = _CmmSysInputPowerUnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 62),
    _CmmSysInputPowerUnderResume_Type()
)
cmmSysInputPowerUnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPowerUnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPowerUnderResume.setUnits("0.01 W")
_CmmSysOutputPowerOverShutdown_Type = Integer32
_CmmSysOutputPowerOverShutdown_Object = MibTableColumn
cmmSysOutputPowerOverShutdown = _CmmSysOutputPowerOverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 63),
    _CmmSysOutputPowerOverShutdown_Type()
)
cmmSysOutputPowerOverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputPowerOverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputPowerOverShutdown.setUnits("0.01 W")
_CmmSysOutputPowerUnderShutdown_Type = Integer32
_CmmSysOutputPowerUnderShutdown_Object = MibTableColumn
cmmSysOutputPowerUnderShutdown = _CmmSysOutputPowerUnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 64),
    _CmmSysOutputPowerUnderShutdown_Type()
)
cmmSysOutputPowerUnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputPowerUnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputPowerUnderShutdown.setUnits("0.01 W")
_CmmSysOutputPowerOverResume_Type = Integer32
_CmmSysOutputPowerOverResume_Object = MibTableColumn
cmmSysOutputPowerOverResume = _CmmSysOutputPowerOverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 65),
    _CmmSysOutputPowerOverResume_Type()
)
cmmSysOutputPowerOverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputPowerOverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputPowerOverResume.setUnits("0.01 W")
_CmmSysOutputPowerUnderResume_Type = Integer32
_CmmSysOutputPowerUnderResume_Object = MibTableColumn
cmmSysOutputPowerUnderResume = _CmmSysOutputPowerUnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 66),
    _CmmSysOutputPowerUnderResume_Type()
)
cmmSysOutputPowerUnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputPowerUnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputPowerUnderResume.setUnits("0.01 W")
_CmmSysInputCurrentOverShutdown_Type = Integer32
_CmmSysInputCurrentOverShutdown_Object = MibTableColumn
cmmSysInputCurrentOverShutdown = _CmmSysInputCurrentOverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 67),
    _CmmSysInputCurrentOverShutdown_Type()
)
cmmSysInputCurrentOverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentOverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentOverShutdown.setUnits("0.01 A")
_CmmSysInputCurrentUnderShutdown_Type = Integer32
_CmmSysInputCurrentUnderShutdown_Object = MibTableColumn
cmmSysInputCurrentUnderShutdown = _CmmSysInputCurrentUnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 68),
    _CmmSysInputCurrentUnderShutdown_Type()
)
cmmSysInputCurrentUnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentUnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentUnderShutdown.setUnits("0.01 A")
_CmmSysInputCurrentOverResume_Type = Integer32
_CmmSysInputCurrentOverResume_Object = MibTableColumn
cmmSysInputCurrentOverResume = _CmmSysInputCurrentOverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 69),
    _CmmSysInputCurrentOverResume_Type()
)
cmmSysInputCurrentOverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentOverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentOverResume.setUnits("0.01 A")
_CmmSysInputCurrentUnderResume_Type = Integer32
_CmmSysInputCurrentUnderResume_Object = MibTableColumn
cmmSysInputCurrentUnderResume = _CmmSysInputCurrentUnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 70),
    _CmmSysInputCurrentUnderResume_Type()
)
cmmSysInputCurrentUnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrentUnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrentUnderResume.setUnits("0.01 A")
_CmmSysOutputCurrentOverShutdown_Type = Integer32
_CmmSysOutputCurrentOverShutdown_Object = MibTableColumn
cmmSysOutputCurrentOverShutdown = _CmmSysOutputCurrentOverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 71),
    _CmmSysOutputCurrentOverShutdown_Type()
)
cmmSysOutputCurrentOverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentOverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentOverShutdown.setUnits("0.01 A")
_CmmSysOutputCurrentUnderShutdown_Type = Integer32
_CmmSysOutputCurrentUnderShutdown_Object = MibTableColumn
cmmSysOutputCurrentUnderShutdown = _CmmSysOutputCurrentUnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 72),
    _CmmSysOutputCurrentUnderShutdown_Type()
)
cmmSysOutputCurrentUnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentUnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentUnderShutdown.setUnits("0.01 A")
_CmmSysOutputCurrentOverResume_Type = Integer32
_CmmSysOutputCurrentOverResume_Object = MibTableColumn
cmmSysOutputCurrentOverResume = _CmmSysOutputCurrentOverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 73),
    _CmmSysOutputCurrentOverResume_Type()
)
cmmSysOutputCurrentOverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentOverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentOverResume.setUnits("0.01 A")
_CmmSysOutputCurrentUnderResume_Type = Integer32
_CmmSysOutputCurrentUnderResume_Object = MibTableColumn
cmmSysOutputCurrentUnderResume = _CmmSysOutputCurrentUnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 74),
    _CmmSysOutputCurrentUnderResume_Type()
)
cmmSysOutputCurrentUnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentUnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrentUnderResume.setUnits("0.01 A")
_CmmSysPsuTemperature1OverShutdown_Type = Integer32
_CmmSysPsuTemperature1OverShutdown_Object = MibTableColumn
cmmSysPsuTemperature1OverShutdown = _CmmSysPsuTemperature1OverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 75),
    _CmmSysPsuTemperature1OverShutdown_Type()
)
cmmSysPsuTemperature1OverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1OverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1OverShutdown.setUnits("0.01 C")
_CmmSysPsuTemperature1UnderShutdown_Type = Integer32
_CmmSysPsuTemperature1UnderShutdown_Object = MibTableColumn
cmmSysPsuTemperature1UnderShutdown = _CmmSysPsuTemperature1UnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 76),
    _CmmSysPsuTemperature1UnderShutdown_Type()
)
cmmSysPsuTemperature1UnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1UnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1UnderShutdown.setUnits("0.01 C")
_CmmSysPsuTemperature1OverResume_Type = Integer32
_CmmSysPsuTemperature1OverResume_Object = MibTableColumn
cmmSysPsuTemperature1OverResume = _CmmSysPsuTemperature1OverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 77),
    _CmmSysPsuTemperature1OverResume_Type()
)
cmmSysPsuTemperature1OverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1OverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1OverResume.setUnits("0.01 C")
_CmmSysPsuTemperature1UnderResume_Type = Integer32
_CmmSysPsuTemperature1UnderResume_Object = MibTableColumn
cmmSysPsuTemperature1UnderResume = _CmmSysPsuTemperature1UnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 78),
    _CmmSysPsuTemperature1UnderResume_Type()
)
cmmSysPsuTemperature1UnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1UnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature1UnderResume.setUnits("0.01 C")
_CmmSysPsuTemperature2OverShutdown_Type = Integer32
_CmmSysPsuTemperature2OverShutdown_Object = MibTableColumn
cmmSysPsuTemperature2OverShutdown = _CmmSysPsuTemperature2OverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 79),
    _CmmSysPsuTemperature2OverShutdown_Type()
)
cmmSysPsuTemperature2OverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2OverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2OverShutdown.setUnits("0.01 C")
_CmmSysPsuTemperature2UnderShutdown_Type = Integer32
_CmmSysPsuTemperature2UnderShutdown_Object = MibTableColumn
cmmSysPsuTemperature2UnderShutdown = _CmmSysPsuTemperature2UnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 80),
    _CmmSysPsuTemperature2UnderShutdown_Type()
)
cmmSysPsuTemperature2UnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2UnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2UnderShutdown.setUnits("0.01 C")
_CmmSysPsuTemperature2OverResume_Type = Integer32
_CmmSysPsuTemperature2OverResume_Object = MibTableColumn
cmmSysPsuTemperature2OverResume = _CmmSysPsuTemperature2OverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 81),
    _CmmSysPsuTemperature2OverResume_Type()
)
cmmSysPsuTemperature2OverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2OverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2OverResume.setUnits("0.01 C")
_CmmSysPsuTemperature2UnderResume_Type = Integer32
_CmmSysPsuTemperature2UnderResume_Object = MibTableColumn
cmmSysPsuTemperature2UnderResume = _CmmSysPsuTemperature2UnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 82),
    _CmmSysPsuTemperature2UnderResume_Type()
)
cmmSysPsuTemperature2UnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2UnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature2UnderResume.setUnits("0.01 C")
_CmmSysPSTemperature3_Type = Integer32
_CmmSysPSTemperature3_Object = MibTableColumn
cmmSysPSTemperature3 = _CmmSysPSTemperature3_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 83),
    _CmmSysPSTemperature3_Type()
)
cmmSysPSTemperature3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3.setUnits("0.01 C")
_CmmSysPSTemperature3AlertThresholdMin_Type = Integer32
_CmmSysPSTemperature3AlertThresholdMin_Object = MibTableColumn
cmmSysPSTemperature3AlertThresholdMin = _CmmSysPSTemperature3AlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 84),
    _CmmSysPSTemperature3AlertThresholdMin_Type()
)
cmmSysPSTemperature3AlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3AlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3AlertThresholdMin.setUnits("0.01 C")
_CmmSysPSTemperature3AlertThresholdMax_Type = Integer32
_CmmSysPSTemperature3AlertThresholdMax_Object = MibTableColumn
cmmSysPSTemperature3AlertThresholdMax = _CmmSysPSTemperature3AlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 85),
    _CmmSysPSTemperature3AlertThresholdMax_Type()
)
cmmSysPSTemperature3AlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3AlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3AlertThresholdMax.setUnits("0.01 C")
_CmmSysPSTemperature3CriticalThresholdMin_Type = Integer32
_CmmSysPSTemperature3CriticalThresholdMin_Object = MibTableColumn
cmmSysPSTemperature3CriticalThresholdMin = _CmmSysPSTemperature3CriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 86),
    _CmmSysPSTemperature3CriticalThresholdMin_Type()
)
cmmSysPSTemperature3CriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3CriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3CriticalThresholdMin.setUnits("0.01 C")
_CmmSysPSTemperature3CriticalThresholdMax_Type = Integer32
_CmmSysPSTemperature3CriticalThresholdMax_Object = MibTableColumn
cmmSysPSTemperature3CriticalThresholdMax = _CmmSysPSTemperature3CriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 87),
    _CmmSysPSTemperature3CriticalThresholdMax_Type()
)
cmmSysPSTemperature3CriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3CriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature3CriticalThresholdMax.setUnits("0.01 C")
_CmmSysPsuTemperature3OverShutdown_Type = Integer32
_CmmSysPsuTemperature3OverShutdown_Object = MibTableColumn
cmmSysPsuTemperature3OverShutdown = _CmmSysPsuTemperature3OverShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 88),
    _CmmSysPsuTemperature3OverShutdown_Type()
)
cmmSysPsuTemperature3OverShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3OverShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3OverShutdown.setUnits("0.01 C")
_CmmSysPsuTemperature3UnderShutdown_Type = Integer32
_CmmSysPsuTemperature3UnderShutdown_Object = MibTableColumn
cmmSysPsuTemperature3UnderShutdown = _CmmSysPsuTemperature3UnderShutdown_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 89),
    _CmmSysPsuTemperature3UnderShutdown_Type()
)
cmmSysPsuTemperature3UnderShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3UnderShutdown.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3UnderShutdown.setUnits("0.01 C")
_CmmSysPsuTemperature3OverResume_Type = Integer32
_CmmSysPsuTemperature3OverResume_Object = MibTableColumn
cmmSysPsuTemperature3OverResume = _CmmSysPsuTemperature3OverResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 90),
    _CmmSysPsuTemperature3OverResume_Type()
)
cmmSysPsuTemperature3OverResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3OverResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3OverResume.setUnits("0.01 C")
_CmmSysPsuTemperature3UnderResume_Type = Integer32
_CmmSysPsuTemperature3UnderResume_Object = MibTableColumn
cmmSysPsuTemperature3UnderResume = _CmmSysPsuTemperature3UnderResume_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 91),
    _CmmSysPsuTemperature3UnderResume_Type()
)
cmmSysPsuTemperature3UnderResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3UnderResume.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPsuTemperature3UnderResume.setUnits("0.01 C")
_CmmSysPSFan3Rpm_Type = Integer32
_CmmSysPSFan3Rpm_Object = MibTableColumn
cmmSysPSFan3Rpm = _CmmSysPSFan3Rpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 92),
    _CmmSysPSFan3Rpm_Type()
)
cmmSysPSFan3Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSFan3Rpm.setStatus("current")
_CmmSysPSFan4Rpm_Type = Integer32
_CmmSysPSFan4Rpm_Object = MibTableColumn
cmmSysPSFan4Rpm = _CmmSysPSFan4Rpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 93),
    _CmmSysPSFan4Rpm_Type()
)
cmmSysPSFan4Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSFan4Rpm.setStatus("current")
_CmmSysPowerRailTable_Object = MibTable
cmmSysPowerRailTable = _CmmSysPowerRailTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cmmSysPowerRailTable.setStatus("current")
_CmmSysPowerRailEntry_Object = MibTableRow
cmmSysPowerRailEntry = _CmmSysPowerRailEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1)
)
cmmSysPowerRailEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysPowerRailEntry.setStatus("current")


class _CmmSysPOWERVDDR_Type(Integer32):
    """Custom type cmmSysPOWERVDDR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPOWERVDDR_Type.__name__ = "Integer32"
_CmmSysPOWERVDDR_Object = MibTableColumn
cmmSysPOWERVDDR = _CmmSysPOWERVDDR_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 1),
    _CmmSysPOWERVDDR_Type()
)
cmmSysPOWERVDDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPOWERVDDR.setStatus("current")


class _CmmSysPOWERCORE_Type(Integer32):
    """Custom type cmmSysPOWERCORE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPOWERCORE_Type.__name__ = "Integer32"
_CmmSysPOWERCORE_Object = MibTableColumn
cmmSysPOWERCORE = _CmmSysPOWERCORE_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 2),
    _CmmSysPOWERCORE_Type()
)
cmmSysPOWERCORE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPOWERCORE.setStatus("current")


class _CmmSysV1P1POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P1POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV1P1POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P1POWERRAIL_Object = MibTableColumn
cmmSysV1P1POWERRAIL = _CmmSysV1P1POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 3),
    _CmmSysV1P1POWERRAIL_Type()
)
cmmSysV1P1POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P1POWERRAIL.setStatus("current")


class _CmmSysMAINBOARDPOWERRAIL_Type(Integer32):
    """Custom type cmmSysMAINBOARDPOWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysMAINBOARDPOWERRAIL_Type.__name__ = "Integer32"
_CmmSysMAINBOARDPOWERRAIL_Object = MibTableColumn
cmmSysMAINBOARDPOWERRAIL = _CmmSysMAINBOARDPOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 4),
    _CmmSysMAINBOARDPOWERRAIL_Type()
)
cmmSysMAINBOARDPOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysMAINBOARDPOWERRAIL.setStatus("current")


class _CmmSysV1P05POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P05POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV1P05POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P05POWERRAIL_Object = MibTableColumn
cmmSysV1P05POWERRAIL = _CmmSysV1P05POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 5),
    _CmmSysV1P05POWERRAIL_Type()
)
cmmSysV1P05POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P05POWERRAIL.setStatus("current")


class _CmmSysV1P5POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P5POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV1P5POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P5POWERRAIL_Object = MibTableColumn
cmmSysV1P5POWERRAIL = _CmmSysV1P5POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 6),
    _CmmSysV1P5POWERRAIL_Type()
)
cmmSysV1P5POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P5POWERRAIL.setStatus("current")


class _CmmSysVCCPOWERRAIL_Type(Integer32):
    """Custom type cmmSysVCCPOWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCPOWERRAIL_Type.__name__ = "Integer32"
_CmmSysVCCPOWERRAIL_Object = MibTableColumn
cmmSysVCCPOWERRAIL = _CmmSysVCCPOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 7),
    _CmmSysVCCPOWERRAIL_Type()
)
cmmSysVCCPOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCPOWERRAIL.setStatus("current")


class _CmmSysSBV1P5POWERRAIL_Type(Integer32):
    """Custom type cmmSysSBV1P5POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysSBV1P5POWERRAIL_Type.__name__ = "Integer32"
_CmmSysSBV1P5POWERRAIL_Object = MibTableColumn
cmmSysSBV1P5POWERRAIL = _CmmSysSBV1P5POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 8),
    _CmmSysSBV1P5POWERRAIL_Type()
)
cmmSysSBV1P5POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysSBV1P5POWERRAIL.setStatus("current")


class _CmmSysV1P0POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P0POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV1P0POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P0POWERRAIL_Object = MibTableColumn
cmmSysV1P0POWERRAIL = _CmmSysV1P0POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 9),
    _CmmSysV1P0POWERRAIL_Type()
)
cmmSysV1P0POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P0POWERRAIL.setStatus("current")


class _CmmSysV3P3POWERRAIL_Type(Integer32):
    """Custom type cmmSysV3P3POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV3P3POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV3P3POWERRAIL_Object = MibTableColumn
cmmSysV3P3POWERRAIL = _CmmSysV3P3POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 10),
    _CmmSysV3P3POWERRAIL_Type()
)
cmmSysV3P3POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV3P3POWERRAIL.setStatus("current")


class _CmmSysV1P8POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P8POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV1P8POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P8POWERRAIL_Object = MibTableColumn
cmmSysV1P8POWERRAIL = _CmmSysV1P8POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 11),
    _CmmSysV1P8POWERRAIL_Type()
)
cmmSysV1P8POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P8POWERRAIL.setStatus("current")


class _CmmSysV1P35POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P35POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV1P35POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P35POWERRAIL_Object = MibTableColumn
cmmSysV1P35POWERRAIL = _CmmSysV1P35POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 12),
    _CmmSysV1P35POWERRAIL_Type()
)
cmmSysV1P35POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P35POWERRAIL.setStatus("current")


class _CmmSysVCC5V_Type(Integer32):
    """Custom type cmmSysVCC5V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCC5V_Type.__name__ = "Integer32"
_CmmSysVCC5V_Object = MibTableColumn
cmmSysVCC5V = _CmmSysVCC5V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 13),
    _CmmSysVCC5V_Type()
)
cmmSysVCC5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCC5V.setStatus("current")


class _CmmSysVCC33V_Type(Integer32):
    """Custom type cmmSysVCC33V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCC33V_Type.__name__ = "Integer32"
_CmmSysVCC33V_Object = MibTableColumn
cmmSysVCC33V = _CmmSysVCC33V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 14),
    _CmmSysVCC33V_Type()
)
cmmSysVCC33V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCC33V.setStatus("current")


class _CmmSysVCCMAC1V_Type(Integer32):
    """Custom type cmmSysVCCMAC1V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCMAC1V_Type.__name__ = "Integer32"
_CmmSysVCCMAC1V_Object = MibTableColumn
cmmSysVCCMAC1V = _CmmSysVCCMAC1V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 15),
    _CmmSysVCCMAC1V_Type()
)
cmmSysVCCMAC1V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCMAC1V.setStatus("current")


class _CmmSysVCCMACAVS1V_Type(Integer32):
    """Custom type cmmSysVCCMACAVS1V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCMACAVS1V_Type.__name__ = "Integer32"
_CmmSysVCCMACAVS1V_Object = MibTableColumn
cmmSysVCCMACAVS1V = _CmmSysVCCMACAVS1V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 16),
    _CmmSysVCCMACAVS1V_Type()
)
cmmSysVCCMACAVS1V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCMACAVS1V.setStatus("current")


class _CmmSysVCCV1P05_Type(Integer32):
    """Custom type cmmSysVCCV1P05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCV1P05_Type.__name__ = "Integer32"
_CmmSysVCCV1P05_Object = MibTableColumn
cmmSysVCCV1P05 = _CmmSysVCCV1P05_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 17),
    _CmmSysVCCV1P05_Type()
)
cmmSysVCCV1P05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCV1P05.setStatus("current")


class _CmmSysVCCV1P5_Type(Integer32):
    """Custom type cmmSysVCCV1P5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCV1P5_Type.__name__ = "Integer32"
_CmmSysVCCV1P5_Object = MibTableColumn
cmmSysVCCV1P5 = _CmmSysVCCV1P5_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 18),
    _CmmSysVCCV1P5_Type()
)
cmmSysVCCV1P5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCV1P5.setStatus("current")


class _CmmSysVCCV1P8_Type(Integer32):
    """Custom type cmmSysVCCV1P8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCV1P8_Type.__name__ = "Integer32"
_CmmSysVCCV1P8_Object = MibTableColumn
cmmSysVCCV1P8 = _CmmSysVCCV1P8_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 19),
    _CmmSysVCCV1P8_Type()
)
cmmSysVCCV1P8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCV1P8.setStatus("current")


class _CmmSysVCCAVS1V_Type(Integer32):
    """Custom type cmmSysVCCAVS1V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCAVS1V_Type.__name__ = "Integer32"
_CmmSysVCCAVS1V_Object = MibTableColumn
cmmSysVCCAVS1V = _CmmSysVCCAVS1V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 20),
    _CmmSysVCCAVS1V_Type()
)
cmmSysVCCAVS1V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCAVS1V.setStatus("current")


class _CmmSysDDRVTT_Type(Integer32):
    """Custom type cmmSysDDRVTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysDDRVTT_Type.__name__ = "Integer32"
_CmmSysDDRVTT_Object = MibTableColumn
cmmSysDDRVTT = _CmmSysDDRVTT_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 21),
    _CmmSysDDRVTT_Type()
)
cmmSysDDRVTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysDDRVTT.setStatus("current")


class _CmmSysSBV1P9POWERRAIL_Type(Integer32):
    """Custom type cmmSysSBV1P9POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysSBV1P9POWERRAIL_Type.__name__ = "Integer32"
_CmmSysSBV1P9POWERRAIL_Object = MibTableColumn
cmmSysSBV1P9POWERRAIL = _CmmSysSBV1P9POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 22),
    _CmmSysSBV1P9POWERRAIL_Type()
)
cmmSysSBV1P9POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysSBV1P9POWERRAIL.setStatus("current")


class _CmmSysVCCMACV1P25_Type(Integer32):
    """Custom type cmmSysVCCMACV1P25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysVCCMACV1P25_Type.__name__ = "Integer32"
_CmmSysVCCMACV1P25_Object = MibTableColumn
cmmSysVCCMACV1P25 = _CmmSysVCCMACV1P25_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 23),
    _CmmSysVCCMACV1P25_Type()
)
cmmSysVCCMACV1P25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCMACV1P25.setStatus("current")


class _CmmSysMACV1P8_Type(Integer32):
    """Custom type cmmSysMACV1P8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysMACV1P8_Type.__name__ = "Integer32"
_CmmSysMACV1P8_Object = MibTableColumn
cmmSysMACV1P8 = _CmmSysMACV1P8_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 24),
    _CmmSysMACV1P8_Type()
)
cmmSysMACV1P8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysMACV1P8.setStatus("current")


class _CmmSysPS1_Type(Integer32):
    """Custom type cmmSysPS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS1_Type.__name__ = "Integer32"
_CmmSysPS1_Object = MibTableColumn
cmmSysPS1 = _CmmSysPS1_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 25),
    _CmmSysPS1_Type()
)
cmmSysPS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS1.setStatus("current")


class _CmmSysPS2_Type(Integer32):
    """Custom type cmmSysPS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS2_Type.__name__ = "Integer32"
_CmmSysPS2_Object = MibTableColumn
cmmSysPS2 = _CmmSysPS2_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 26),
    _CmmSysPS2_Type()
)
cmmSysPS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS2.setStatus("current")


class _CmmSysPS1POWERRAIL_Type(Integer32):
    """Custom type cmmSysPS1POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS1POWERRAIL_Type.__name__ = "Integer32"
_CmmSysPS1POWERRAIL_Object = MibTableColumn
cmmSysPS1POWERRAIL = _CmmSysPS1POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 27),
    _CmmSysPS1POWERRAIL_Type()
)
cmmSysPS1POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS1POWERRAIL.setStatus("current")


class _CmmSysPS2POWERRAIL_Type(Integer32):
    """Custom type cmmSysPS2POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS2POWERRAIL_Type.__name__ = "Integer32"
_CmmSysPS2POWERRAIL_Object = MibTableColumn
cmmSysPS2POWERRAIL = _CmmSysPS2POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 28),
    _CmmSysPS2POWERRAIL_Type()
)
cmmSysPS2POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS2POWERRAIL.setStatus("current")


class _CmmSysPS1V12POWERRAIL_Type(Integer32):
    """Custom type cmmSysPS1V12POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS1V12POWERRAIL_Type.__name__ = "Integer32"
_CmmSysPS1V12POWERRAIL_Object = MibTableColumn
cmmSysPS1V12POWERRAIL = _CmmSysPS1V12POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 29),
    _CmmSysPS1V12POWERRAIL_Type()
)
cmmSysPS1V12POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS1V12POWERRAIL.setStatus("current")


class _CmmSysPS2V12POWERRAIL_Type(Integer32):
    """Custom type cmmSysPS2V12POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS2V12POWERRAIL_Type.__name__ = "Integer32"
_CmmSysPS2V12POWERRAIL_Object = MibTableColumn
cmmSysPS2V12POWERRAIL = _CmmSysPS2V12POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 30),
    _CmmSysPS2V12POWERRAIL_Type()
)
cmmSysPS2V12POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS2V12POWERRAIL.setStatus("current")


class _CmmSysPS1ACALERTPOWERRAIL_Type(Integer32):
    """Custom type cmmSysPS1ACALERTPOWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS1ACALERTPOWERRAIL_Type.__name__ = "Integer32"
_CmmSysPS1ACALERTPOWERRAIL_Object = MibTableColumn
cmmSysPS1ACALERTPOWERRAIL = _CmmSysPS1ACALERTPOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 31),
    _CmmSysPS1ACALERTPOWERRAIL_Type()
)
cmmSysPS1ACALERTPOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS1ACALERTPOWERRAIL.setStatus("current")


class _CmmSysPS2ACALERTPOWERRAIL_Type(Integer32):
    """Custom type cmmSysPS2ACALERTPOWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPS2ACALERTPOWERRAIL_Type.__name__ = "Integer32"
_CmmSysPS2ACALERTPOWERRAIL_Object = MibTableColumn
cmmSysPS2ACALERTPOWERRAIL = _CmmSysPS2ACALERTPOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 32),
    _CmmSysPS2ACALERTPOWERRAIL_Type()
)
cmmSysPS2ACALERTPOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS2ACALERTPOWERRAIL.setStatus("current")


class _CmmSysPOWERVCCP_Type(Integer32):
    """Custom type cmmSysPOWERVCCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysPOWERVCCP_Type.__name__ = "Integer32"
_CmmSysPOWERVCCP_Object = MibTableColumn
cmmSysPOWERVCCP = _CmmSysPOWERVCCP_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 33),
    _CmmSysPOWERVCCP_Type()
)
cmmSysPOWERVCCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPOWERVCCP.setStatus("current")


class _CmmSysV5APOWERRAIL_Type(Integer32):
    """Custom type cmmSysV5APOWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV5APOWERRAIL_Type.__name__ = "Integer32"
_CmmSysV5APOWERRAIL_Object = MibTableColumn
cmmSysV5APOWERRAIL = _CmmSysV5APOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 34),
    _CmmSysV5APOWERRAIL_Type()
)
cmmSysV5APOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV5APOWERRAIL.setStatus("current")


class _CmmSysV3P3APOWERRAIL_Type(Integer32):
    """Custom type cmmSysV3P3APOWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysV3P3APOWERRAIL_Type.__name__ = "Integer32"
_CmmSysV3P3APOWERRAIL_Object = MibTableColumn
cmmSysV3P3APOWERRAIL = _CmmSysV3P3APOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 35),
    _CmmSysV3P3APOWERRAIL_Type()
)
cmmSysV3P3APOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV3P3APOWERRAIL.setStatus("current")


class _CmmSysXP0RV75POWERRAIL_Type(Integer32):
    """Custom type cmmSysXP0RV75POWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysXP0RV75POWERRAIL_Type.__name__ = "Integer32"
_CmmSysXP0RV75POWERRAIL_Object = MibTableColumn
cmmSysXP0RV75POWERRAIL = _CmmSysXP0RV75POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 36),
    _CmmSysXP0RV75POWERRAIL_Type()
)
cmmSysXP0RV75POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysXP0RV75POWERRAIL.setStatus("current")


class _CmmSysXP1RV07CPPOWERRAIL_Type(Integer32):
    """Custom type cmmSysXP1RV07CPPOWERRAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("good", 1),
          ("fail", 2))
    )


_CmmSysXP1RV07CPPOWERRAIL_Type.__name__ = "Integer32"
_CmmSysXP1RV07CPPOWERRAIL_Object = MibTableColumn
cmmSysXP1RV07CPPOWERRAIL = _CmmSysXP1RV07CPPOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 37),
    _CmmSysXP1RV07CPPOWERRAIL_Type()
)
cmmSysXP1RV07CPPOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysXP1RV07CPPOWERRAIL.setStatus("current")
_CmmFanTrayTable_Object = MibTable
cmmFanTrayTable = _CmmFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cmmFanTrayTable.setStatus("current")
_CmmFanTrayEntry_Object = MibTableRow
cmmFanTrayEntry = _CmmFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1)
)
cmmFanTrayEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
)
if mibBuilder.loadTexts:
    cmmFanTrayEntry.setStatus("current")


class _CmmFanTrayNumber_Type(Integer32):
    """Custom type cmmFanTrayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmFanTrayNumber_Type.__name__ = "Integer32"
_CmmFanTrayNumber_Object = MibTableColumn
cmmFanTrayNumber = _CmmFanTrayNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1, 1),
    _CmmFanTrayNumber_Type()
)
cmmFanTrayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanTrayNumber.setStatus("current")


class _CmmFanTrayStatus_Type(Integer32):
    """Custom type cmmFanTrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("notpresent", 1),
          ("present", 2))
    )


_CmmFanTrayStatus_Type.__name__ = "Integer32"
_CmmFanTrayStatus_Object = MibTableColumn
cmmFanTrayStatus = _CmmFanTrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1, 2),
    _CmmFanTrayStatus_Type()
)
cmmFanTrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanTrayStatus.setStatus("current")
_CmmFanTrayLedColor_Type = LedColorCode
_CmmFanTrayLedColor_Object = MibTableColumn
cmmFanTrayLedColor = _CmmFanTrayLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1, 3),
    _CmmFanTrayLedColor_Type()
)
cmmFanTrayLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanTrayLedColor.setStatus("current")
_CmmFanTable_Object = MibTable
cmmFanTable = _CmmFanTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cmmFanTable.setStatus("current")
_CmmFanEntry_Object = MibTableRow
cmmFanEntry = _CmmFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1)
)
cmmFanEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmFanIndex"),
)
if mibBuilder.loadTexts:
    cmmFanEntry.setStatus("current")


class _CmmFanIndex_Type(Integer32):
    """Custom type cmmFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmFanIndex_Type.__name__ = "Integer32"
_CmmFanIndex_Object = MibTableColumn
cmmFanIndex = _CmmFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 1),
    _CmmFanIndex_Type()
)
cmmFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanIndex.setStatus("current")
_CmmFanRpm_Type = Integer32
_CmmFanRpm_Object = MibTableColumn
cmmFanRpm = _CmmFanRpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 2),
    _CmmFanRpm_Type()
)
cmmFanRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanRpm.setStatus("current")
_CmmFanRpmMin_Type = Integer32
_CmmFanRpmMin_Object = MibTableColumn
cmmFanRpmMin = _CmmFanRpmMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 3),
    _CmmFanRpmMin_Type()
)
cmmFanRpmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanRpmMin.setStatus("current")
_CmmFanRpmMax_Type = Integer32
_CmmFanRpmMax_Object = MibTableColumn
cmmFanRpmMax = _CmmFanRpmMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 4),
    _CmmFanRpmMax_Type()
)
cmmFanRpmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanRpmMax.setStatus("current")


class _CmmFanStatus_Type(Integer32):
    """Custom type cmmFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("notpresent", 1),
          ("running", 2),
          ("faulty", 3),
          ("stalled", 4))
    )


_CmmFanStatus_Type.__name__ = "Integer32"
_CmmFanStatus_Object = MibTableColumn
cmmFanStatus = _CmmFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 5),
    _CmmFanStatus_Type()
)
cmmFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanStatus.setStatus("current")


class _CmmFanLocation_Type(Integer32):
    """Custom type cmmFanLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("front", 1),
          ("rear", 2),
          ("unknown", 3))
    )


_CmmFanLocation_Type.__name__ = "Integer32"
_CmmFanLocation_Object = MibTableColumn
cmmFanLocation = _CmmFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 6),
    _CmmFanLocation_Type()
)
cmmFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanLocation.setStatus("current")
_CmmSysTemperatureTable_Object = MibTable
cmmSysTemperatureTable = _CmmSysTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cmmSysTemperatureTable.setStatus("current")
_CmmSysTemperatureEntry_Object = MibTableRow
cmmSysTemperatureEntry = _CmmSysTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1)
)
cmmSysTemperatureEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    cmmSysTemperatureEntry.setStatus("current")


class _CmmSysTemperatureSensorIndex_Type(Integer32):
    """Custom type cmmSysTemperatureSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmSysTemperatureSensorIndex_Type.__name__ = "Integer32"
_CmmSysTemperatureSensorIndex_Object = MibTableColumn
cmmSysTemperatureSensorIndex = _CmmSysTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 1),
    _CmmSysTemperatureSensorIndex_Type()
)
cmmSysTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureSensorIndex.setStatus("current")
_CmmSysTemperatureSensorName_Type = DisplayString
_CmmSysTemperatureSensorName_Object = MibTableColumn
cmmSysTemperatureSensorName = _CmmSysTemperatureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 2),
    _CmmSysTemperatureSensorName_Type()
)
cmmSysTemperatureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureSensorName.setStatus("current")
_CmmSysTemperatureValue_Type = Integer32
_CmmSysTemperatureValue_Object = MibTableColumn
cmmSysTemperatureValue = _CmmSysTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 3),
    _CmmSysTemperatureValue_Type()
)
cmmSysTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTemperatureValue.setUnits("0.01 C")
_CmmSysTempEmergencyThresholdMin_Type = Integer32
_CmmSysTempEmergencyThresholdMin_Object = MibTableColumn
cmmSysTempEmergencyThresholdMin = _CmmSysTempEmergencyThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 4),
    _CmmSysTempEmergencyThresholdMin_Type()
)
cmmSysTempEmergencyThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMin.setUnits("0.01 C")
_CmmSysTempEmergencyThresholdMax_Type = Integer32
_CmmSysTempEmergencyThresholdMax_Object = MibTableColumn
cmmSysTempEmergencyThresholdMax = _CmmSysTempEmergencyThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 5),
    _CmmSysTempEmergencyThresholdMax_Type()
)
cmmSysTempEmergencyThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMax.setUnits("0.01 C")
_CmmSysTempCriticalThresholdMin_Type = Integer32
_CmmSysTempCriticalThresholdMin_Object = MibTableColumn
cmmSysTempCriticalThresholdMin = _CmmSysTempCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 6),
    _CmmSysTempCriticalThresholdMin_Type()
)
cmmSysTempCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMin.setUnits("0.01 C")
_CmmSysTempCriticalThresholdMax_Type = Integer32
_CmmSysTempCriticalThresholdMax_Object = MibTableColumn
cmmSysTempCriticalThresholdMax = _CmmSysTempCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 7),
    _CmmSysTempCriticalThresholdMax_Type()
)
cmmSysTempCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMax.setUnits("0.01 C")
_CmmSysTempAlertThresholdMin_Type = Integer32
_CmmSysTempAlertThresholdMin_Object = MibTableColumn
cmmSysTempAlertThresholdMin = _CmmSysTempAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 8),
    _CmmSysTempAlertThresholdMin_Type()
)
cmmSysTempAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMin.setUnits("0.01 C")
_CmmSysTempAlertThresholdMax_Type = Integer32
_CmmSysTempAlertThresholdMax_Object = MibTableColumn
cmmSysTempAlertThresholdMax = _CmmSysTempAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 9),
    _CmmSysTempAlertThresholdMax_Type()
)
cmmSysTempAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMax.setUnits("0.01 C")
_CmmSysTempMinValue_Type = Integer32
_CmmSysTempMinValue_Object = MibTableColumn
cmmSysTempMinValue = _CmmSysTempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 10),
    _CmmSysTempMinValue_Type()
)
cmmSysTempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempMinValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempMinValue.setUnits("0.01 C")
_CmmSysTempMaxValue_Type = Integer32
_CmmSysTempMaxValue_Object = MibTableColumn
cmmSysTempMaxValue = _CmmSysTempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 11),
    _CmmSysTempMaxValue_Type()
)
cmmSysTempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempMaxValue.setUnits("0.01 C")
_CmmSysTempAverageValue_Type = Integer32
_CmmSysTempAverageValue_Object = MibTableColumn
cmmSysTempAverageValue = _CmmSysTempAverageValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 12),
    _CmmSysTempAverageValue_Type()
)
cmmSysTempAverageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempAverageValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempAverageValue.setUnits("0.01 C")
_CmmSysComponentStatusTable_Object = MibTable
cmmSysComponentStatusTable = _CmmSysComponentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cmmSysComponentStatusTable.setStatus("current")
_CmmSysComponentStatusEntry_Object = MibTableRow
cmmSysComponentStatusEntry = _CmmSysComponentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1)
)
cmmSysComponentStatusEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysComponentStatusEntry.setStatus("current")


class _CmmSysPsu1Status_Type(Integer32):
    """Custom type cmmSysPsu1Status based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysPsu1Status_Type.__name__ = "Integer32"
_CmmSysPsu1Status_Object = MibTableColumn
cmmSysPsu1Status = _CmmSysPsu1Status_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 1),
    _CmmSysPsu1Status_Type()
)
cmmSysPsu1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu1Status.setStatus("current")
_CmmSysPsu1LedColor_Type = LedColorCode
_CmmSysPsu1LedColor_Object = MibTableColumn
cmmSysPsu1LedColor = _CmmSysPsu1LedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 2),
    _CmmSysPsu1LedColor_Type()
)
cmmSysPsu1LedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu1LedColor.setStatus("current")


class _CmmSysPsu2Status_Type(Integer32):
    """Custom type cmmSysPsu2Status based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysPsu2Status_Type.__name__ = "Integer32"
_CmmSysPsu2Status_Object = MibTableColumn
cmmSysPsu2Status = _CmmSysPsu2Status_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 3),
    _CmmSysPsu2Status_Type()
)
cmmSysPsu2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu2Status.setStatus("current")
_CmmSysPsu2LedColor_Type = LedColorCode
_CmmSysPsu2LedColor_Object = MibTableColumn
cmmSysPsu2LedColor = _CmmSysPsu2LedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 4),
    _CmmSysPsu2LedColor_Type()
)
cmmSysPsu2LedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu2LedColor.setStatus("current")


class _CmmSysLocatorLedStatus_Type(Integer32):
    """Custom type cmmSysLocatorLedStatus based on Integer32"""
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
        *(("notpresent", 1),
          ("on", 2),
          ("off", 3),
          ("unknown", 4))
    )


_CmmSysLocatorLedStatus_Type.__name__ = "Integer32"
_CmmSysLocatorLedStatus_Object = MibTableColumn
cmmSysLocatorLedStatus = _CmmSysLocatorLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 5),
    _CmmSysLocatorLedStatus_Type()
)
cmmSysLocatorLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysLocatorLedStatus.setStatus("current")
_CmmSysLocatorLedColor_Type = LedColorCode
_CmmSysLocatorLedColor_Object = MibTableColumn
cmmSysLocatorLedColor = _CmmSysLocatorLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 6),
    _CmmSysLocatorLedColor_Type()
)
cmmSysLocatorLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysLocatorLedColor.setStatus("current")


class _CmmSysMasterLedStatus_Type(Integer32):
    """Custom type cmmSysMasterLedStatus based on Integer32"""
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
        *(("notpresent", 1),
          ("on", 2),
          ("off", 3),
          ("unknown", 4))
    )


_CmmSysMasterLedStatus_Type.__name__ = "Integer32"
_CmmSysMasterLedStatus_Object = MibTableColumn
cmmSysMasterLedStatus = _CmmSysMasterLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 7),
    _CmmSysMasterLedStatus_Type()
)
cmmSysMasterLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysMasterLedStatus.setStatus("current")
_CmmSysMasterLedColor_Type = LedColorCode
_CmmSysMasterLedColor_Object = MibTableColumn
cmmSysMasterLedColor = _CmmSysMasterLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 8),
    _CmmSysMasterLedColor_Type()
)
cmmSysMasterLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysMasterLedColor.setStatus("current")


class _CmmSysFanStatus_Type(Integer32):
    """Custom type cmmSysFanStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysFanStatus_Type.__name__ = "Integer32"
_CmmSysFanStatus_Object = MibTableColumn
cmmSysFanStatus = _CmmSysFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 9),
    _CmmSysFanStatus_Type()
)
cmmSysFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysFanStatus.setStatus("current")
_CmmSysFrontFanLedColor_Type = LedColorCode
_CmmSysFrontFanLedColor_Object = MibTableColumn
cmmSysFrontFanLedColor = _CmmSysFrontFanLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 10),
    _CmmSysFrontFanLedColor_Type()
)
cmmSysFrontFanLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysFrontFanLedColor.setStatus("current")


class _CmmSysRamStatus_Type(Integer32):
    """Custom type cmmSysRamStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysRamStatus_Type.__name__ = "Integer32"
_CmmSysRamStatus_Object = MibTableColumn
cmmSysRamStatus = _CmmSysRamStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 11),
    _CmmSysRamStatus_Type()
)
cmmSysRamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamStatus.setStatus("current")


class _CmmSysCpuStatus_Type(Integer32):
    """Custom type cmmSysCpuStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysCpuStatus_Type.__name__ = "Integer32"
_CmmSysCpuStatus_Object = MibTableColumn
cmmSysCpuStatus = _CmmSysCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 12),
    _CmmSysCpuStatus_Type()
)
cmmSysCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpuStatus.setStatus("current")


class _CmmSysDiskStatus_Type(Integer32):
    """Custom type cmmSysDiskStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysDiskStatus_Type.__name__ = "Integer32"
_CmmSysDiskStatus_Object = MibTableColumn
cmmSysDiskStatus = _CmmSysDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 13),
    _CmmSysDiskStatus_Type()
)
cmmSysDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysDiskStatus.setStatus("current")


class _CmmSysTemperatureStatus_Type(Integer32):
    """Custom type cmmSysTemperatureStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysTemperatureStatus_Type.__name__ = "Integer32"
_CmmSysTemperatureStatus_Object = MibTableColumn
cmmSysTemperatureStatus = _CmmSysTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 14),
    _CmmSysTemperatureStatus_Type()
)
cmmSysTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureStatus.setStatus("current")
_CmmSysSwModuleTable_Object = MibTable
cmmSysSwModuleTable = _CmmSysSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cmmSysSwModuleTable.setStatus("current")
_CmmSysSwModuleEntry_Object = MibTableRow
cmmSysSwModuleEntry = _CmmSysSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12, 1)
)
cmmSysSwModuleEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysSwModuleEntry.setStatus("current")
_CmmSysSwRuntimeImgVersion_Type = DisplayString
_CmmSysSwRuntimeImgVersion_Object = MibTableColumn
cmmSysSwRuntimeImgVersion = _CmmSysSwRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12, 1, 1),
    _CmmSysSwRuntimeImgVersion_Type()
)
cmmSysSwRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysSwRuntimeImgVersion.setStatus("current")
_CmmSysSwRuntimeImgDate_Type = DateAndTime
_CmmSysSwRuntimeImgDate_Object = MibTableColumn
cmmSysSwRuntimeImgDate = _CmmSysSwRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12, 1, 2),
    _CmmSysSwRuntimeImgDate_Type()
)
cmmSysSwRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysSwRuntimeImgDate.setStatus("current")
_CmmSwitchTemperatureTable_Object = MibTable
cmmSwitchTemperatureTable = _CmmSwitchTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cmmSwitchTemperatureTable.setStatus("current")
_CmmSwitchTemperatureEntry_Object = MibTableRow
cmmSwitchTemperatureEntry = _CmmSwitchTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1)
)
cmmSwitchTemperatureEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmSwitchTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    cmmSwitchTemperatureEntry.setStatus("current")


class _CmmSwitchTemperatureSensorIndex_Type(Integer32):
    """Custom type cmmSwitchTemperatureSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmSwitchTemperatureSensorIndex_Type.__name__ = "Integer32"
_CmmSwitchTemperatureSensorIndex_Object = MibTableColumn
cmmSwitchTemperatureSensorIndex = _CmmSwitchTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1, 1),
    _CmmSwitchTemperatureSensorIndex_Type()
)
cmmSwitchTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSwitchTemperatureSensorIndex.setStatus("current")
_CmmSwitchTemperatureValue_Type = Integer32
_CmmSwitchTemperatureValue_Object = MibTableColumn
cmmSwitchTemperatureValue = _CmmSwitchTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1, 2),
    _CmmSwitchTemperatureValue_Type()
)
cmmSwitchTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSwitchTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSwitchTemperatureValue.setUnits("0.01 C")
_CmmSwitchTempPeakValue_Type = Integer32
_CmmSwitchTempPeakValue_Object = MibTableColumn
cmmSwitchTempPeakValue = _CmmSwitchTempPeakValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1, 3),
    _CmmSwitchTempPeakValue_Type()
)
cmmSwitchTempPeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSwitchTempPeakValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSwitchTempPeakValue.setUnits("0.01 C")
_CmmSysHardDiskTable_Object = MibTable
cmmSysHardDiskTable = _CmmSysHardDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cmmSysHardDiskTable.setStatus("current")
_CmmSysHardDiskEntry_Object = MibTableRow
cmmSysHardDiskEntry = _CmmSysHardDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1)
)
cmmSysHardDiskEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysHardDiskEntry.setStatus("current")
_CmmSysHarddiskSerialno_Type = DisplayString
_CmmSysHarddiskSerialno_Object = MibTableColumn
cmmSysHarddiskSerialno = _CmmSysHarddiskSerialno_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 1),
    _CmmSysHarddiskSerialno_Type()
)
cmmSysHarddiskSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskSerialno.setStatus("current")
_CmmSysHarddiskModelno_Type = DisplayString
_CmmSysHarddiskModelno_Object = MibTableColumn
cmmSysHarddiskModelno = _CmmSysHarddiskModelno_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 2),
    _CmmSysHarddiskModelno_Type()
)
cmmSysHarddiskModelno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskModelno.setStatus("current")
_CmmSysHarddiskFirmwarerev_Type = DisplayString
_CmmSysHarddiskFirmwarerev_Object = MibTableColumn
cmmSysHarddiskFirmwarerev = _CmmSysHarddiskFirmwarerev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 3),
    _CmmSysHarddiskFirmwarerev_Type()
)
cmmSysHarddiskFirmwarerev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskFirmwarerev.setStatus("current")
_CmmSysHarddiskCylinders_Type = Integer32
_CmmSysHarddiskCylinders_Object = MibTableColumn
cmmSysHarddiskCylinders = _CmmSysHarddiskCylinders_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 4),
    _CmmSysHarddiskCylinders_Type()
)
cmmSysHarddiskCylinders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskCylinders.setStatus("current")
_CmmSysHarddiskHeads_Type = Integer32
_CmmSysHarddiskHeads_Object = MibTableColumn
cmmSysHarddiskHeads = _CmmSysHarddiskHeads_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 5),
    _CmmSysHarddiskHeads_Type()
)
cmmSysHarddiskHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskHeads.setStatus("current")
_CmmSysHarddiskSectors_Type = Integer32
_CmmSysHarddiskSectors_Object = MibTableColumn
cmmSysHarddiskSectors = _CmmSysHarddiskSectors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 6),
    _CmmSysHarddiskSectors_Type()
)
cmmSysHarddiskSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskSectors.setStatus("current")
_CmmSysHarddiskUnformattedBytesorTrack_Type = Integer32
_CmmSysHarddiskUnformattedBytesorTrack_Object = MibTableColumn
cmmSysHarddiskUnformattedBytesorTrack = _CmmSysHarddiskUnformattedBytesorTrack_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 7),
    _CmmSysHarddiskUnformattedBytesorTrack_Type()
)
cmmSysHarddiskUnformattedBytesorTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUnformattedBytesorTrack.setStatus("current")
_CmmSysHarddiskUnformattedBytesorSector_Type = Integer32
_CmmSysHarddiskUnformattedBytesorSector_Object = MibTableColumn
cmmSysHarddiskUnformattedBytesorSector = _CmmSysHarddiskUnformattedBytesorSector_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 8),
    _CmmSysHarddiskUnformattedBytesorSector_Type()
)
cmmSysHarddiskUnformattedBytesorSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUnformattedBytesorSector.setStatus("current")
_CmmSysHarddiskRevisionNum_Type = DisplayString
_CmmSysHarddiskRevisionNum_Object = MibTableColumn
cmmSysHarddiskRevisionNum = _CmmSysHarddiskRevisionNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 9),
    _CmmSysHarddiskRevisionNum_Type()
)
cmmSysHarddiskRevisionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskRevisionNum.setStatus("current")
_CmmSysHarddiskTotalsize_Type = Integer32
_CmmSysHarddiskTotalsize_Object = MibTableColumn
cmmSysHarddiskTotalsize = _CmmSysHarddiskTotalsize_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 10),
    _CmmSysHarddiskTotalsize_Type()
)
cmmSysHarddiskTotalsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskTotalsize.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskTotalsize.setUnits(" MBytes ")
_CmmSysHarddiskUsedMem_Type = Integer32
_CmmSysHarddiskUsedMem_Object = MibTableColumn
cmmSysHarddiskUsedMem = _CmmSysHarddiskUsedMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 11),
    _CmmSysHarddiskUsedMem_Type()
)
cmmSysHarddiskUsedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsedMem.setStatus("deprecated")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsedMem.setUnits(" % ")
_CmmSysHarddiskFreeMem_Type = Integer32
_CmmSysHarddiskFreeMem_Object = MibTableColumn
cmmSysHarddiskFreeMem = _CmmSysHarddiskFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 12),
    _CmmSysHarddiskFreeMem_Type()
)
cmmSysHarddiskFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskFreeMem.setStatus("deprecated")
if mibBuilder.loadTexts:
    cmmSysHarddiskFreeMem.setUnits(" % ")
_CmmSysHarddiskUsageAlertThreshold_Type = Integer32
_CmmSysHarddiskUsageAlertThreshold_Object = MibTableColumn
cmmSysHarddiskUsageAlertThreshold = _CmmSysHarddiskUsageAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 13),
    _CmmSysHarddiskUsageAlertThreshold_Type()
)
cmmSysHarddiskUsageAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsageAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsageAlertThreshold.setUnits(" % ")
_CmmSysHarddiskUsageCriticalThreshold_Type = Integer32
_CmmSysHarddiskUsageCriticalThreshold_Object = MibTableColumn
cmmSysHarddiskUsageCriticalThreshold = _CmmSysHarddiskUsageCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 14),
    _CmmSysHarddiskUsageCriticalThreshold_Type()
)
cmmSysHarddiskUsageCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsageCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsageCriticalThreshold.setUnits(" % ")
_CmmSysHardDiskRemainLifeAlertThreshold_Type = Integer32
_CmmSysHardDiskRemainLifeAlertThreshold_Object = MibTableColumn
cmmSysHardDiskRemainLifeAlertThreshold = _CmmSysHardDiskRemainLifeAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 15),
    _CmmSysHardDiskRemainLifeAlertThreshold_Type()
)
cmmSysHardDiskRemainLifeAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLifeAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLifeAlertThreshold.setUnits(" % ")
_CmmSysHardDiskRemainLifeCriticalThreshold_Type = Integer32
_CmmSysHardDiskRemainLifeCriticalThreshold_Object = MibTableColumn
cmmSysHardDiskRemainLifeCriticalThreshold = _CmmSysHardDiskRemainLifeCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 16),
    _CmmSysHardDiskRemainLifeCriticalThreshold_Type()
)
cmmSysHardDiskRemainLifeCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLifeCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLifeCriticalThreshold.setUnits(" % ")
_CmmSysHardDiskRemainLife_Type = Integer32
_CmmSysHardDiskRemainLife_Object = MibTableColumn
cmmSysHardDiskRemainLife = _CmmSysHardDiskRemainLife_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 17),
    _CmmSysHardDiskRemainLife_Type()
)
cmmSysHardDiskRemainLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLife.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLife.setUnits(" % ")
_CmmSysHardDiskAvailableReservedSpaceAlertThreshold_Type = Integer32
_CmmSysHardDiskAvailableReservedSpaceAlertThreshold_Object = MibTableColumn
cmmSysHardDiskAvailableReservedSpaceAlertThreshold = _CmmSysHardDiskAvailableReservedSpaceAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 18),
    _CmmSysHardDiskAvailableReservedSpaceAlertThreshold_Type()
)
cmmSysHardDiskAvailableReservedSpaceAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpaceAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpaceAlertThreshold.setUnits(" % ")
_CmmSysHardDiskAvailableReservedSpaceCriticalThreshold_Type = Integer32
_CmmSysHardDiskAvailableReservedSpaceCriticalThreshold_Object = MibTableColumn
cmmSysHardDiskAvailableReservedSpaceCriticalThreshold = _CmmSysHardDiskAvailableReservedSpaceCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 19),
    _CmmSysHardDiskAvailableReservedSpaceCriticalThreshold_Type()
)
cmmSysHardDiskAvailableReservedSpaceCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpaceCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpaceCriticalThreshold.setUnits(" % ")
_CmmSysHardDiskAvailableReservedSpace_Type = Integer32
_CmmSysHardDiskAvailableReservedSpace_Object = MibTableColumn
cmmSysHardDiskAvailableReservedSpace = _CmmSysHardDiskAvailableReservedSpace_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 20),
    _CmmSysHardDiskAvailableReservedSpace_Type()
)
cmmSysHardDiskAvailableReservedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpace.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpace.setUnits(" % ")
_CmmSysHardDiskReallocSectorsCount_Type = Integer32
_CmmSysHardDiskReallocSectorsCount_Object = MibTableColumn
cmmSysHardDiskReallocSectorsCount = _CmmSysHardDiskReallocSectorsCount_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 21),
    _CmmSysHardDiskReallocSectorsCount_Type()
)
cmmSysHardDiskReallocSectorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskReallocSectorsCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskReallocSectorsCount.setUnits(" 1 ")
_CmmSysHardDiskUncorrectSectorCount_Type = Integer32
_CmmSysHardDiskUncorrectSectorCount_Object = MibTableColumn
cmmSysHardDiskUncorrectSectorCount = _CmmSysHardDiskUncorrectSectorCount_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 22),
    _CmmSysHardDiskUncorrectSectorCount_Type()
)
cmmSysHardDiskUncorrectSectorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskUncorrectSectorCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskUncorrectSectorCount.setUnits(" 1 ")
_CmmSysHardDiskActivityMonitoringInterval_Type = Integer32
_CmmSysHardDiskActivityMonitoringInterval_Object = MibTableColumn
cmmSysHardDiskActivityMonitoringInterval = _CmmSysHardDiskActivityMonitoringInterval_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 23),
    _CmmSysHardDiskActivityMonitoringInterval_Type()
)
cmmSysHardDiskActivityMonitoringInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringInterval.setUnits(" Seconds ")
_CmmSysHardDiskActivityMonitoringRead_Type = Integer32
_CmmSysHardDiskActivityMonitoringRead_Object = MibTableColumn
cmmSysHardDiskActivityMonitoringRead = _CmmSysHardDiskActivityMonitoringRead_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 24),
    _CmmSysHardDiskActivityMonitoringRead_Type()
)
cmmSysHardDiskActivityMonitoringRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringRead.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringRead.setUnits(" kBps ")
_CmmSysHardDiskActivityMonitoringWrite_Type = Integer32
_CmmSysHardDiskActivityMonitoringWrite_Object = MibTableColumn
cmmSysHardDiskActivityMonitoringWrite = _CmmSysHardDiskActivityMonitoringWrite_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 25),
    _CmmSysHardDiskActivityMonitoringWrite_Type()
)
cmmSysHardDiskActivityMonitoringWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWrite.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWrite.setUnits(" kBps ")
_CmmSysHardDiskActivityMonitoringReadCurrent_Type = Integer32
_CmmSysHardDiskActivityMonitoringReadCurrent_Object = MibTableColumn
cmmSysHardDiskActivityMonitoringReadCurrent = _CmmSysHardDiskActivityMonitoringReadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 26),
    _CmmSysHardDiskActivityMonitoringReadCurrent_Type()
)
cmmSysHardDiskActivityMonitoringReadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringReadCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringReadCurrent.setUnits(" kBps ")
_CmmSysHardDiskActivityMonitoringWriteCurrent_Type = Integer32
_CmmSysHardDiskActivityMonitoringWriteCurrent_Object = MibTableColumn
cmmSysHardDiskActivityMonitoringWriteCurrent = _CmmSysHardDiskActivityMonitoringWriteCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 27),
    _CmmSysHardDiskActivityMonitoringWriteCurrent_Type()
)
cmmSysHardDiskActivityMonitoringWriteCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWriteCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWriteCurrent.setUnits(" kB/s ")
_CmmSysHardDiskActivityMonitoringReadThreshold_Type = Integer32
_CmmSysHardDiskActivityMonitoringReadThreshold_Object = MibTableColumn
cmmSysHardDiskActivityMonitoringReadThreshold = _CmmSysHardDiskActivityMonitoringReadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 28),
    _CmmSysHardDiskActivityMonitoringReadThreshold_Type()
)
cmmSysHardDiskActivityMonitoringReadThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringReadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringReadThreshold.setUnits(" kBps ")
_CmmSysHardDiskActivityMonitoringWriteThreshold_Type = Integer32
_CmmSysHardDiskActivityMonitoringWriteThreshold_Object = MibTableColumn
cmmSysHardDiskActivityMonitoringWriteThreshold = _CmmSysHardDiskActivityMonitoringWriteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 29),
    _CmmSysHardDiskActivityMonitoringWriteThreshold_Type()
)
cmmSysHardDiskActivityMonitoringWriteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWriteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWriteThreshold.setUnits(" kBps ")
_CmmSysHardDiskManufacturerId_Type = DisplayString
_CmmSysHardDiskManufacturerId_Object = MibTableColumn
cmmSysHardDiskManufacturerId = _CmmSysHardDiskManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 30),
    _CmmSysHardDiskManufacturerId_Type()
)
cmmSysHardDiskManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskManufacturerId.setStatus("current")
_CmmSysHardDiskManufactureDate_Type = DisplayString
_CmmSysHardDiskManufactureDate_Object = MibTableColumn
cmmSysHardDiskManufactureDate = _CmmSysHardDiskManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 31),
    _CmmSysHardDiskManufactureDate_Type()
)
cmmSysHardDiskManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskManufactureDate.setStatus("current")
_CmmSysHardDiskDeviceType_Type = DisplayString
_CmmSysHardDiskDeviceType_Object = MibTableColumn
cmmSysHardDiskDeviceType = _CmmSysHardDiskDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 32),
    _CmmSysHardDiskDeviceType_Type()
)
cmmSysHardDiskDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskDeviceType.setStatus("current")
_CmmSysHardDiskCacheSize_Type = Integer32
_CmmSysHardDiskCacheSize_Object = MibTableColumn
cmmSysHardDiskCacheSize = _CmmSysHardDiskCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 33),
    _CmmSysHardDiskCacheSize_Type()
)
cmmSysHardDiskCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskCacheSize.setUnits(" KBytes ")


class _CmmSysHardDiskStorageStatus_Type(Integer32):
    """Custom type cmmSysHardDiskStorageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-100002,
              -100001,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -100002),
          ("unavailable", -100001),
          ("normal", 1),
          ("critical", 2),
          ("alert", 3),
          ("undefined", 4))
    )


_CmmSysHardDiskStorageStatus_Type.__name__ = "Integer32"
_CmmSysHardDiskStorageStatus_Object = MibTableColumn
cmmSysHardDiskStorageStatus = _CmmSysHardDiskStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 34),
    _CmmSysHardDiskStorageStatus_Type()
)
cmmSysHardDiskStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskStorageStatus.setStatus("current")
_CmmSystemStatusTable_Object = MibTable
cmmSystemStatusTable = _CmmSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cmmSystemStatusTable.setStatus("current")
_CmmSystemStatusEntry_Object = MibTableRow
cmmSystemStatusEntry = _CmmSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1)
)
cmmSystemStatusEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSystemStatusEntry.setStatus("current")
_CmmSystemMinorFaultStatus_Type = SystemStatusCode
_CmmSystemMinorFaultStatus_Object = MibTableColumn
cmmSystemMinorFaultStatus = _CmmSystemMinorFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 1),
    _CmmSystemMinorFaultStatus_Type()
)
cmmSystemMinorFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSystemMinorFaultStatus.setStatus("current")
_CmmSystemMajorFaultStatus_Type = SystemStatusCode
_CmmSystemMajorFaultStatus_Object = MibTableColumn
cmmSystemMajorFaultStatus = _CmmSystemMajorFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 2),
    _CmmSystemMajorFaultStatus_Type()
)
cmmSystemMajorFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSystemMajorFaultStatus.setStatus("current")


class _CmmSysStatus_Type(Integer32):
    """Custom type cmmSysStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysStatus_Type.__name__ = "Integer32"
_CmmSysStatus_Object = MibTableColumn
cmmSysStatus = _CmmSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 3),
    _CmmSysStatus_Type()
)
cmmSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysStatus.setStatus("current")
_CmmSysLedColor_Type = LedColorCode
_CmmSysLedColor_Object = MibTableColumn
cmmSysLedColor = _CmmSysLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 4),
    _CmmSysLedColor_Type()
)
cmmSysLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysLedColor.setStatus("current")
_CmmCpuCoreUtilTable_Object = MibTable
cmmCpuCoreUtilTable = _CmmCpuCoreUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilTable.setStatus("current")
_CmmCpuCoreUtilEntry_Object = MibTableRow
cmmCpuCoreUtilEntry = _CmmCpuCoreUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1)
)
cmmCpuCoreUtilEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmCpuCoreIndex"),
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilEntry.setStatus("current")


class _CmmCpuCoreIndex_Type(Integer32):
    """Custom type cmmCpuCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmCpuCoreIndex_Type.__name__ = "Integer32"
_CmmCpuCoreIndex_Object = MibTableColumn
cmmCpuCoreIndex = _CmmCpuCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1, 1),
    _CmmCpuCoreIndex_Type()
)
cmmCpuCoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmCpuCoreIndex.setStatus("current")
_CmmCpuCoreUtilization_Type = Integer32
_CmmCpuCoreUtilization_Object = MibTableColumn
cmmCpuCoreUtilization = _CmmCpuCoreUtilization_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1, 2),
    _CmmCpuCoreUtilization_Type()
)
cmmCpuCoreUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCpuCoreUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cmmCpuCoreUtilization.setUnits("0.01 %")
_CmmCpuCoreModelName_Type = DisplayString
_CmmCpuCoreModelName_Object = MibTableColumn
cmmCpuCoreModelName = _CmmCpuCoreModelName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1, 3),
    _CmmCpuCoreModelName_Type()
)
cmmCpuCoreModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCpuCoreModelName.setStatus("current")
_CmmPsuFruTable_Object = MibTable
cmmPsuFruTable = _CmmPsuFruTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17)
)
if mibBuilder.loadTexts:
    cmmPsuFruTable.setStatus("current")
_CmmPsuFruEntry_Object = MibTableRow
cmmPsuFruEntry = _CmmPsuFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1)
)
cmmPsuFruEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
)
if mibBuilder.loadTexts:
    cmmPsuFruEntry.setStatus("current")
_CmmPsuPpid_Type = DisplayString
_CmmPsuPpid_Object = MibTableColumn
cmmPsuPpid = _CmmPsuPpid_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 1),
    _CmmPsuPpid_Type()
)
cmmPsuPpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPpid.setStatus("current")
_CmmPsuCountryofOrigin_Type = DisplayString
_CmmPsuCountryofOrigin_Object = MibTableColumn
cmmPsuCountryofOrigin = _CmmPsuCountryofOrigin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 2),
    _CmmPsuCountryofOrigin_Type()
)
cmmPsuCountryofOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuCountryofOrigin.setStatus("current")
_CmmPsuPpidPartNum_Type = DisplayString
_CmmPsuPpidPartNum_Object = MibTableColumn
cmmPsuPpidPartNum = _CmmPsuPpidPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 3),
    _CmmPsuPpidPartNum_Type()
)
cmmPsuPpidPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPpidPartNum.setStatus("current")
_CmmPsuPpidPartNumRev_Type = DisplayString
_CmmPsuPpidPartNumRev_Object = MibTableColumn
cmmPsuPpidPartNumRev = _CmmPsuPpidPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 4),
    _CmmPsuPpidPartNumRev_Type()
)
cmmPsuPpidPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPpidPartNumRev.setStatus("current")
_CmmPsuManufactureId_Type = DisplayString
_CmmPsuManufactureId_Object = MibTableColumn
cmmPsuManufactureId = _CmmPsuManufactureId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 5),
    _CmmPsuManufactureId_Type()
)
cmmPsuManufactureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuManufactureId.setStatus("current")


class _CmmPsuDateCode_Type(OctetString):
    """Custom type cmmPsuDateCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )


_CmmPsuDateCode_Type.__name__ = "OctetString"
_CmmPsuDateCode_Object = MibTableColumn
cmmPsuDateCode = _CmmPsuDateCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 6),
    _CmmPsuDateCode_Type()
)
cmmPsuDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuDateCode.setStatus("current")
_CmmPsuSerialNumber_Type = DisplayString
_CmmPsuSerialNumber_Object = MibTableColumn
cmmPsuSerialNumber = _CmmPsuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 7),
    _CmmPsuSerialNumber_Type()
)
cmmPsuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuSerialNumber.setStatus("current")
_CmmPsuPartNum_Type = DisplayString
_CmmPsuPartNum_Object = MibTableColumn
cmmPsuPartNum = _CmmPsuPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 8),
    _CmmPsuPartNum_Type()
)
cmmPsuPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPartNum.setStatus("current")
_CmmPsuPartNumRev_Type = DisplayString
_CmmPsuPartNumRev_Object = MibTableColumn
cmmPsuPartNumRev = _CmmPsuPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 9),
    _CmmPsuPartNumRev_Type()
)
cmmPsuPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPartNumRev.setStatus("current")
_CmmPsuNumOfFanPerTray_Type = Integer32
_CmmPsuNumOfFanPerTray_Object = MibTableColumn
cmmPsuNumOfFanPerTray = _CmmPsuNumOfFanPerTray_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 10),
    _CmmPsuNumOfFanPerTray_Type()
)
cmmPsuNumOfFanPerTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuNumOfFanPerTray.setStatus("current")


class _CmmPsuType_Type(Integer32):
    """Custom type cmmPsuType based on Integer32"""
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
        *(("ac-normal", 1),
          ("ac-reverse", 2),
          ("dc-normal", 3),
          ("dc-reverse", 4),
          ("not-applicable", 5))
    )


_CmmPsuType_Type.__name__ = "Integer32"
_CmmPsuType_Object = MibTableColumn
cmmPsuType = _CmmPsuType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 11),
    _CmmPsuType_Type()
)
cmmPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuType.setStatus("current")
_CmmPsuServiceTag_Type = DisplayString
_CmmPsuServiceTag_Object = MibTableColumn
cmmPsuServiceTag = _CmmPsuServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 12),
    _CmmPsuServiceTag_Type()
)
cmmPsuServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuServiceTag.setStatus("current")
_CmmPsuIanaNum_Type = DisplayString
_CmmPsuIanaNum_Object = MibTableColumn
cmmPsuIanaNum = _CmmPsuIanaNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 13),
    _CmmPsuIanaNum_Type()
)
cmmPsuIanaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuIanaNum.setStatus("current")
_CmmPsuFanMaxRpm_Type = Integer32
_CmmPsuFanMaxRpm_Object = MibTableColumn
cmmPsuFanMaxRpm = _CmmPsuFanMaxRpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 14),
    _CmmPsuFanMaxRpm_Type()
)
cmmPsuFanMaxRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuFanMaxRpm.setStatus("current")
_CmmPsuAirFlowDir_Type = DisplayString
_CmmPsuAirFlowDir_Object = MibTableColumn
cmmPsuAirFlowDir = _CmmPsuAirFlowDir_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 15),
    _CmmPsuAirFlowDir_Type()
)
cmmPsuAirFlowDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuAirFlowDir.setStatus("current")
_CmmPsuMaxOutputWatt_Type = Integer32
_CmmPsuMaxOutputWatt_Object = MibTableColumn
cmmPsuMaxOutputWatt = _CmmPsuMaxOutputWatt_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 16),
    _CmmPsuMaxOutputWatt_Type()
)
cmmPsuMaxOutputWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuMaxOutputWatt.setStatus("current")
_CmmFanFruTable_Object = MibTable
cmmFanFruTable = _CmmFanFruTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18)
)
if mibBuilder.loadTexts:
    cmmFanFruTable.setStatus("current")
_CmmFanFruEntry_Object = MibTableRow
cmmFanFruEntry = _CmmFanFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1)
)
cmmFanFruEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
)
if mibBuilder.loadTexts:
    cmmFanFruEntry.setStatus("current")
_CmmFanPpid_Type = DisplayString
_CmmFanPpid_Object = MibTableColumn
cmmFanPpid = _CmmFanPpid_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 1),
    _CmmFanPpid_Type()
)
cmmFanPpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPpid.setStatus("current")
_CmmFanCountryofOrigin_Type = DisplayString
_CmmFanCountryofOrigin_Object = MibTableColumn
cmmFanCountryofOrigin = _CmmFanCountryofOrigin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 2),
    _CmmFanCountryofOrigin_Type()
)
cmmFanCountryofOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanCountryofOrigin.setStatus("current")
_CmmFanPpidPartNum_Type = DisplayString
_CmmFanPpidPartNum_Object = MibTableColumn
cmmFanPpidPartNum = _CmmFanPpidPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 3),
    _CmmFanPpidPartNum_Type()
)
cmmFanPpidPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPpidPartNum.setStatus("current")
_CmmFanPpidPartNumRev_Type = DisplayString
_CmmFanPpidPartNumRev_Object = MibTableColumn
cmmFanPpidPartNumRev = _CmmFanPpidPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 4),
    _CmmFanPpidPartNumRev_Type()
)
cmmFanPpidPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPpidPartNumRev.setStatus("current")
_CmmFanManufactureId_Type = DisplayString
_CmmFanManufactureId_Object = MibTableColumn
cmmFanManufactureId = _CmmFanManufactureId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 5),
    _CmmFanManufactureId_Type()
)
cmmFanManufactureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanManufactureId.setStatus("current")
_CmmFanDateCode_Type = DisplayString
_CmmFanDateCode_Object = MibTableColumn
cmmFanDateCode = _CmmFanDateCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 6),
    _CmmFanDateCode_Type()
)
cmmFanDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanDateCode.setStatus("current")
_CmmFanSerialNumber_Type = DisplayString
_CmmFanSerialNumber_Object = MibTableColumn
cmmFanSerialNumber = _CmmFanSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 7),
    _CmmFanSerialNumber_Type()
)
cmmFanSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanSerialNumber.setStatus("current")
_CmmFanPartNum_Type = DisplayString
_CmmFanPartNum_Object = MibTableColumn
cmmFanPartNum = _CmmFanPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 8),
    _CmmFanPartNum_Type()
)
cmmFanPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPartNum.setStatus("current")
_CmmFanPartNumRev_Type = DisplayString
_CmmFanPartNumRev_Object = MibTableColumn
cmmFanPartNumRev = _CmmFanPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 9),
    _CmmFanPartNumRev_Type()
)
cmmFanPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPartNumRev.setStatus("current")
_CmmFanNumOfFanPerTray_Type = Integer32
_CmmFanNumOfFanPerTray_Object = MibTableColumn
cmmFanNumOfFanPerTray = _CmmFanNumOfFanPerTray_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 10),
    _CmmFanNumOfFanPerTray_Type()
)
cmmFanNumOfFanPerTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanNumOfFanPerTray.setStatus("current")


class _CmmFanType_Type(Integer32):
    """Custom type cmmFanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blow-outfan", 1),
          ("blow-infan", 2),
          ("fan-type-unknown", 3))
    )


_CmmFanType_Type.__name__ = "Integer32"
_CmmFanType_Object = MibTableColumn
cmmFanType = _CmmFanType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 11),
    _CmmFanType_Type()
)
cmmFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanType.setStatus("current")
_CmmFanServiceTag_Type = DisplayString
_CmmFanServiceTag_Object = MibTableColumn
cmmFanServiceTag = _CmmFanServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 12),
    _CmmFanServiceTag_Type()
)
cmmFanServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanServiceTag.setStatus("current")
_CmmFanIanaNum_Type = DisplayString
_CmmFanIanaNum_Object = MibTableColumn
cmmFanIanaNum = _CmmFanIanaNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 13),
    _CmmFanIanaNum_Type()
)
cmmFanIanaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanIanaNum.setStatus("current")
_CmmFanMaxRpm_Type = Integer32
_CmmFanMaxRpm_Object = MibTableColumn
cmmFanMaxRpm = _CmmFanMaxRpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 14),
    _CmmFanMaxRpm_Type()
)
cmmFanMaxRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanMaxRpm.setStatus("current")
_CmmSysCpldTable_Object = MibTable
cmmSysCpldTable = _CmmSysCpldTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19)
)
if mibBuilder.loadTexts:
    cmmSysCpldTable.setStatus("current")
_CmmSysCpldEntry_Object = MibTableRow
cmmSysCpldEntry = _CmmSysCpldEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1)
)
cmmSysCpldEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmSysCpldIndex"),
)
if mibBuilder.loadTexts:
    cmmSysCpldEntry.setStatus("current")


class _CmmSysCpldIndex_Type(Integer32):
    """Custom type cmmSysCpldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmSysCpldIndex_Type.__name__ = "Integer32"
_CmmSysCpldIndex_Object = MibTableColumn
cmmSysCpldIndex = _CmmSysCpldIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 1),
    _CmmSysCpldIndex_Type()
)
cmmSysCpldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmSysCpldIndex.setStatus("current")
_CmmSysCpldName_Type = DisplayString
_CmmSysCpldName_Object = MibTableColumn
cmmSysCpldName = _CmmSysCpldName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 2),
    _CmmSysCpldName_Type()
)
cmmSysCpldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpldName.setStatus("current")
_CmmSysCpldSupportedVer_Type = DisplayString
_CmmSysCpldSupportedVer_Object = MibTableColumn
cmmSysCpldSupportedVer = _CmmSysCpldSupportedVer_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 3),
    _CmmSysCpldSupportedVer_Type()
)
cmmSysCpldSupportedVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpldSupportedVer.setStatus("current")
_CmmSysCpldCurrentVer_Type = DisplayString
_CmmSysCpldCurrentVer_Object = MibTableColumn
cmmSysCpldCurrentVer = _CmmSysCpldCurrentVer_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 4),
    _CmmSysCpldCurrentVer_Type()
)
cmmSysCpldCurrentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpldCurrentVer.setStatus("current")
_CmmTransDDMPage20h21hTable_Object = MibTable
cmmTransDDMPage20h21hTable = _CmmTransDDMPage20h21hTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20)
)
if mibBuilder.loadTexts:
    cmmTransDDMPage20h21hTable.setStatus("current")
_CmmTransDDMPage20h21hEntry_Object = MibTableRow
cmmTransDDMPage20h21hEntry = _CmmTransDDMPage20h21hEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1)
)
cmmTransDDMPage20h21hEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
)
if mibBuilder.loadTexts:
    cmmTransDDMPage20h21hEntry.setStatus("current")
_CmmTransPreFecBerVal_Type = ErrorFigures
_CmmTransPreFecBerVal_Object = MibTableColumn
cmmTransPreFecBerVal = _CmmTransPreFecBerVal_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 1),
    _CmmTransPreFecBerVal_Type()
)
cmmTransPreFecBerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPreFecBerVal.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransPreFecBerVal.setUnits("BER")
_CmmTransPreFecBerCriticMin_Type = ErrorFigures
_CmmTransPreFecBerCriticMin_Object = MibTableColumn
cmmTransPreFecBerCriticMin = _CmmTransPreFecBerCriticMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 2),
    _CmmTransPreFecBerCriticMin_Type()
)
cmmTransPreFecBerCriticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticMin.setUnits("BER")
_CmmTransPreFecBerCriticMax_Type = ErrorFigures
_CmmTransPreFecBerCriticMax_Object = MibTableColumn
cmmTransPreFecBerCriticMax = _CmmTransPreFecBerCriticMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 3),
    _CmmTransPreFecBerCriticMax_Type()
)
cmmTransPreFecBerCriticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticMax.setUnits("BER")
_CmmTransPreFecBerCriticalMin_Type = ErrorFigures
_CmmTransPreFecBerCriticalMin_Object = MibTableColumn
cmmTransPreFecBerCriticalMin = _CmmTransPreFecBerCriticalMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 4),
    _CmmTransPreFecBerCriticalMin_Type()
)
cmmTransPreFecBerCriticalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticalMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticalMin.setUnits("BER")
_CmmTransPreFecBerCriticalMax_Type = ErrorFigures
_CmmTransPreFecBerCriticalMax_Object = MibTableColumn
cmmTransPreFecBerCriticalMax = _CmmTransPreFecBerCriticalMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 5),
    _CmmTransPreFecBerCriticalMax_Type()
)
cmmTransPreFecBerCriticalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticalMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransPreFecBerCriticalMax.setUnits("BER")
_CmmTransUncorrectedBerVal_Type = ErrorFigures
_CmmTransUncorrectedBerVal_Object = MibTableColumn
cmmTransUncorrectedBerVal = _CmmTransUncorrectedBerVal_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 6),
    _CmmTransUncorrectedBerVal_Type()
)
cmmTransUncorrectedBerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerVal.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerVal.setUnits("BER")
_CmmTransUncorrectedBerValCriticMin_Type = ErrorFigures
_CmmTransUncorrectedBerValCriticMin_Object = MibTableColumn
cmmTransUncorrectedBerValCriticMin = _CmmTransUncorrectedBerValCriticMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 7),
    _CmmTransUncorrectedBerValCriticMin_Type()
)
cmmTransUncorrectedBerValCriticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticMin.setUnits("BER")
_CmmTransUncorrectedBerValCriticMax_Type = ErrorFigures
_CmmTransUncorrectedBerValCriticMax_Object = MibTableColumn
cmmTransUncorrectedBerValCriticMax = _CmmTransUncorrectedBerValCriticMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 8),
    _CmmTransUncorrectedBerValCriticMax_Type()
)
cmmTransUncorrectedBerValCriticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticMax.setUnits("BER")
_CmmTransUncorrectedBerValCriticalMin_Type = ErrorFigures
_CmmTransUncorrectedBerValCriticalMin_Object = MibTableColumn
cmmTransUncorrectedBerValCriticalMin = _CmmTransUncorrectedBerValCriticalMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 9),
    _CmmTransUncorrectedBerValCriticalMin_Type()
)
cmmTransUncorrectedBerValCriticalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticalMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticalMin.setUnits("BER")
_CmmTransUncorrectedBerValCriticalMax_Type = ErrorFigures
_CmmTransUncorrectedBerValCriticalMax_Object = MibTableColumn
cmmTransUncorrectedBerValCriticalMax = _CmmTransUncorrectedBerValCriticalMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 10),
    _CmmTransUncorrectedBerValCriticalMax_Type()
)
cmmTransUncorrectedBerValCriticalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticalMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransUncorrectedBerValCriticalMax.setUnits("BER")
_CmmTransSnrVal_Type = Integer32
_CmmTransSnrVal_Object = MibTableColumn
cmmTransSnrVal = _CmmTransSnrVal_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 11),
    _CmmTransSnrVal_Type()
)
cmmTransSnrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSnrVal.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransSnrVal.setUnits("0.001 dB")
_CmmTransSnrCriticMin_Type = Integer32
_CmmTransSnrCriticMin_Object = MibTableColumn
cmmTransSnrCriticMin = _CmmTransSnrCriticMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 12),
    _CmmTransSnrCriticMin_Type()
)
cmmTransSnrCriticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSnrCriticMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransSnrCriticMin.setUnits("0.001 dB")
_CmmTransSnrCriticMax_Type = Integer32
_CmmTransSnrCriticMax_Object = MibTableColumn
cmmTransSnrCriticMax = _CmmTransSnrCriticMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 13),
    _CmmTransSnrCriticMax_Type()
)
cmmTransSnrCriticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSnrCriticMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransSnrCriticMax.setUnits("0.001 dB")
_CmmTransSnrCriticalMin_Type = Integer32
_CmmTransSnrCriticalMin_Object = MibTableColumn
cmmTransSnrCriticalMin = _CmmTransSnrCriticalMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 14),
    _CmmTransSnrCriticalMin_Type()
)
cmmTransSnrCriticalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSnrCriticalMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransSnrCriticalMin.setUnits("0.001 dB")
_CmmTransSnrCriticalMax_Type = Integer32
_CmmTransSnrCriticalMax_Object = MibTableColumn
cmmTransSnrCriticalMax = _CmmTransSnrCriticalMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 15),
    _CmmTransSnrCriticalMax_Type()
)
cmmTransSnrCriticalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSnrCriticalMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransSnrCriticalMax.setUnits("0.001 dB")
_CmmTransResIsiVal_Type = Integer32
_CmmTransResIsiVal_Object = MibTableColumn
cmmTransResIsiVal = _CmmTransResIsiVal_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 16),
    _CmmTransResIsiVal_Type()
)
cmmTransResIsiVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransResIsiVal.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransResIsiVal.setUnits("0.001 ps/nm")
_CmmTransResIsiCriticMin_Type = Integer32
_CmmTransResIsiCriticMin_Object = MibTableColumn
cmmTransResIsiCriticMin = _CmmTransResIsiCriticMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 17),
    _CmmTransResIsiCriticMin_Type()
)
cmmTransResIsiCriticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticMin.setUnits("0.001 ps/nm")
_CmmTransResIsiCriticMax_Type = Integer32
_CmmTransResIsiCriticMax_Object = MibTableColumn
cmmTransResIsiCriticMax = _CmmTransResIsiCriticMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 18),
    _CmmTransResIsiCriticMax_Type()
)
cmmTransResIsiCriticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticMax.setUnits("0.001 ps/nm")
_CmmTransResIsiCriticalMin_Type = Integer32
_CmmTransResIsiCriticalMin_Object = MibTableColumn
cmmTransResIsiCriticalMin = _CmmTransResIsiCriticalMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 19),
    _CmmTransResIsiCriticalMin_Type()
)
cmmTransResIsiCriticalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticalMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticalMin.setUnits("0.001 ps/nm")
_CmmTransResIsiCriticalMax_Type = Integer32
_CmmTransResIsiCriticalMax_Object = MibTableColumn
cmmTransResIsiCriticalMax = _CmmTransResIsiCriticalMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 20),
    _CmmTransResIsiCriticalMax_Type()
)
cmmTransResIsiCriticalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticalMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransResIsiCriticalMax.setUnits("0.001 ps/nm")
_CmmTransLvlTransVal_Type = Integer32
_CmmTransLvlTransVal_Object = MibTableColumn
cmmTransLvlTransVal = _CmmTransLvlTransVal_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 21),
    _CmmTransLvlTransVal_Type()
)
cmmTransLvlTransVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLvlTransVal.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLvlTransVal.setUnits("0.001 dB")
_CmmTransLvlTransCriticMin_Type = Integer32
_CmmTransLvlTransCriticMin_Object = MibTableColumn
cmmTransLvlTransCriticMin = _CmmTransLvlTransCriticMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 22),
    _CmmTransLvlTransCriticMin_Type()
)
cmmTransLvlTransCriticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticMin.setUnits("0.001 dB")
_CmmTransLvlTransCriticMax_Type = Integer32
_CmmTransLvlTransCriticMax_Object = MibTableColumn
cmmTransLvlTransCriticMax = _CmmTransLvlTransCriticMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 23),
    _CmmTransLvlTransCriticMax_Type()
)
cmmTransLvlTransCriticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticMax.setUnits("0.001 dB")
_CmmTransLvlTransCriticalMin_Type = Integer32
_CmmTransLvlTransCriticalMin_Object = MibTableColumn
cmmTransLvlTransCriticalMin = _CmmTransLvlTransCriticalMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 24),
    _CmmTransLvlTransCriticalMin_Type()
)
cmmTransLvlTransCriticalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticalMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticalMin.setUnits("0.001 dB")
_CmmTransLvlTransCriticalMax_Type = Integer32
_CmmTransLvlTransCriticalMax_Object = MibTableColumn
cmmTransLvlTransCriticalMax = _CmmTransLvlTransCriticalMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 25),
    _CmmTransLvlTransCriticalMax_Type()
)
cmmTransLvlTransCriticalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticalMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLvlTransCriticalMax.setUnits("0.001 dB")
_CmmTransTecCurrErrVal_Type = Integer32
_CmmTransTecCurrErrVal_Object = MibTableColumn
cmmTransTecCurrErrVal = _CmmTransTecCurrErrVal_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 26),
    _CmmTransTecCurrErrVal_Type()
)
cmmTransTecCurrErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrVal.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrVal.setUnits("0.001 mA")
_CmmTransTecCurrErrCriticMin_Type = Integer32
_CmmTransTecCurrErrCriticMin_Object = MibTableColumn
cmmTransTecCurrErrCriticMin = _CmmTransTecCurrErrCriticMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 27),
    _CmmTransTecCurrErrCriticMin_Type()
)
cmmTransTecCurrErrCriticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticMin.setUnits("0.001 mA")
_CmmTransTecCurrErrCriticMax_Type = Integer32
_CmmTransTecCurrErrCriticMax_Object = MibTableColumn
cmmTransTecCurrErrCriticMax = _CmmTransTecCurrErrCriticMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 28),
    _CmmTransTecCurrErrCriticMax_Type()
)
cmmTransTecCurrErrCriticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticMax.setUnits("0.001 mA")
_CmmTransTecCurrErrCriticalMin_Type = Integer32
_CmmTransTecCurrErrCriticalMin_Object = MibTableColumn
cmmTransTecCurrErrCriticalMin = _CmmTransTecCurrErrCriticalMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 29),
    _CmmTransTecCurrErrCriticalMin_Type()
)
cmmTransTecCurrErrCriticalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticalMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticalMin.setUnits("0.001 mA")
_CmmTransTecCurrErrCriticalMax_Type = Integer32
_CmmTransTecCurrErrCriticalMax_Object = MibTableColumn
cmmTransTecCurrErrCriticalMax = _CmmTransTecCurrErrCriticalMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 30),
    _CmmTransTecCurrErrCriticalMax_Type()
)
cmmTransTecCurrErrCriticalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticalMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTecCurrErrCriticalMax.setUnits("0.001 mA")
_CmmTransLaserTempVal_Type = Integer32
_CmmTransLaserTempVal_Object = MibTableColumn
cmmTransLaserTempVal = _CmmTransLaserTempVal_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 31),
    _CmmTransLaserTempVal_Type()
)
cmmTransLaserTempVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserTempVal.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserTempVal.setUnits("0.001 C")
_CmmTransLaserTempCriticMin_Type = Integer32
_CmmTransLaserTempCriticMin_Object = MibTableColumn
cmmTransLaserTempCriticMin = _CmmTransLaserTempCriticMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 32),
    _CmmTransLaserTempCriticMin_Type()
)
cmmTransLaserTempCriticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticMin.setUnits("0.001 C")
_CmmTransLaserTempCriticMax_Type = Integer32
_CmmTransLaserTempCriticMax_Object = MibTableColumn
cmmTransLaserTempCriticMax = _CmmTransLaserTempCriticMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 33),
    _CmmTransLaserTempCriticMax_Type()
)
cmmTransLaserTempCriticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticMax.setUnits("0.001 C")
_CmmTransLaserTempCriticalMin_Type = Integer32
_CmmTransLaserTempCriticalMin_Object = MibTableColumn
cmmTransLaserTempCriticalMin = _CmmTransLaserTempCriticalMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 34),
    _CmmTransLaserTempCriticalMin_Type()
)
cmmTransLaserTempCriticalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticalMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticalMin.setUnits("0.001 C")
_CmmTransLaserTempCriticalMax_Type = Integer32
_CmmTransLaserTempCriticalMax_Object = MibTableColumn
cmmTransLaserTempCriticalMax = _CmmTransLaserTempCriticalMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 20, 1, 35),
    _CmmTransLaserTempCriticalMax_Type()
)
cmmTransLaserTempCriticalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticalMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserTempCriticalMax.setUnits("0.001 C")
_CmmSysHardDiskPartitionTable_Object = MibTable
cmmSysHardDiskPartitionTable = _CmmSysHardDiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 21)
)
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionTable.setStatus("current")
_CmmSysHardDiskPartitionEntry_Object = MibTableRow
cmmSysHardDiskPartitionEntry = _CmmSysHardDiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 21, 1)
)
cmmSysHardDiskPartitionEntry.setIndexNames(
    (0, "IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskPartitionIndex"),
)
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionEntry.setStatus("current")


class _CmmSysHardDiskPartitionIndex_Type(Integer32):
    """Custom type cmmSysHardDiskPartitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmSysHardDiskPartitionIndex_Type.__name__ = "Integer32"
_CmmSysHardDiskPartitionIndex_Object = MibTableColumn
cmmSysHardDiskPartitionIndex = _CmmSysHardDiskPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 21, 1, 1),
    _CmmSysHardDiskPartitionIndex_Type()
)
cmmSysHardDiskPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionIndex.setStatus("current")
_CmmSysHardDiskPartitionName_Type = DisplayString
_CmmSysHardDiskPartitionName_Object = MibTableColumn
cmmSysHardDiskPartitionName = _CmmSysHardDiskPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 21, 1, 2),
    _CmmSysHardDiskPartitionName_Type()
)
cmmSysHardDiskPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionName.setStatus("current")
_CmmSysHardDiskPartitionTotalMem_Type = Integer32
_CmmSysHardDiskPartitionTotalMem_Object = MibTableColumn
cmmSysHardDiskPartitionTotalMem = _CmmSysHardDiskPartitionTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 21, 1, 3),
    _CmmSysHardDiskPartitionTotalMem_Type()
)
cmmSysHardDiskPartitionTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionTotalMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionTotalMem.setUnits(" MBytes ")
_CmmSysHardDiskPartitionUsedMem_Type = Integer32
_CmmSysHardDiskPartitionUsedMem_Object = MibTableColumn
cmmSysHardDiskPartitionUsedMem = _CmmSysHardDiskPartitionUsedMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 21, 1, 4),
    _CmmSysHardDiskPartitionUsedMem_Type()
)
cmmSysHardDiskPartitionUsedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionUsedMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionUsedMem.setUnits(" MBytes ")
_CmmSysHardDiskPartitionFreeMem_Type = Integer32
_CmmSysHardDiskPartitionFreeMem_Object = MibTableColumn
cmmSysHardDiskPartitionFreeMem = _CmmSysHardDiskPartitionFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 21, 1, 5),
    _CmmSysHardDiskPartitionFreeMem_Type()
)
cmmSysHardDiskPartitionFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionFreeMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHardDiskPartitionFreeMem.setUnits(" MBytes ")
_CmmAlarmObjects_ObjectIdentity = ObjectIdentity
cmmAlarmObjects = _CmmAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3)
)
_CmmAlarmVariable_ObjectIdentity = ObjectIdentity
cmmAlarmVariable = _CmmAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 0)
)
_CmmAlarmVarInteger_Type = Integer32
_CmmAlarmVarInteger_Object = MibScalar
cmmAlarmVarInteger = _CmmAlarmVarInteger_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 0, 1),
    _CmmAlarmVarInteger_Type()
)
cmmAlarmVarInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmAlarmVarInteger.setStatus("current")
_CmmAlarmVarString_Type = OctetString
_CmmAlarmVarString_Object = MibScalar
cmmAlarmVarString = _CmmAlarmVarString_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 0, 2),
    _CmmAlarmVarString_Type()
)
cmmAlarmVarString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmAlarmVarString.setStatus("current")
_CmmAlarmMibNotifications_ObjectIdentity = ObjectIdentity
cmmAlarmMibNotifications = _CmmAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1)
)
_CmmTransMibNotifications_ObjectIdentity = ObjectIdentity
cmmTransMibNotifications = _CmmTransMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2)
)

# Managed Objects groups


# Notification objects

cmmCpuLoad15MinAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 1)
)
cmmCpuLoad15MinAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad15minAlertThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad15Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad15MinAlert.setStatus(
        "current"
    )

cmmCpuLoad5MinAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 2)
)
cmmCpuLoad5MinAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad5minAlertThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad5Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad5MinAlert.setStatus(
        "current"
    )

cmmCpuLoad1MinCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 3)
)
cmmCpuLoad1MinCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad1minCriticalThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinCritical.setStatus(
        "current"
    )

cmmCpuLoad1MinAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 4)
)
cmmCpuLoad1MinAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad1minAlertThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinAlert.setStatus(
        "current"
    )

cmmCpuLoad1MinCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 5)
)
cmmCpuLoad1MinCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad1minCriticalThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinCriticalRecovery.setStatus(
        "current"
    )

cmmCpuLoad15MinAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 6)
)
cmmCpuLoad15MinAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad15minAlertThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad15Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad15MinAlertRecovery.setStatus(
        "current"
    )

cmmCpuLoad5MinAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 7)
)
cmmCpuLoad5MinAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad5minAlertThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad5Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad5MinAlertRecovery.setStatus(
        "current"
    )

cmmCpuLoad1MinAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 8)
)
cmmCpuLoad1MinAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackCpuLoad1minAlertThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinAlertRecovery.setStatus(
        "current"
    )

cmmCpuCoreUtilHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 9)
)
cmmCpuCoreUtilHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilCriticalThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighCritical.setStatus(
        "current"
    )

cmmCpuCoreUtilHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 10)
)
cmmCpuCoreUtilHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilAlertThreshold"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighAlert.setStatus(
        "current"
    )

cmmCpuCoreUtilHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 11)
)
cmmCpuCoreUtilHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighCriticalRecovery.setStatus(
        "current"
    )

cmmCpuCoreUtilHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 12)
)
cmmCpuCoreUtilHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighAlertRecovery.setStatus(
        "current"
    )

cmmRamUsageRisingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 21)
)
cmmRamUsageRisingCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageRisingCritical.setStatus(
        "current"
    )

cmmRamUsageRisingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 22)
)
cmmRamUsageRisingAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageRisingAlert.setStatus(
        "current"
    )

cmmRamUsageCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 23)
)
cmmRamUsageCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageCriticalRecovery.setStatus(
        "current"
    )

cmmRamUsageAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 24)
)
cmmRamUsageAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysRamAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageAlertRecovery.setStatus(
        "current"
    )

cmmHardDiskUsageRisingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 25)
)
cmmHardDiskUsageRisingCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsageCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageRisingCritical.setStatus(
        "current"
    )

cmmHardDiskUsageRisingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 26)
)
cmmHardDiskUsageRisingAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsageAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageRisingAlert.setStatus(
        "current"
    )

cmmHardDiskUsageCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 27)
)
cmmHardDiskUsageCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsageCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageCriticalRecovery.setStatus(
        "current"
    )

cmmHardDiskUsageAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 28)
)
cmmHardDiskUsageAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHarddiskUsageAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageAlertRecovery.setStatus(
        "current"
    )

cmmSysHardDiskRemainLifeRisingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 29)
)
cmmSysHardDiskRemainLifeRisingAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskRemainLife"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskRemainLifeAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLifeRisingAlert.setStatus(
        "current"
    )

cmmSysHardDiskRemainLifeRisingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 30)
)
cmmSysHardDiskRemainLifeRisingCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskRemainLife"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskRemainLifeCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskRemainLifeRisingCritical.setStatus(
        "current"
    )

cmmSysHardDiskAvailableReservedSpaceAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 31)
)
cmmSysHardDiskAvailableReservedSpaceAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskAvailableReservedSpace"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskAvailableReservedSpaceAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpaceAlert.setStatus(
        "current"
    )

cmmSysHardDiskAvailableReservedSpaceCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 32)
)
cmmSysHardDiskAvailableReservedSpaceCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskAvailableReservedSpace"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskAvailableReservedSpaceCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskAvailableReservedSpaceCritical.setStatus(
        "current"
    )

cmmSysHardDiskReallocSectorsCountAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 33)
)
cmmSysHardDiskReallocSectorsCountAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskReallocSectorsCount"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskReallocSectorsCountAlert.setStatus(
        "current"
    )

cmmSysHardDiskUncorrectableSectorCountCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 34)
)
cmmSysHardDiskUncorrectableSectorCountCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskUncorrectSectorCount"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskUncorrectableSectorCountCritical.setStatus(
        "current"
    )

cmmSysHardDiskActivityMonitoringReadAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 35)
)
cmmSysHardDiskActivityMonitoringReadAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringRead"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringReadThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringReadAlert.setStatus(
        "current"
    )

cmmSysHardDiskActivityMonitoringReadRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 36)
)
cmmSysHardDiskActivityMonitoringReadRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringRead"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringReadThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringReadRecovery.setStatus(
        "current"
    )

cmmSysHardDiskActivityMonitoringWriteAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 37)
)
cmmSysHardDiskActivityMonitoringWriteAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringWrite"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringWriteThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWriteAlert.setStatus(
        "current"
    )

cmmSysHardDiskActivityMonitoringWriteRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 38)
)
cmmSysHardDiskActivityMonitoringWriteRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringWrite"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskActivityMonitoringWriteThreshold"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskActivityMonitoringWriteRecovery.setStatus(
        "current"
    )

cmmSysHardDiskStorageStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 39)
)
cmmSysHardDiskStorageStatusNotification.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysHardDiskStorageStatus"))
)
if mibBuilder.loadTexts:
    cmmSysHardDiskStorageStatusNotification.setStatus(
        "current"
    )

cmmTemperatureLowEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 41)
)
cmmTemperatureLowEmergency.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowEmergency.setStatus(
        "current"
    )

cmmTemperatureHighEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 42)
)
cmmTemperatureHighEmergency.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighEmergency.setStatus(
        "current"
    )

cmmTemperatureLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 43)
)
cmmTemperatureLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowCritical.setStatus(
        "current"
    )

cmmTemperatureHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 44)
)
cmmTemperatureHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighCritical.setStatus(
        "current"
    )

cmmTemperatureLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 45)
)
cmmTemperatureLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowAlert.setStatus(
        "current"
    )

cmmTemperatureHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 46)
)
cmmTemperatureHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighAlert.setStatus(
        "current"
    )

cmmTemperatureHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 47)
)
cmmTemperatureHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighCriticalRecovery.setStatus(
        "current"
    )

cmmTemperatureLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 48)
)
cmmTemperatureLowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowCriticalRecovery.setStatus(
        "current"
    )

cmmTemperatureHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 49)
)
cmmTemperatureHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighAlertRecovery.setStatus(
        "current"
    )

cmmTemperatureLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 50)
)
cmmTemperatureLowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowAlertRecovery.setStatus(
        "current"
    )

cmmPsuInsertedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 61)
)
cmmPsuInsertedNotify.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPowerSupplyOperStatus"),
        ("IPI-CMM-CHASSIS-MIB", "cmmPsuSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmPsuInsertedNotify.setStatus(
        "current"
    )

cmmPsuRemovedCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 62)
)
cmmPsuRemovedCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPowerSupplyOperStatus"),
        ("IPI-CMM-CHASSIS-MIB", "cmmPsuSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmPsuRemovedCritical.setStatus(
        "current"
    )

cmmPsuAcFailedCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 63)
)
cmmPsuAcFailedCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsuAcFailedCritical.setStatus(
        "current"
    )

cmmPsuAcRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 64)
)
cmmPsuAcRecover.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsuAcRecover.setStatus(
        "current"
    )

cmmPsu12vPgFailedCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 65)
)
cmmPsu12vPgFailedCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsu12vPgFailedCritical.setStatus(
        "current"
    )

cmmPsu12vPgRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 66)
)
cmmPsu12vPgRecover.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsu12vPgRecover.setStatus(
        "current"
    )

cmmSysPSUInputVoltageHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 67)
)
cmmSysPSUInputVoltageHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageHighAlert.setStatus(
        "current"
    )

cmmSysPSUInputVoltageLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 68)
)
cmmSysPSUInputVoltageLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageLowAlert.setStatus(
        "current"
    )

cmmSysPSUInputVoltageHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 69)
)
cmmSysPSUInputVoltageHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageHighCritical.setStatus(
        "current"
    )

cmmSysPSUInputVoltageLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 70)
)
cmmSysPSUInputVoltageLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageLowCritical.setStatus(
        "current"
    )

cmmSysPSUInputVoltageHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 71)
)
cmmSysPSUInputVoltageHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageHighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUInputVoltageLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 72)
)
cmmSysPSUInputVoltageLowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageLowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUInputVoltageHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 73)
)
cmmSysPSUInputVoltageHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageHighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUInputVoltageLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 74)
)
cmmSysPSUInputVoltageLowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputVoltageLowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 75)
)
cmmSysPSUOutputVoltageHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageHighAlert.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 76)
)
cmmSysPSUOutputVoltageLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageLowAlert.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 77)
)
cmmSysPSUOutputVoltageHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageHighCritical.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 78)
)
cmmSysPSUOutputVoltageLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageLowCritical.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 79)
)
cmmSysPSUOutputVoltageHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageHighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 80)
)
cmmSysPSUOutputVoltageLowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageLowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 81)
)
cmmSysPSUOutputVoltageHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageHighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputVoltageLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 82)
)
cmmSysPSUOutputVoltageLowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputVoltageCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputVoltageLowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUInputPowerHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 83)
)
cmmSysPSUInputPowerHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerHighAlert.setStatus(
        "current"
    )

cmmSysPSUInputPowerLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 84)
)
cmmSysPSUInputPowerLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerLowAlert.setStatus(
        "current"
    )

cmmSysPSUInputPowerHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 85)
)
cmmSysPSUInputPowerHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerHighCritical.setStatus(
        "current"
    )

cmmSysPSUInputPowerLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 86)
)
cmmSysPSUInputPowerLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerLowCritical.setStatus(
        "current"
    )

cmmSysPSUInputPowerHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 87)
)
cmmSysPSUInputPowerHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerHighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUInputPowerLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 88)
)
cmmSysPSUInputPowerLowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerLowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUInputPowerHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 89)
)
cmmSysPSUInputPowerHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerHighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUInputPowerLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 90)
)
cmmSysPSUInputPowerLowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputPowerLowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputPowerHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 91)
)
cmmSysPSUOutputPowerHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerHighAlert.setStatus(
        "current"
    )

cmmSysPSUOutputPowerLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 92)
)
cmmSysPSUOutputPowerLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerLowAlert.setStatus(
        "current"
    )

cmmSysPSUOutputPowerHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 93)
)
cmmSysPSUOutputPowerHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerHighCritical.setStatus(
        "current"
    )

cmmSysPSUOutputPowerLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 94)
)
cmmSysPSUOutputPowerLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerLowCritical.setStatus(
        "current"
    )

cmmSysPSUOutputPowerHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 95)
)
cmmSysPSUOutputPowerHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerHighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputPowerLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 96)
)
cmmSysPSUOutputPowerLowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerLowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputPowerHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 97)
)
cmmSysPSUOutputPowerHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerHighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputPowerLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 98)
)
cmmSysPSUOutputPowerLowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumption"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSConsumptionCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputPowerLowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUInputCurrentHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 99)
)
cmmSysPSUInputCurrentHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentHighAlert.setStatus(
        "current"
    )

cmmSysPSUInputCurrentLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 100)
)
cmmSysPSUInputCurrentLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentLowAlert.setStatus(
        "current"
    )

cmmSysPSUInputCurrentHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 101)
)
cmmSysPSUInputCurrentHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentHighCritical.setStatus(
        "current"
    )

cmmSysPSUInputCurrentLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 102)
)
cmmSysPSUInputCurrentLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentLowCritical.setStatus(
        "current"
    )

cmmSysPSUInputCurrentHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 103)
)
cmmSysPSUInputCurrentHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentHighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUInputCurrentLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 104)
)
cmmSysPSUInputCurrentLowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentLowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUInputCurrentHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 105)
)
cmmSysPSUInputCurrentHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentHighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUInputCurrentLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 106)
)
cmmSysPSUInputCurrentLowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysInputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUInputCurrentLowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 107)
)
cmmSysPSUOutputCurrentHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentHighAlert.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 108)
)
cmmSysPSUOutputCurrentLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentLowAlert.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 109)
)
cmmSysPSUOutputCurrentHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentHighCritical.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 110)
)
cmmSysPSUOutputCurrentLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentLowCritical.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 111)
)
cmmSysPSUOutputCurrentHighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentHighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 112)
)
cmmSysPSUOutputCurrentLowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentLowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 113)
)
cmmSysPSUOutputCurrentHighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentHighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUOutputCurrentLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 114)
)
cmmSysPSUOutputCurrentLowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysOutputCurrentCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUOutputCurrentLowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature1HighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 115)
)
cmmSysPSUTemperature1HighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1HighAlert.setStatus(
        "current"
    )

cmmSysPSUTemperature1LowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 116)
)
cmmSysPSUTemperature1LowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1LowAlert.setStatus(
        "current"
    )

cmmSysPSUTemperature1HighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 117)
)
cmmSysPSUTemperature1HighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1HighCritical.setStatus(
        "current"
    )

cmmSysPSUTemperature1LowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 118)
)
cmmSysPSUTemperature1LowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1LowCritical.setStatus(
        "current"
    )

cmmSysPSUTemperature1HighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 119)
)
cmmSysPSUTemperature1HighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1HighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature1LowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 120)
)
cmmSysPSUTemperature1LowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1LowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature1HighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 121)
)
cmmSysPSUTemperature1HighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1HighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature1LowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 122)
)
cmmSysPSUTemperature1LowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature1CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature1LowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature2HighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 123)
)
cmmSysPSUTemperature2HighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2HighAlert.setStatus(
        "current"
    )

cmmSysPSUTemperature2LowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 124)
)
cmmSysPSUTemperature2LowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2LowAlert.setStatus(
        "current"
    )

cmmSysPSUTemperature2HighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 125)
)
cmmSysPSUTemperature2HighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2HighCritical.setStatus(
        "current"
    )

cmmSysPSUTemperature2LowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 126)
)
cmmSysPSUTemperature2LowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2LowCritical.setStatus(
        "current"
    )

cmmSysPSUTemperature2HighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 127)
)
cmmSysPSUTemperature2HighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2HighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature2LowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 128)
)
cmmSysPSUTemperature2LowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2LowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature2HighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 129)
)
cmmSysPSUTemperature2HighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2HighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature2LowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 130)
)
cmmSysPSUTemperature2LowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature2CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature2LowCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature3HighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 131)
)
cmmSysPSUTemperature3HighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3HighAlert.setStatus(
        "current"
    )

cmmSysPSUTemperature3LowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 132)
)
cmmSysPSUTemperature3LowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3LowAlert.setStatus(
        "current"
    )

cmmSysPSUTemperature3HighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 133)
)
cmmSysPSUTemperature3HighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3HighCritical.setStatus(
        "current"
    )

cmmSysPSUTemperature3LowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 134)
)
cmmSysPSUTemperature3LowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3LowCritical.setStatus(
        "current"
    )

cmmSysPSUTemperature3HighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 135)
)
cmmSysPSUTemperature3HighAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3HighAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature3LowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 136)
)
cmmSysPSUTemperature3LowAlertRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3LowAlertRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature3HighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 137)
)
cmmSysPSUTemperature3HighCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3HighCriticalRecovery.setStatus(
        "current"
    )

cmmSysPSUTemperature3LowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 138)
)
cmmSysPSUTemperature3LowCriticalRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmSysPSTemperature3CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmSysPSUTemperature3LowCriticalRecovery.setStatus(
        "current"
    )

cmmFanTrayInsertedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 141)
)
cmmFanTrayInsertedNotify.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmFanTrayInsertedNotify.setStatus(
        "current"
    )

cmmFanTrayRemovedCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 142)
)
cmmFanTrayRemovedCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmFanTrayRemovedCritical.setStatus(
        "current"
    )

cmmFanTrayFaultyCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 143)
)
cmmFanTrayFaultyCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayFaultyCritical.setStatus(
        "current"
    )

cmmFanTrayRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 144)
)
cmmFanTrayRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayRecovered.setStatus(
        "current"
    )

cmmFanTrayStallCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 145)
)
cmmFanTrayStallCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayStallCritical.setStatus(
        "current"
    )

cmmFanTrayStallRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 146)
)
cmmFanTrayStallRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayStallRecovered.setStatus(
        "current"
    )

cmmFanRPMMinNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 147)
)
cmmFanRPMMinNotify.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanRpmMin"))
)
if mibBuilder.loadTexts:
    cmmFanRPMMinNotify.setStatus(
        "obsolete"
    )

cmmFanRPMMaxCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 148)
)
cmmFanRPMMaxCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanRpmMax"))
)
if mibBuilder.loadTexts:
    cmmFanRPMMaxCritical.setStatus(
        "current"
    )

cmmFanRPMDecreasedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 149)
)
cmmFanRPMDecreasedNotify.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanRpm"))
)
if mibBuilder.loadTexts:
    cmmFanRPMDecreasedNotify.setStatus(
        "current"
    )

cmmFanRPMIncreasedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 150)
)
cmmFanRPMIncreasedNotify.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmFanRpm"))
)
if mibBuilder.loadTexts:
    cmmFanRPMIncreasedNotify.setStatus(
        "current"
    )

cmmTransAlertTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 1)
)
cmmTransAlertTempHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTempHigh.setStatus(
        "current"
    )

cmmTransAlertTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 2)
)
cmmTransAlertTempLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTempLow.setStatus(
        "current"
    )

cmmTransCriticalTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 3)
)
cmmTransCriticalTempHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTempHigh.setStatus(
        "current"
    )

cmmTransCriticalTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 4)
)
cmmTransCriticalTempLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTempLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverTempRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 5)
)
cmmTransNotifyTransceiverTempRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTemperature"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverTempRecovered.setStatus(
        "current"
    )

cmmTransAlertVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 11)
)
cmmTransAlertVoltageHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertVoltageHigh.setStatus(
        "current"
    )

cmmTransAlertVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 12)
)
cmmTransAlertVoltageLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertVoltageLow.setStatus(
        "current"
    )

cmmTransCriticalVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 13)
)
cmmTransCriticalVoltageHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalVoltageHigh.setStatus(
        "current"
    )

cmmTransCriticalVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 14)
)
cmmTransCriticalVoltageLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalVoltageLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverVoltRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 15)
)
cmmTransNotifyTransceiverVoltRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVoltage"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverVoltRecovered.setStatus(
        "current"
    )

cmmTransAlertBiasHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 21)
)
cmmTransAlertBiasHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertBiasHigh.setStatus(
        "current"
    )

cmmTransAlertBiasLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 22)
)
cmmTransAlertBiasLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertBiasLow.setStatus(
        "current"
    )

cmmTransCriticalBiashigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 23)
)
cmmTransCriticalBiashigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalBiashigh.setStatus(
        "current"
    )

cmmTransCriticalBiasLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 24)
)
cmmTransCriticalBiasLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalBiasLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverBiasRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 25)
)
cmmTransNotifyTransceiverBiasRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverBiasRecovered.setStatus(
        "current"
    )

cmmTransAlertRxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 31)
)
cmmTransAlertRxPowerHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertRxPowerHigh.setStatus(
        "current"
    )

cmmTransAlertRxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 32)
)
cmmTransAlertRxPowerLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertRxPowerLow.setStatus(
        "current"
    )

cmmTransCriticalRxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 33)
)
cmmTransCriticalRxPowerHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalRxPowerHigh.setStatus(
        "current"
    )

cmmTransCriticalRxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 34)
)
cmmTransCriticalRxPowerLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalRxPowerLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverRxPowRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 35)
)
cmmTransNotifyTransceiverRxPowRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransRxPower"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverRxPowRecovered.setStatus(
        "current"
    )

cmmTransAlertTxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 41)
)
cmmTransAlertTxPowerHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTxPowerHigh.setStatus(
        "current"
    )

cmmTransAlertTxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 42)
)
cmmTransAlertTxPowerLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTxPowerLow.setStatus(
        "current"
    )

cmmTransCriticalTxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 43)
)
cmmTransCriticalTxPowerHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTxPowerHigh.setStatus(
        "current"
    )

cmmTransCriticalTxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 44)
)
cmmTransCriticalTxPowerLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTxPowerLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverTxPowRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 45)
)
cmmTransNotifyTransceiverTxPowRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTxPower"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverTxPowRecovered.setStatus(
        "current"
    )

cmmTransNotifyTransceiverInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 51)
)
cmmTransNotifyTransceiverInserted.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVendorName"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVendorSerialNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransconnectortype"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverInserted.setStatus(
        "current"
    )

cmmTransCriticalTransceiverRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 52)
)
cmmTransCriticalTransceiverRemoved.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVendorName"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransVendorSerialNumber"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransconnectortype"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTransceiverRemoved.setStatus(
        "current"
    )

cmmTransCriticalFaultyTransceiverInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 53)
)
cmmTransCriticalFaultyTransceiverInserted.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalFaultyTransceiverInserted.setStatus(
        "current"
    )

cmmCriticalIncompatibleTransceiverPresence = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 54)
)
cmmCriticalIncompatibleTransceiverPresence.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"))
)
if mibBuilder.loadTexts:
    cmmCriticalIncompatibleTransceiverPresence.setStatus(
        "current"
    )

cmmNotifyIncompatibleTransceiverRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 55)
)
cmmNotifyIncompatibleTransceiverRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"))
)
if mibBuilder.loadTexts:
    cmmNotifyIncompatibleTransceiverRecovery.setStatus(
        "current"
    )

cmmTransXFPAlertVoltage2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 61)
)
cmmTransXFPAlertVoltage2High.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVoltage2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransXFPAlertVoltage2High.setStatus(
        "current"
    )

cmmTransXFPAlertVoltage2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 62)
)
cmmTransXFPAlertVoltage2Low.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVoltage2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2AlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2AlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransXFPAlertVoltage2Low.setStatus(
        "current"
    )

cmmTransXFPCriticalVoltage2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 63)
)
cmmTransXFPCriticalVoltage2High.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVoltage2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransXFPCriticalVoltage2High.setStatus(
        "current"
    )

cmmTransXFPCriticalVoltage2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 64)
)
cmmTransXFPCriticalVoltage2Low.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVoltage2"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2CriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVolt2CriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransXFPCriticalVoltage2Low.setStatus(
        "current"
    )

cmmTransNotifyTransceiverXFPVolt2Recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 65)
)
cmmTransNotifyTransceiverXFPVolt2Recovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransXFPVoltage2"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverXFPVolt2Recovered.setStatus(
        "current"
    )

cmmTransFrequencyErrorHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 66)
)
cmmTransFrequencyErrorHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorHighAlert.setStatus(
        "current"
    )

cmmTransFrequencyErrorLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 67)
)
cmmTransFrequencyErrorLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorLowAlert.setStatus(
        "current"
    )

cmmTransFrequencyErrorHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 68)
)
cmmTransFrequencyErrorHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorHighCritical.setStatus(
        "current"
    )

cmmTransFrequencyErrorLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 69)
)
cmmTransFrequencyErrorLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyErrorCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorLowCritical.setStatus(
        "current"
    )

cmmTransFrequencyErrorRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 70)
)
cmmTransFrequencyErrorRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransFrequencyError"))
)
if mibBuilder.loadTexts:
    cmmTransFrequencyErrorRecovery.setStatus(
        "current"
    )

cmmTransWavelengthErrorHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 71)
)
cmmTransWavelengthErrorHighAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorHighAlert.setStatus(
        "current"
    )

cmmTransWavelengthErrorLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 72)
)
cmmTransWavelengthErrorLowAlert.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorAlertThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorLowAlert.setStatus(
        "current"
    )

cmmTransWavelengthErrorHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 73)
)
cmmTransWavelengthErrorHighCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorHighCritical.setStatus(
        "current"
    )

cmmTransWavelengthErrorLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 74)
)
cmmTransWavelengthErrorLowCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthError"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorCriticalThresholdMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthErrorCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorLowCritical.setStatus(
        "current"
    )

cmmTransWavelengthErrorRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 75)
)
cmmTransWavelengthErrorRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransWavelengthError"))
)
if mibBuilder.loadTexts:
    cmmTransWavelengthErrorRecovery.setStatus(
        "current"
    )

cmmTransTECFaultCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 76)
)
cmmTransTECFaultCritical.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"))
)
if mibBuilder.loadTexts:
    cmmTransTECFaultCritical.setStatus(
        "current"
    )

cmmTransTECFaultRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 77)
)
cmmTransTECFaultRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"))
)
if mibBuilder.loadTexts:
    cmmTransTECFaultRecovery.setStatus(
        "current"
    )

cmmTransAlertPreFecBerErrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 81)
)
cmmTransAlertPreFecBerErrHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertPreFecBerErrHigh.setStatus(
        "current"
    )

cmmTransAlertPreFecBerErrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 82)
)
cmmTransAlertPreFecBerErrLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertPreFecBerErrLow.setStatus(
        "current"
    )

cmmTransCriticalPreFecBerErrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 83)
)
cmmTransCriticalPreFecBerErrHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalPreFecBerErrHigh.setStatus(
        "current"
    )

cmmTransCriticalPreFecBerErrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 84)
)
cmmTransCriticalPreFecBerErrLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalPreFecBerErrLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverPreFecBerRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 85)
)
cmmTransNotifyTransceiverPreFecBerRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransPreFecBerVal"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverPreFecBerRecovered.setStatus(
        "current"
    )

cmmTransAlertUncorrectedBerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 91)
)
cmmTransAlertUncorrectedBerHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertUncorrectedBerHigh.setStatus(
        "current"
    )

cmmTransAlertUncorrectedBerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 92)
)
cmmTransAlertUncorrectedBerLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertUncorrectedBerLow.setStatus(
        "current"
    )

cmmTransCriticalUncorrectedBerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 93)
)
cmmTransCriticalUncorrectedBerHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalUncorrectedBerHigh.setStatus(
        "current"
    )

cmmTransCriticalUncorrectedBerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 94)
)
cmmTransCriticalUncorrectedBerLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerValCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalUncorrectedBerLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverUncorrectedBerRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 95)
)
cmmTransNotifyTransceiverUncorrectedBerRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransUncorrectedBerVal"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverUncorrectedBerRecovered.setStatus(
        "current"
    )

cmmTransAlertSnrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 101)
)
cmmTransAlertSnrHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertSnrHigh.setStatus(
        "current"
    )

cmmTransAlertSnrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 102)
)
cmmTransAlertSnrLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertSnrLow.setStatus(
        "current"
    )

cmmTransCriticalSnrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 103)
)
cmmTransCriticalSnrHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalSnrHigh.setStatus(
        "current"
    )

cmmTransCriticalSnrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 104)
)
cmmTransCriticalSnrLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalSnrLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverSnrRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 105)
)
cmmTransNotifyTransceiverSnrRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransSnrVal"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverSnrRecovered.setStatus(
        "current"
    )

cmmTransAlertresIsiHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 111)
)
cmmTransAlertresIsiHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertresIsiHigh.setStatus(
        "current"
    )

cmmTransAlertresIsiLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 112)
)
cmmTransAlertresIsiLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertresIsiLow.setStatus(
        "current"
    )

cmmTransCriticalResIsiHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 113)
)
cmmTransCriticalResIsiHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalResIsiHigh.setStatus(
        "current"
    )

cmmTransCriticalResIsiLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 114)
)
cmmTransCriticalResIsiLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalResIsiLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverResIsiRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 115)
)
cmmTransNotifyTransceiverResIsiRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransResIsiVal"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverResIsiRecovered.setStatus(
        "current"
    )

cmmTransAlertLvlTranHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 121)
)
cmmTransAlertLvlTranHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertLvlTranHigh.setStatus(
        "current"
    )

cmmTransAlertLvlTranLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 122)
)
cmmTransAlertLvlTranLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertLvlTranLow.setStatus(
        "current"
    )

cmmTransCriticalLvlTranHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 123)
)
cmmTransCriticalLvlTranHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalLvlTranHigh.setStatus(
        "current"
    )

cmmTransCriticalLvlTranLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 124)
)
cmmTransCriticalLvlTranLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalLvlTranLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverLvlTranRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 125)
)
cmmTransNotifyTransceiverLvlTranRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLvlTransVal"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverLvlTranRecovered.setStatus(
        "current"
    )

cmmTransAlertTecCurrErrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 131)
)
cmmTransAlertTecCurrErrHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTecCurrErrHigh.setStatus(
        "current"
    )

cmmTransAlertTecCurrErrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 132)
)
cmmTransAlertTecCurrErrLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTecCurrErrLow.setStatus(
        "current"
    )

cmmTransCriticalTecCurrErrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 133)
)
cmmTransCriticalTecCurrErrHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTecCurrErrHigh.setStatus(
        "current"
    )

cmmTransCriticalTecCurrErrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 134)
)
cmmTransCriticalTecCurrErrLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTecCurrErrLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverTecCurrErrRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 135)
)
cmmTransNotifyTransceiverTecCurrErrRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransTecCurrErrVal"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverTecCurrErrRecovered.setStatus(
        "current"
    )

cmmTransAlertLaserTempValHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 141)
)
cmmTransAlertLaserTempValHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertLaserTempValHigh.setStatus(
        "current"
    )

cmmTransAlertLaserTempValLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 142)
)
cmmTransAlertLaserTempValLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertLaserTempValLow.setStatus(
        "current"
    )

cmmTransCriticalLaserTempValHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 143)
)
cmmTransCriticalLaserTempValHigh.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalLaserTempValHigh.setStatus(
        "current"
    )

cmmTransCriticalLaserTempValLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 144)
)
cmmTransCriticalLaserTempValLow.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempVal"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticalMin"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempCriticalMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalLaserTempValLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverLaserTempRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 145)
)
cmmTransNotifyTransceiverLaserTempRecovered.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransLaserTempVal"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverLaserTempRecovered.setStatus(
        "current"
    )

cmmTranAlertTransceiverPortRxLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 146)
)
cmmTranAlertTransceiverPortRxLoss.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"))
)
if mibBuilder.loadTexts:
    cmmTranAlertTransceiverPortRxLoss.setStatus(
        "current"
    )

cmmTransNotifyTransceiverPortRxLossRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 147)
)
cmmTransNotifyTransceiverPortRxLossRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransType"),
        ("IPI-CMM-CHASSIS-MIB", "cmmTransChannelIndex"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverPortRxLossRecovery.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPI-CMM-CHASSIS-MIB",
    **{"LedColorCode": LedColorCode,
       "SystemStatusCode": SystemStatusCode,
       "ErrorFigures": ErrorFigures,
       "cmm": cmm,
       "cmmChassisObject": cmmChassisObject,
       "cmmObjects": cmmObjects,
       "cmmNumStackUnits": cmmNumStackUnits,
       "cmmSysObjects": cmmSysObjects,
       "cmmStackUnitTable": cmmStackUnitTable,
       "cmmStackUnitEntry": cmmStackUnitEntry,
       "cmmStackUnitIndex": cmmStackUnitIndex,
       "cmmStackUnitModelName": cmmStackUnitModelName,
       "cmmStackUnitSerialNumber": cmmStackUnitSerialNumber,
       "cmmStackUnitUpTime": cmmStackUnitUpTime,
       "cmmStackUnitMfgDate": cmmStackUnitMfgDate,
       "cmmStackUnitMacAddress": cmmStackUnitMacAddress,
       "cmmStackUnitPartNum": cmmStackUnitPartNum,
       "cmmStackLabelRevision": cmmStackLabelRevision,
       "cmmStackUnitCountryCode": cmmStackUnitCountryCode,
       "cmmStackUnitServiceTag": cmmStackUnitServiceTag,
       "cmmStackPlatformName": cmmStackPlatformName,
       "cmmStackOnieVersion": cmmStackOnieVersion,
       "cmmStackMfgName": cmmStackMfgName,
       "cmmStackVendorName": cmmStackVendorName,
       "cmmStackDiagVersion": cmmStackDiagVersion,
       "cmmStackCrc32": cmmStackCrc32,
       "cmmStackUnitNumFanControllers": cmmStackUnitNumFanControllers,
       "cmmStackUnitNumFanTrays": cmmStackUnitNumFanTrays,
       "cmmStackUnitNumPowerSupplies": cmmStackUnitNumPowerSupplies,
       "cmmStackUnitNumPluggableModules": cmmStackUnitNumPluggableModules,
       "cmmStackUnitNumFastEtherPorts": cmmStackUnitNumFastEtherPorts,
       "cmmStackUnitNumGigEtherPorts": cmmStackUnitNumGigEtherPorts,
       "cmmStackUnitNum10GigEtherPorts": cmmStackUnitNum10GigEtherPorts,
       "cmmStackUnitNum25GigEtherPorts": cmmStackUnitNum25GigEtherPorts,
       "cmmStackUnitNum40GigEtherPorts": cmmStackUnitNum40GigEtherPorts,
       "cmmStackUnitNum50GigEtherPorts": cmmStackUnitNum50GigEtherPorts,
       "cmmStackUnitNum100GigEtherPorts": cmmStackUnitNum100GigEtherPorts,
       "cmmStackUnitSwitchChipRev": cmmStackUnitSwitchChipRev,
       "cmmStackSupportedLabelRevision": cmmStackSupportedLabelRevision,
       "cmmStackUnitSupportedSwitchChipRev": cmmStackUnitSupportedSwitchChipRev,
       "cmmTransEEPROMTable": cmmTransEEPROMTable,
       "cmmTransEEPROMEntry": cmmTransEEPROMEntry,
       "cmmTransIndex": cmmTransIndex,
       "cmmTransType": cmmTransType,
       "cmmTransNoOfChannels": cmmTransNoOfChannels,
       "cmmTransidentifier": cmmTransidentifier,
       "cmmTransSFPextendedidentifier": cmmTransSFPextendedidentifier,
       "cmmTransQSFPextendedidentifier": cmmTransQSFPextendedidentifier,
       "cmmTransconnectortype": cmmTransconnectortype,
       "cmmTransEthCompliance": cmmTransEthCompliance,
       "cmmTransExtEthCompliance": cmmTransExtEthCompliance,
       "cmmTransSonetCompliance": cmmTransSonetCompliance,
       "cmmTransFiberChnlLinkLen": cmmTransFiberChnlLinkLen,
       "cmmTransFiberChnlTransTech": cmmTransFiberChnlTransTech,
       "cmmTransFiberChnlTransMedia": cmmTransFiberChnlTransMedia,
       "cmmTransSFPFiberChnlSpeed": cmmTransSFPFiberChnlSpeed,
       "cmmTransQSFPFiberChnlSpeed": cmmTransQSFPFiberChnlSpeed,
       "cmmTransSFPInfiniBandCompliance": cmmTransSFPInfiniBandCompliance,
       "cmmTransSFPEsconCompliance": cmmTransSFPEsconCompliance,
       "cmmTransSfpPlusCableTech": cmmTransSfpPlusCableTech,
       "cmmTransEncoding": cmmTransEncoding,
       "cmmTransLengthKmtrs": cmmTransLengthKmtrs,
       "cmmTransLengthMtrs": cmmTransLengthMtrs,
       "cmmTransLengthOM1": cmmTransLengthOM1,
       "cmmTransLengthOM2": cmmTransLengthOM2,
       "cmmTransLengthOM3": cmmTransLengthOM3,
       "cmmTransLengthOM4": cmmTransLengthOM4,
       "cmmTransVendorName": cmmTransVendorName,
       "cmmTransVendorOUI": cmmTransVendorOUI,
       "cmmTransVendorPartNumber": cmmTransVendorPartNumber,
       "cmmTransVendorRevision": cmmTransVendorRevision,
       "cmmTransCheckCode": cmmTransCheckCode,
       "cmmTransCheckCodeExtended": cmmTransCheckCodeExtended,
       "cmmTransNominalBitRate": cmmTransNominalBitRate,
       "cmmTransBitRateMax": cmmTransBitRateMax,
       "cmmTransBitRateMin": cmmTransBitRateMin,
       "cmmTransVendorSerialNumber": cmmTransVendorSerialNumber,
       "cmmTransDateCode": cmmTransDateCode,
       "cmmTransDDMSupport": cmmTransDDMSupport,
       "cmmTransMaxCaseTemp": cmmTransMaxCaseTemp,
       "cmmTransSFPOptionsImp": cmmTransSFPOptionsImp,
       "cmmTransQSFPOptionsImp": cmmTransQSFPOptionsImp,
       "cmmTransPresence": cmmTransPresence,
       "cmmTransFrontPanelPortNumber": cmmTransFrontPanelPortNumber,
       "cmmTransXFPextendedidentifier": cmmTransXFPextendedidentifier,
       "cmmTransXFP10GEthCompliance": cmmTransXFP10GEthCompliance,
       "cmmTransXFP10GFiberChnCompliance": cmmTransXFP10GFiberChnCompliance,
       "cmmTransXFP10GCopperLinksRsvd": cmmTransXFP10GCopperLinksRsvd,
       "cmmTransXFPLowerSpeedLinks": cmmTransXFPLowerSpeedLinks,
       "cmmTransXFPSonetInterconnect": cmmTransXFPSonetInterconnect,
       "cmmTransXFPSonetShortHaul": cmmTransXFPSonetShortHaul,
       "cmmTransXFPSonetLongHaul": cmmTransXFPSonetLongHaul,
       "cmmTransXFPSonetVeryLongHaul": cmmTransXFPSonetVeryLongHaul,
       "cmmTransXFPOptionsImp": cmmTransXFPOptionsImp,
       "cmmTransXFPVoltageAuxMonitor": cmmTransXFPVoltageAuxMonitor,
       "cmmTransXFPEncoding": cmmTransXFPEncoding,
       "cmmTransWavelength": cmmTransWavelength,
       "cmmTransChannelNumber": cmmTransChannelNumber,
       "cmmTransGridSpacing": cmmTransGridSpacing,
       "cmmTransLaserFirstFrequency": cmmTransLaserFirstFrequency,
       "cmmTransLaserLastFrequency": cmmTransLaserLastFrequency,
       "cmmTransDDMTable": cmmTransDDMTable,
       "cmmTransDDMEntry": cmmTransDDMEntry,
       "cmmTransChannelIndex": cmmTransChannelIndex,
       "cmmTransTemperature": cmmTransTemperature,
       "cmmTransTempAlertThresholdMin": cmmTransTempAlertThresholdMin,
       "cmmTransTempAlertThresholdMax": cmmTransTempAlertThresholdMax,
       "cmmTransTempCriticalThresholdMin": cmmTransTempCriticalThresholdMin,
       "cmmTransTempCriticalThresholdMax": cmmTransTempCriticalThresholdMax,
       "cmmTransVoltage": cmmTransVoltage,
       "cmmTransVoltAlertThresholdMin": cmmTransVoltAlertThresholdMin,
       "cmmTransVoltAlertThresholdMax": cmmTransVoltAlertThresholdMax,
       "cmmTransVoltCriticalThresholdMin": cmmTransVoltCriticalThresholdMin,
       "cmmTransVoltCriticalThresholdMax": cmmTransVoltCriticalThresholdMax,
       "cmmTransLaserBiasCurrent": cmmTransLaserBiasCurrent,
       "cmmTransLaserBiasCurrAlertThresholdMin": cmmTransLaserBiasCurrAlertThresholdMin,
       "cmmTransLaserBiasCurrAlertThresholdMax": cmmTransLaserBiasCurrAlertThresholdMax,
       "cmmTransLaserBiasCurrCriticalThresholdMin": cmmTransLaserBiasCurrCriticalThresholdMin,
       "cmmTransLaserBiasCurrCriticalThresholdMax": cmmTransLaserBiasCurrCriticalThresholdMax,
       "cmmTransTxPower": cmmTransTxPower,
       "cmmTransTxPowerAlertThresholdMin": cmmTransTxPowerAlertThresholdMin,
       "cmmTransTxPowerAlertThresholdMax": cmmTransTxPowerAlertThresholdMax,
       "cmmTransTxPowerCriticalThresholdMin": cmmTransTxPowerCriticalThresholdMin,
       "cmmTransTxPowerCriticalThresholdMax": cmmTransTxPowerCriticalThresholdMax,
       "cmmTransRxPower": cmmTransRxPower,
       "cmmTransRxPowerAlertThresholdMin": cmmTransRxPowerAlertThresholdMin,
       "cmmTransRxPowerAlertThresholdMax": cmmTransRxPowerAlertThresholdMax,
       "cmmTransRxPowerCriticalThresholdMin": cmmTransRxPowerCriticalThresholdMin,
       "cmmTransRxPowerCriticalThresholdMax": cmmTransRxPowerCriticalThresholdMax,
       "cmmTransTxPowerSupported": cmmTransTxPowerSupported,
       "cmmTransRxPowerSupported": cmmTransRxPowerSupported,
       "cmmTransDDMStatus": cmmTransDDMStatus,
       "cmmTransTxState": cmmTransTxState,
       "cmmTransRxLosState": cmmTransRxLosState,
       "cmmTransTxLosState": cmmTransTxLosState,
       "cmmTransResetState": cmmTransResetState,
       "cmmTransPowerMode": cmmTransPowerMode,
       "cmmTransXFPVoltage2": cmmTransXFPVoltage2,
       "cmmTransXFPVolt2AlertThresholdMin": cmmTransXFPVolt2AlertThresholdMin,
       "cmmTransXFPVolt2AlertThresholdMax": cmmTransXFPVolt2AlertThresholdMax,
       "cmmTransXFPVolt2CriticalThresholdMin": cmmTransXFPVolt2CriticalThresholdMin,
       "cmmTransXFPVolt2CriticalThresholdMax": cmmTransXFPVolt2CriticalThresholdMax,
       "cmmTransFrequencyError": cmmTransFrequencyError,
       "cmmTransFrequencyErrorAlertThresholdMin": cmmTransFrequencyErrorAlertThresholdMin,
       "cmmTransFrequencyErrorAlertThresholdMax": cmmTransFrequencyErrorAlertThresholdMax,
       "cmmTransFrequencyErrorCriticalThresholdMin": cmmTransFrequencyErrorCriticalThresholdMin,
       "cmmTransFrequencyErrorCriticalThresholdMax": cmmTransFrequencyErrorCriticalThresholdMax,
       "cmmTransWavelengthError": cmmTransWavelengthError,
       "cmmTransWavelengthErrorAlertThresholdMin": cmmTransWavelengthErrorAlertThresholdMin,
       "cmmTransWavelengthErrorAlertThresholdMax": cmmTransWavelengthErrorAlertThresholdMax,
       "cmmTransWavelengthErrorCriticalThresholdMin": cmmTransWavelengthErrorCriticalThresholdMin,
       "cmmTransWavelengthErrorCriticalThresholdMax": cmmTransWavelengthErrorCriticalThresholdMax,
       "cmmTransCurrentStatus": cmmTransCurrentStatus,
       "cmmSysRamTable": cmmSysRamTable,
       "cmmSysRamEntry": cmmSysRamEntry,
       "cmmSysRamTotalMem": cmmSysRamTotalMem,
       "cmmSysRamUsedMem": cmmSysRamUsedMem,
       "cmmSysRamFreeMem": cmmSysRamFreeMem,
       "cmmSysRamAlertThreshold": cmmSysRamAlertThreshold,
       "cmmSysRamCriticalThreshold": cmmSysRamCriticalThreshold,
       "cmmStackCpuTable": cmmStackCpuTable,
       "cmmStackCpuEntry": cmmStackCpuEntry,
       "cmmStackUnitNumCpuProcessor": cmmStackUnitNumCpuProcessor,
       "cmmStackUnitCpuLoad1Min": cmmStackUnitCpuLoad1Min,
       "cmmStackUnitCpuLoad5Min": cmmStackUnitCpuLoad5Min,
       "cmmStackUnitCpuLoad15Min": cmmStackUnitCpuLoad15Min,
       "cmmStackCpuLoad1minCriticalThreshold": cmmStackCpuLoad1minCriticalThreshold,
       "cmmStackCpuLoad1minAlertThreshold": cmmStackCpuLoad1minAlertThreshold,
       "cmmStackCpuLoad5minAlertThreshold": cmmStackCpuLoad5minAlertThreshold,
       "cmmStackCpuLoad15minAlertThreshold": cmmStackCpuLoad15minAlertThreshold,
       "cmmStackUnitCpuUtilization": cmmStackUnitCpuUtilization,
       "cmmStackUnitCpuUtilCriticalThreshold": cmmStackUnitCpuUtilCriticalThreshold,
       "cmmStackUnitCpuUtilAlertThreshold": cmmStackUnitCpuUtilAlertThreshold,
       "cmmSysPowerSupplyTable": cmmSysPowerSupplyTable,
       "cmmSysPowerSupplyEntry": cmmSysPowerSupplyEntry,
       "cmmSysPSUIndex": cmmSysPSUIndex,
       "cmmSysPowerSupplyOperStatus": cmmSysPowerSupplyOperStatus,
       "cmmSysPowerSupplyType": cmmSysPowerSupplyType,
       "cmmSysHotSwapStat": cmmSysHotSwapStat,
       "cmmSysPSConsumption": cmmSysPSConsumption,
       "cmmSysInputPower": cmmSysInputPower,
       "cmmSysInputVoltage": cmmSysInputVoltage,
       "cmmSysOutputVoltage": cmmSysOutputVoltage,
       "cmmSysInputCurrent": cmmSysInputCurrent,
       "cmmSysOutputCurrent": cmmSysOutputCurrent,
       "cmmSysPSTemperature1": cmmSysPSTemperature1,
       "cmmSysPSTemperature2": cmmSysPSTemperature2,
       "cmmSysPSFan1Rpm": cmmSysPSFan1Rpm,
       "cmmSysPSFan2Rpm": cmmSysPSFan2Rpm,
       "cmmSysPS12VPg": cmmSysPS12VPg,
       "cmmSysPSAcCritical": cmmSysPSAcCritical,
       "cmmSysPSParamsSupport": cmmSysPSParamsSupport,
       "cmmSysPSCapacity": cmmSysPSCapacity,
       "cmmSysPSConsumptionAlertThresholdMin": cmmSysPSConsumptionAlertThresholdMin,
       "cmmSysPSConsumptionAlertThresholdMax": cmmSysPSConsumptionAlertThresholdMax,
       "cmmSysInputPowerAlertThresholdMin": cmmSysInputPowerAlertThresholdMin,
       "cmmSysInputPowerAlertThresholdMax": cmmSysInputPowerAlertThresholdMax,
       "cmmSysInputVoltageAlertThresholdMin": cmmSysInputVoltageAlertThresholdMin,
       "cmmSysInputVoltageAlertThresholdMax": cmmSysInputVoltageAlertThresholdMax,
       "cmmSysOutputVoltageAlertThresholdMin": cmmSysOutputVoltageAlertThresholdMin,
       "cmmSysOutputVoltageAlertThresholdMax": cmmSysOutputVoltageAlertThresholdMax,
       "cmmSysInputCurrentAlertThresholdMin": cmmSysInputCurrentAlertThresholdMin,
       "cmmSysInputCurrentAlertThresholdMax": cmmSysInputCurrentAlertThresholdMax,
       "cmmSysOutputCurrentAlertThresholdMin": cmmSysOutputCurrentAlertThresholdMin,
       "cmmSysOutputCurrentAlertThresholdMax": cmmSysOutputCurrentAlertThresholdMax,
       "cmmSysPSTemperature1AlertThresholdMin": cmmSysPSTemperature1AlertThresholdMin,
       "cmmSysPSTemperature1AlertThresholdMax": cmmSysPSTemperature1AlertThresholdMax,
       "cmmSysPSTemperature2AlertThresholdMin": cmmSysPSTemperature2AlertThresholdMin,
       "cmmSysPSTemperature2AlertThresholdMax": cmmSysPSTemperature2AlertThresholdMax,
       "cmmSysPSConsumptionCriticalThresholdMin": cmmSysPSConsumptionCriticalThresholdMin,
       "cmmSysPSConsumptionCriticalThresholdMax": cmmSysPSConsumptionCriticalThresholdMax,
       "cmmSysInputPowerCriticalThresholdMin": cmmSysInputPowerCriticalThresholdMin,
       "cmmSysInputPowerCriticalThresholdMax": cmmSysInputPowerCriticalThresholdMax,
       "cmmSysInputVoltageCriticalThresholdMin": cmmSysInputVoltageCriticalThresholdMin,
       "cmmSysInputVoltageCriticalThresholdMax": cmmSysInputVoltageCriticalThresholdMax,
       "cmmSysOutputVoltageCriticalThresholdMin": cmmSysOutputVoltageCriticalThresholdMin,
       "cmmSysOutputVoltageCriticalThresholdMax": cmmSysOutputVoltageCriticalThresholdMax,
       "cmmSysInputCurrentCriticalThresholdMin": cmmSysInputCurrentCriticalThresholdMin,
       "cmmSysInputCurrentCriticalThresholdMax": cmmSysInputCurrentCriticalThresholdMax,
       "cmmSysOutputCurrentCriticalThresholdMin": cmmSysOutputCurrentCriticalThresholdMin,
       "cmmSysOutputCurrentCriticalThresholdMax": cmmSysOutputCurrentCriticalThresholdMax,
       "cmmSysPSTemperature1CriticalThresholdMin": cmmSysPSTemperature1CriticalThresholdMin,
       "cmmSysPSTemperature1CriticalThresholdMax": cmmSysPSTemperature1CriticalThresholdMax,
       "cmmSysPSTemperature2CriticalThresholdMin": cmmSysPSTemperature2CriticalThresholdMin,
       "cmmSysPSTemperature2CriticalThresholdMax": cmmSysPSTemperature2CriticalThresholdMax,
       "cmmSysInputVoltageOverShutdown": cmmSysInputVoltageOverShutdown,
       "cmmSysInputVoltageUnderShutdown": cmmSysInputVoltageUnderShutdown,
       "cmmSysInputVoltageOverResume": cmmSysInputVoltageOverResume,
       "cmmSysInputVoltageUnderResume": cmmSysInputVoltageUnderResume,
       "cmmSysOutputVoltageOverShutdown": cmmSysOutputVoltageOverShutdown,
       "cmmSysOutputVoltageUnderShutdown": cmmSysOutputVoltageUnderShutdown,
       "cmmSysOutputVoltageOverResume": cmmSysOutputVoltageOverResume,
       "cmmSysOutputVoltageUnderResume": cmmSysOutputVoltageUnderResume,
       "cmmSysInputPowerOverShutdown": cmmSysInputPowerOverShutdown,
       "cmmSysInputPowerUnderShutdown": cmmSysInputPowerUnderShutdown,
       "cmmSysInputPowerOverResume": cmmSysInputPowerOverResume,
       "cmmSysInputPowerUnderResume": cmmSysInputPowerUnderResume,
       "cmmSysOutputPowerOverShutdown": cmmSysOutputPowerOverShutdown,
       "cmmSysOutputPowerUnderShutdown": cmmSysOutputPowerUnderShutdown,
       "cmmSysOutputPowerOverResume": cmmSysOutputPowerOverResume,
       "cmmSysOutputPowerUnderResume": cmmSysOutputPowerUnderResume,
       "cmmSysInputCurrentOverShutdown": cmmSysInputCurrentOverShutdown,
       "cmmSysInputCurrentUnderShutdown": cmmSysInputCurrentUnderShutdown,
       "cmmSysInputCurrentOverResume": cmmSysInputCurrentOverResume,
       "cmmSysInputCurrentUnderResume": cmmSysInputCurrentUnderResume,
       "cmmSysOutputCurrentOverShutdown": cmmSysOutputCurrentOverShutdown,
       "cmmSysOutputCurrentUnderShutdown": cmmSysOutputCurrentUnderShutdown,
       "cmmSysOutputCurrentOverResume": cmmSysOutputCurrentOverResume,
       "cmmSysOutputCurrentUnderResume": cmmSysOutputCurrentUnderResume,
       "cmmSysPsuTemperature1OverShutdown": cmmSysPsuTemperature1OverShutdown,
       "cmmSysPsuTemperature1UnderShutdown": cmmSysPsuTemperature1UnderShutdown,
       "cmmSysPsuTemperature1OverResume": cmmSysPsuTemperature1OverResume,
       "cmmSysPsuTemperature1UnderResume": cmmSysPsuTemperature1UnderResume,
       "cmmSysPsuTemperature2OverShutdown": cmmSysPsuTemperature2OverShutdown,
       "cmmSysPsuTemperature2UnderShutdown": cmmSysPsuTemperature2UnderShutdown,
       "cmmSysPsuTemperature2OverResume": cmmSysPsuTemperature2OverResume,
       "cmmSysPsuTemperature2UnderResume": cmmSysPsuTemperature2UnderResume,
       "cmmSysPSTemperature3": cmmSysPSTemperature3,
       "cmmSysPSTemperature3AlertThresholdMin": cmmSysPSTemperature3AlertThresholdMin,
       "cmmSysPSTemperature3AlertThresholdMax": cmmSysPSTemperature3AlertThresholdMax,
       "cmmSysPSTemperature3CriticalThresholdMin": cmmSysPSTemperature3CriticalThresholdMin,
       "cmmSysPSTemperature3CriticalThresholdMax": cmmSysPSTemperature3CriticalThresholdMax,
       "cmmSysPsuTemperature3OverShutdown": cmmSysPsuTemperature3OverShutdown,
       "cmmSysPsuTemperature3UnderShutdown": cmmSysPsuTemperature3UnderShutdown,
       "cmmSysPsuTemperature3OverResume": cmmSysPsuTemperature3OverResume,
       "cmmSysPsuTemperature3UnderResume": cmmSysPsuTemperature3UnderResume,
       "cmmSysPSFan3Rpm": cmmSysPSFan3Rpm,
       "cmmSysPSFan4Rpm": cmmSysPSFan4Rpm,
       "cmmSysPowerRailTable": cmmSysPowerRailTable,
       "cmmSysPowerRailEntry": cmmSysPowerRailEntry,
       "cmmSysPOWERVDDR": cmmSysPOWERVDDR,
       "cmmSysPOWERCORE": cmmSysPOWERCORE,
       "cmmSysV1P1POWERRAIL": cmmSysV1P1POWERRAIL,
       "cmmSysMAINBOARDPOWERRAIL": cmmSysMAINBOARDPOWERRAIL,
       "cmmSysV1P05POWERRAIL": cmmSysV1P05POWERRAIL,
       "cmmSysV1P5POWERRAIL": cmmSysV1P5POWERRAIL,
       "cmmSysVCCPOWERRAIL": cmmSysVCCPOWERRAIL,
       "cmmSysSBV1P5POWERRAIL": cmmSysSBV1P5POWERRAIL,
       "cmmSysV1P0POWERRAIL": cmmSysV1P0POWERRAIL,
       "cmmSysV3P3POWERRAIL": cmmSysV3P3POWERRAIL,
       "cmmSysV1P8POWERRAIL": cmmSysV1P8POWERRAIL,
       "cmmSysV1P35POWERRAIL": cmmSysV1P35POWERRAIL,
       "cmmSysVCC5V": cmmSysVCC5V,
       "cmmSysVCC33V": cmmSysVCC33V,
       "cmmSysVCCMAC1V": cmmSysVCCMAC1V,
       "cmmSysVCCMACAVS1V": cmmSysVCCMACAVS1V,
       "cmmSysVCCV1P05": cmmSysVCCV1P05,
       "cmmSysVCCV1P5": cmmSysVCCV1P5,
       "cmmSysVCCV1P8": cmmSysVCCV1P8,
       "cmmSysVCCAVS1V": cmmSysVCCAVS1V,
       "cmmSysDDRVTT": cmmSysDDRVTT,
       "cmmSysSBV1P9POWERRAIL": cmmSysSBV1P9POWERRAIL,
       "cmmSysVCCMACV1P25": cmmSysVCCMACV1P25,
       "cmmSysMACV1P8": cmmSysMACV1P8,
       "cmmSysPS1": cmmSysPS1,
       "cmmSysPS2": cmmSysPS2,
       "cmmSysPS1POWERRAIL": cmmSysPS1POWERRAIL,
       "cmmSysPS2POWERRAIL": cmmSysPS2POWERRAIL,
       "cmmSysPS1V12POWERRAIL": cmmSysPS1V12POWERRAIL,
       "cmmSysPS2V12POWERRAIL": cmmSysPS2V12POWERRAIL,
       "cmmSysPS1ACALERTPOWERRAIL": cmmSysPS1ACALERTPOWERRAIL,
       "cmmSysPS2ACALERTPOWERRAIL": cmmSysPS2ACALERTPOWERRAIL,
       "cmmSysPOWERVCCP": cmmSysPOWERVCCP,
       "cmmSysV5APOWERRAIL": cmmSysV5APOWERRAIL,
       "cmmSysV3P3APOWERRAIL": cmmSysV3P3APOWERRAIL,
       "cmmSysXP0RV75POWERRAIL": cmmSysXP0RV75POWERRAIL,
       "cmmSysXP1RV07CPPOWERRAIL": cmmSysXP1RV07CPPOWERRAIL,
       "cmmFanTrayTable": cmmFanTrayTable,
       "cmmFanTrayEntry": cmmFanTrayEntry,
       "cmmFanTrayNumber": cmmFanTrayNumber,
       "cmmFanTrayStatus": cmmFanTrayStatus,
       "cmmFanTrayLedColor": cmmFanTrayLedColor,
       "cmmFanTable": cmmFanTable,
       "cmmFanEntry": cmmFanEntry,
       "cmmFanIndex": cmmFanIndex,
       "cmmFanRpm": cmmFanRpm,
       "cmmFanRpmMin": cmmFanRpmMin,
       "cmmFanRpmMax": cmmFanRpmMax,
       "cmmFanStatus": cmmFanStatus,
       "cmmFanLocation": cmmFanLocation,
       "cmmSysTemperatureTable": cmmSysTemperatureTable,
       "cmmSysTemperatureEntry": cmmSysTemperatureEntry,
       "cmmSysTemperatureSensorIndex": cmmSysTemperatureSensorIndex,
       "cmmSysTemperatureSensorName": cmmSysTemperatureSensorName,
       "cmmSysTemperatureValue": cmmSysTemperatureValue,
       "cmmSysTempEmergencyThresholdMin": cmmSysTempEmergencyThresholdMin,
       "cmmSysTempEmergencyThresholdMax": cmmSysTempEmergencyThresholdMax,
       "cmmSysTempCriticalThresholdMin": cmmSysTempCriticalThresholdMin,
       "cmmSysTempCriticalThresholdMax": cmmSysTempCriticalThresholdMax,
       "cmmSysTempAlertThresholdMin": cmmSysTempAlertThresholdMin,
       "cmmSysTempAlertThresholdMax": cmmSysTempAlertThresholdMax,
       "cmmSysTempMinValue": cmmSysTempMinValue,
       "cmmSysTempMaxValue": cmmSysTempMaxValue,
       "cmmSysTempAverageValue": cmmSysTempAverageValue,
       "cmmSysComponentStatusTable": cmmSysComponentStatusTable,
       "cmmSysComponentStatusEntry": cmmSysComponentStatusEntry,
       "cmmSysPsu1Status": cmmSysPsu1Status,
       "cmmSysPsu1LedColor": cmmSysPsu1LedColor,
       "cmmSysPsu2Status": cmmSysPsu2Status,
       "cmmSysPsu2LedColor": cmmSysPsu2LedColor,
       "cmmSysLocatorLedStatus": cmmSysLocatorLedStatus,
       "cmmSysLocatorLedColor": cmmSysLocatorLedColor,
       "cmmSysMasterLedStatus": cmmSysMasterLedStatus,
       "cmmSysMasterLedColor": cmmSysMasterLedColor,
       "cmmSysFanStatus": cmmSysFanStatus,
       "cmmSysFrontFanLedColor": cmmSysFrontFanLedColor,
       "cmmSysRamStatus": cmmSysRamStatus,
       "cmmSysCpuStatus": cmmSysCpuStatus,
       "cmmSysDiskStatus": cmmSysDiskStatus,
       "cmmSysTemperatureStatus": cmmSysTemperatureStatus,
       "cmmSysSwModuleTable": cmmSysSwModuleTable,
       "cmmSysSwModuleEntry": cmmSysSwModuleEntry,
       "cmmSysSwRuntimeImgVersion": cmmSysSwRuntimeImgVersion,
       "cmmSysSwRuntimeImgDate": cmmSysSwRuntimeImgDate,
       "cmmSwitchTemperatureTable": cmmSwitchTemperatureTable,
       "cmmSwitchTemperatureEntry": cmmSwitchTemperatureEntry,
       "cmmSwitchTemperatureSensorIndex": cmmSwitchTemperatureSensorIndex,
       "cmmSwitchTemperatureValue": cmmSwitchTemperatureValue,
       "cmmSwitchTempPeakValue": cmmSwitchTempPeakValue,
       "cmmSysHardDiskTable": cmmSysHardDiskTable,
       "cmmSysHardDiskEntry": cmmSysHardDiskEntry,
       "cmmSysHarddiskSerialno": cmmSysHarddiskSerialno,
       "cmmSysHarddiskModelno": cmmSysHarddiskModelno,
       "cmmSysHarddiskFirmwarerev": cmmSysHarddiskFirmwarerev,
       "cmmSysHarddiskCylinders": cmmSysHarddiskCylinders,
       "cmmSysHarddiskHeads": cmmSysHarddiskHeads,
       "cmmSysHarddiskSectors": cmmSysHarddiskSectors,
       "cmmSysHarddiskUnformattedBytesorTrack": cmmSysHarddiskUnformattedBytesorTrack,
       "cmmSysHarddiskUnformattedBytesorSector": cmmSysHarddiskUnformattedBytesorSector,
       "cmmSysHarddiskRevisionNum": cmmSysHarddiskRevisionNum,
       "cmmSysHarddiskTotalsize": cmmSysHarddiskTotalsize,
       "cmmSysHarddiskUsedMem": cmmSysHarddiskUsedMem,
       "cmmSysHarddiskFreeMem": cmmSysHarddiskFreeMem,
       "cmmSysHarddiskUsageAlertThreshold": cmmSysHarddiskUsageAlertThreshold,
       "cmmSysHarddiskUsageCriticalThreshold": cmmSysHarddiskUsageCriticalThreshold,
       "cmmSysHardDiskRemainLifeAlertThreshold": cmmSysHardDiskRemainLifeAlertThreshold,
       "cmmSysHardDiskRemainLifeCriticalThreshold": cmmSysHardDiskRemainLifeCriticalThreshold,
       "cmmSysHardDiskRemainLife": cmmSysHardDiskRemainLife,
       "cmmSysHardDiskAvailableReservedSpaceAlertThreshold": cmmSysHardDiskAvailableReservedSpaceAlertThreshold,
       "cmmSysHardDiskAvailableReservedSpaceCriticalThreshold": cmmSysHardDiskAvailableReservedSpaceCriticalThreshold,
       "cmmSysHardDiskAvailableReservedSpace": cmmSysHardDiskAvailableReservedSpace,
       "cmmSysHardDiskReallocSectorsCount": cmmSysHardDiskReallocSectorsCount,
       "cmmSysHardDiskUncorrectSectorCount": cmmSysHardDiskUncorrectSectorCount,
       "cmmSysHardDiskActivityMonitoringInterval": cmmSysHardDiskActivityMonitoringInterval,
       "cmmSysHardDiskActivityMonitoringRead": cmmSysHardDiskActivityMonitoringRead,
       "cmmSysHardDiskActivityMonitoringWrite": cmmSysHardDiskActivityMonitoringWrite,
       "cmmSysHardDiskActivityMonitoringReadCurrent": cmmSysHardDiskActivityMonitoringReadCurrent,
       "cmmSysHardDiskActivityMonitoringWriteCurrent": cmmSysHardDiskActivityMonitoringWriteCurrent,
       "cmmSysHardDiskActivityMonitoringReadThreshold": cmmSysHardDiskActivityMonitoringReadThreshold,
       "cmmSysHardDiskActivityMonitoringWriteThreshold": cmmSysHardDiskActivityMonitoringWriteThreshold,
       "cmmSysHardDiskManufacturerId": cmmSysHardDiskManufacturerId,
       "cmmSysHardDiskManufactureDate": cmmSysHardDiskManufactureDate,
       "cmmSysHardDiskDeviceType": cmmSysHardDiskDeviceType,
       "cmmSysHardDiskCacheSize": cmmSysHardDiskCacheSize,
       "cmmSysHardDiskStorageStatus": cmmSysHardDiskStorageStatus,
       "cmmSystemStatusTable": cmmSystemStatusTable,
       "cmmSystemStatusEntry": cmmSystemStatusEntry,
       "cmmSystemMinorFaultStatus": cmmSystemMinorFaultStatus,
       "cmmSystemMajorFaultStatus": cmmSystemMajorFaultStatus,
       "cmmSysStatus": cmmSysStatus,
       "cmmSysLedColor": cmmSysLedColor,
       "cmmCpuCoreUtilTable": cmmCpuCoreUtilTable,
       "cmmCpuCoreUtilEntry": cmmCpuCoreUtilEntry,
       "cmmCpuCoreIndex": cmmCpuCoreIndex,
       "cmmCpuCoreUtilization": cmmCpuCoreUtilization,
       "cmmCpuCoreModelName": cmmCpuCoreModelName,
       "cmmPsuFruTable": cmmPsuFruTable,
       "cmmPsuFruEntry": cmmPsuFruEntry,
       "cmmPsuPpid": cmmPsuPpid,
       "cmmPsuCountryofOrigin": cmmPsuCountryofOrigin,
       "cmmPsuPpidPartNum": cmmPsuPpidPartNum,
       "cmmPsuPpidPartNumRev": cmmPsuPpidPartNumRev,
       "cmmPsuManufactureId": cmmPsuManufactureId,
       "cmmPsuDateCode": cmmPsuDateCode,
       "cmmPsuSerialNumber": cmmPsuSerialNumber,
       "cmmPsuPartNum": cmmPsuPartNum,
       "cmmPsuPartNumRev": cmmPsuPartNumRev,
       "cmmPsuNumOfFanPerTray": cmmPsuNumOfFanPerTray,
       "cmmPsuType": cmmPsuType,
       "cmmPsuServiceTag": cmmPsuServiceTag,
       "cmmPsuIanaNum": cmmPsuIanaNum,
       "cmmPsuFanMaxRpm": cmmPsuFanMaxRpm,
       "cmmPsuAirFlowDir": cmmPsuAirFlowDir,
       "cmmPsuMaxOutputWatt": cmmPsuMaxOutputWatt,
       "cmmFanFruTable": cmmFanFruTable,
       "cmmFanFruEntry": cmmFanFruEntry,
       "cmmFanPpid": cmmFanPpid,
       "cmmFanCountryofOrigin": cmmFanCountryofOrigin,
       "cmmFanPpidPartNum": cmmFanPpidPartNum,
       "cmmFanPpidPartNumRev": cmmFanPpidPartNumRev,
       "cmmFanManufactureId": cmmFanManufactureId,
       "cmmFanDateCode": cmmFanDateCode,
       "cmmFanSerialNumber": cmmFanSerialNumber,
       "cmmFanPartNum": cmmFanPartNum,
       "cmmFanPartNumRev": cmmFanPartNumRev,
       "cmmFanNumOfFanPerTray": cmmFanNumOfFanPerTray,
       "cmmFanType": cmmFanType,
       "cmmFanServiceTag": cmmFanServiceTag,
       "cmmFanIanaNum": cmmFanIanaNum,
       "cmmFanMaxRpm": cmmFanMaxRpm,
       "cmmSysCpldTable": cmmSysCpldTable,
       "cmmSysCpldEntry": cmmSysCpldEntry,
       "cmmSysCpldIndex": cmmSysCpldIndex,
       "cmmSysCpldName": cmmSysCpldName,
       "cmmSysCpldSupportedVer": cmmSysCpldSupportedVer,
       "cmmSysCpldCurrentVer": cmmSysCpldCurrentVer,
       "cmmTransDDMPage20h21hTable": cmmTransDDMPage20h21hTable,
       "cmmTransDDMPage20h21hEntry": cmmTransDDMPage20h21hEntry,
       "cmmTransPreFecBerVal": cmmTransPreFecBerVal,
       "cmmTransPreFecBerCriticMin": cmmTransPreFecBerCriticMin,
       "cmmTransPreFecBerCriticMax": cmmTransPreFecBerCriticMax,
       "cmmTransPreFecBerCriticalMin": cmmTransPreFecBerCriticalMin,
       "cmmTransPreFecBerCriticalMax": cmmTransPreFecBerCriticalMax,
       "cmmTransUncorrectedBerVal": cmmTransUncorrectedBerVal,
       "cmmTransUncorrectedBerValCriticMin": cmmTransUncorrectedBerValCriticMin,
       "cmmTransUncorrectedBerValCriticMax": cmmTransUncorrectedBerValCriticMax,
       "cmmTransUncorrectedBerValCriticalMin": cmmTransUncorrectedBerValCriticalMin,
       "cmmTransUncorrectedBerValCriticalMax": cmmTransUncorrectedBerValCriticalMax,
       "cmmTransSnrVal": cmmTransSnrVal,
       "cmmTransSnrCriticMin": cmmTransSnrCriticMin,
       "cmmTransSnrCriticMax": cmmTransSnrCriticMax,
       "cmmTransSnrCriticalMin": cmmTransSnrCriticalMin,
       "cmmTransSnrCriticalMax": cmmTransSnrCriticalMax,
       "cmmTransResIsiVal": cmmTransResIsiVal,
       "cmmTransResIsiCriticMin": cmmTransResIsiCriticMin,
       "cmmTransResIsiCriticMax": cmmTransResIsiCriticMax,
       "cmmTransResIsiCriticalMin": cmmTransResIsiCriticalMin,
       "cmmTransResIsiCriticalMax": cmmTransResIsiCriticalMax,
       "cmmTransLvlTransVal": cmmTransLvlTransVal,
       "cmmTransLvlTransCriticMin": cmmTransLvlTransCriticMin,
       "cmmTransLvlTransCriticMax": cmmTransLvlTransCriticMax,
       "cmmTransLvlTransCriticalMin": cmmTransLvlTransCriticalMin,
       "cmmTransLvlTransCriticalMax": cmmTransLvlTransCriticalMax,
       "cmmTransTecCurrErrVal": cmmTransTecCurrErrVal,
       "cmmTransTecCurrErrCriticMin": cmmTransTecCurrErrCriticMin,
       "cmmTransTecCurrErrCriticMax": cmmTransTecCurrErrCriticMax,
       "cmmTransTecCurrErrCriticalMin": cmmTransTecCurrErrCriticalMin,
       "cmmTransTecCurrErrCriticalMax": cmmTransTecCurrErrCriticalMax,
       "cmmTransLaserTempVal": cmmTransLaserTempVal,
       "cmmTransLaserTempCriticMin": cmmTransLaserTempCriticMin,
       "cmmTransLaserTempCriticMax": cmmTransLaserTempCriticMax,
       "cmmTransLaserTempCriticalMin": cmmTransLaserTempCriticalMin,
       "cmmTransLaserTempCriticalMax": cmmTransLaserTempCriticalMax,
       "cmmSysHardDiskPartitionTable": cmmSysHardDiskPartitionTable,
       "cmmSysHardDiskPartitionEntry": cmmSysHardDiskPartitionEntry,
       "cmmSysHardDiskPartitionIndex": cmmSysHardDiskPartitionIndex,
       "cmmSysHardDiskPartitionName": cmmSysHardDiskPartitionName,
       "cmmSysHardDiskPartitionTotalMem": cmmSysHardDiskPartitionTotalMem,
       "cmmSysHardDiskPartitionUsedMem": cmmSysHardDiskPartitionUsedMem,
       "cmmSysHardDiskPartitionFreeMem": cmmSysHardDiskPartitionFreeMem,
       "cmmAlarmObjects": cmmAlarmObjects,
       "cmmAlarmVariable": cmmAlarmVariable,
       "cmmAlarmVarInteger": cmmAlarmVarInteger,
       "cmmAlarmVarString": cmmAlarmVarString,
       "cmmAlarmMibNotifications": cmmAlarmMibNotifications,
       "cmmCpuLoad15MinAlert": cmmCpuLoad15MinAlert,
       "cmmCpuLoad5MinAlert": cmmCpuLoad5MinAlert,
       "cmmCpuLoad1MinCritical": cmmCpuLoad1MinCritical,
       "cmmCpuLoad1MinAlert": cmmCpuLoad1MinAlert,
       "cmmCpuLoad1MinCriticalRecovery": cmmCpuLoad1MinCriticalRecovery,
       "cmmCpuLoad15MinAlertRecovery": cmmCpuLoad15MinAlertRecovery,
       "cmmCpuLoad5MinAlertRecovery": cmmCpuLoad5MinAlertRecovery,
       "cmmCpuLoad1MinAlertRecovery": cmmCpuLoad1MinAlertRecovery,
       "cmmCpuCoreUtilHighCritical": cmmCpuCoreUtilHighCritical,
       "cmmCpuCoreUtilHighAlert": cmmCpuCoreUtilHighAlert,
       "cmmCpuCoreUtilHighCriticalRecovery": cmmCpuCoreUtilHighCriticalRecovery,
       "cmmCpuCoreUtilHighAlertRecovery": cmmCpuCoreUtilHighAlertRecovery,
       "cmmRamUsageRisingCritical": cmmRamUsageRisingCritical,
       "cmmRamUsageRisingAlert": cmmRamUsageRisingAlert,
       "cmmRamUsageCriticalRecovery": cmmRamUsageCriticalRecovery,
       "cmmRamUsageAlertRecovery": cmmRamUsageAlertRecovery,
       "cmmHardDiskUsageRisingCritical": cmmHardDiskUsageRisingCritical,
       "cmmHardDiskUsageRisingAlert": cmmHardDiskUsageRisingAlert,
       "cmmHardDiskUsageCriticalRecovery": cmmHardDiskUsageCriticalRecovery,
       "cmmHardDiskUsageAlertRecovery": cmmHardDiskUsageAlertRecovery,
       "cmmSysHardDiskRemainLifeRisingAlert": cmmSysHardDiskRemainLifeRisingAlert,
       "cmmSysHardDiskRemainLifeRisingCritical": cmmSysHardDiskRemainLifeRisingCritical,
       "cmmSysHardDiskAvailableReservedSpaceAlert": cmmSysHardDiskAvailableReservedSpaceAlert,
       "cmmSysHardDiskAvailableReservedSpaceCritical": cmmSysHardDiskAvailableReservedSpaceCritical,
       "cmmSysHardDiskReallocSectorsCountAlert": cmmSysHardDiskReallocSectorsCountAlert,
       "cmmSysHardDiskUncorrectableSectorCountCritical": cmmSysHardDiskUncorrectableSectorCountCritical,
       "cmmSysHardDiskActivityMonitoringReadAlert": cmmSysHardDiskActivityMonitoringReadAlert,
       "cmmSysHardDiskActivityMonitoringReadRecovery": cmmSysHardDiskActivityMonitoringReadRecovery,
       "cmmSysHardDiskActivityMonitoringWriteAlert": cmmSysHardDiskActivityMonitoringWriteAlert,
       "cmmSysHardDiskActivityMonitoringWriteRecovery": cmmSysHardDiskActivityMonitoringWriteRecovery,
       "cmmSysHardDiskStorageStatusNotification": cmmSysHardDiskStorageStatusNotification,
       "cmmTemperatureLowEmergency": cmmTemperatureLowEmergency,
       "cmmTemperatureHighEmergency": cmmTemperatureHighEmergency,
       "cmmTemperatureLowCritical": cmmTemperatureLowCritical,
       "cmmTemperatureHighCritical": cmmTemperatureHighCritical,
       "cmmTemperatureLowAlert": cmmTemperatureLowAlert,
       "cmmTemperatureHighAlert": cmmTemperatureHighAlert,
       "cmmTemperatureHighCriticalRecovery": cmmTemperatureHighCriticalRecovery,
       "cmmTemperatureLowCriticalRecovery": cmmTemperatureLowCriticalRecovery,
       "cmmTemperatureHighAlertRecovery": cmmTemperatureHighAlertRecovery,
       "cmmTemperatureLowAlertRecovery": cmmTemperatureLowAlertRecovery,
       "cmmPsuInsertedNotify": cmmPsuInsertedNotify,
       "cmmPsuRemovedCritical": cmmPsuRemovedCritical,
       "cmmPsuAcFailedCritical": cmmPsuAcFailedCritical,
       "cmmPsuAcRecover": cmmPsuAcRecover,
       "cmmPsu12vPgFailedCritical": cmmPsu12vPgFailedCritical,
       "cmmPsu12vPgRecover": cmmPsu12vPgRecover,
       "cmmSysPSUInputVoltageHighAlert": cmmSysPSUInputVoltageHighAlert,
       "cmmSysPSUInputVoltageLowAlert": cmmSysPSUInputVoltageLowAlert,
       "cmmSysPSUInputVoltageHighCritical": cmmSysPSUInputVoltageHighCritical,
       "cmmSysPSUInputVoltageLowCritical": cmmSysPSUInputVoltageLowCritical,
       "cmmSysPSUInputVoltageHighAlertRecovery": cmmSysPSUInputVoltageHighAlertRecovery,
       "cmmSysPSUInputVoltageLowAlertRecovery": cmmSysPSUInputVoltageLowAlertRecovery,
       "cmmSysPSUInputVoltageHighCriticalRecovery": cmmSysPSUInputVoltageHighCriticalRecovery,
       "cmmSysPSUInputVoltageLowCriticalRecovery": cmmSysPSUInputVoltageLowCriticalRecovery,
       "cmmSysPSUOutputVoltageHighAlert": cmmSysPSUOutputVoltageHighAlert,
       "cmmSysPSUOutputVoltageLowAlert": cmmSysPSUOutputVoltageLowAlert,
       "cmmSysPSUOutputVoltageHighCritical": cmmSysPSUOutputVoltageHighCritical,
       "cmmSysPSUOutputVoltageLowCritical": cmmSysPSUOutputVoltageLowCritical,
       "cmmSysPSUOutputVoltageHighAlertRecovery": cmmSysPSUOutputVoltageHighAlertRecovery,
       "cmmSysPSUOutputVoltageLowAlertRecovery": cmmSysPSUOutputVoltageLowAlertRecovery,
       "cmmSysPSUOutputVoltageHighCriticalRecovery": cmmSysPSUOutputVoltageHighCriticalRecovery,
       "cmmSysPSUOutputVoltageLowCriticalRecovery": cmmSysPSUOutputVoltageLowCriticalRecovery,
       "cmmSysPSUInputPowerHighAlert": cmmSysPSUInputPowerHighAlert,
       "cmmSysPSUInputPowerLowAlert": cmmSysPSUInputPowerLowAlert,
       "cmmSysPSUInputPowerHighCritical": cmmSysPSUInputPowerHighCritical,
       "cmmSysPSUInputPowerLowCritical": cmmSysPSUInputPowerLowCritical,
       "cmmSysPSUInputPowerHighAlertRecovery": cmmSysPSUInputPowerHighAlertRecovery,
       "cmmSysPSUInputPowerLowAlertRecovery": cmmSysPSUInputPowerLowAlertRecovery,
       "cmmSysPSUInputPowerHighCriticalRecovery": cmmSysPSUInputPowerHighCriticalRecovery,
       "cmmSysPSUInputPowerLowCriticalRecovery": cmmSysPSUInputPowerLowCriticalRecovery,
       "cmmSysPSUOutputPowerHighAlert": cmmSysPSUOutputPowerHighAlert,
       "cmmSysPSUOutputPowerLowAlert": cmmSysPSUOutputPowerLowAlert,
       "cmmSysPSUOutputPowerHighCritical": cmmSysPSUOutputPowerHighCritical,
       "cmmSysPSUOutputPowerLowCritical": cmmSysPSUOutputPowerLowCritical,
       "cmmSysPSUOutputPowerHighAlertRecovery": cmmSysPSUOutputPowerHighAlertRecovery,
       "cmmSysPSUOutputPowerLowAlertRecovery": cmmSysPSUOutputPowerLowAlertRecovery,
       "cmmSysPSUOutputPowerHighCriticalRecovery": cmmSysPSUOutputPowerHighCriticalRecovery,
       "cmmSysPSUOutputPowerLowCriticalRecovery": cmmSysPSUOutputPowerLowCriticalRecovery,
       "cmmSysPSUInputCurrentHighAlert": cmmSysPSUInputCurrentHighAlert,
       "cmmSysPSUInputCurrentLowAlert": cmmSysPSUInputCurrentLowAlert,
       "cmmSysPSUInputCurrentHighCritical": cmmSysPSUInputCurrentHighCritical,
       "cmmSysPSUInputCurrentLowCritical": cmmSysPSUInputCurrentLowCritical,
       "cmmSysPSUInputCurrentHighAlertRecovery": cmmSysPSUInputCurrentHighAlertRecovery,
       "cmmSysPSUInputCurrentLowAlertRecovery": cmmSysPSUInputCurrentLowAlertRecovery,
       "cmmSysPSUInputCurrentHighCriticalRecovery": cmmSysPSUInputCurrentHighCriticalRecovery,
       "cmmSysPSUInputCurrentLowCriticalRecovery": cmmSysPSUInputCurrentLowCriticalRecovery,
       "cmmSysPSUOutputCurrentHighAlert": cmmSysPSUOutputCurrentHighAlert,
       "cmmSysPSUOutputCurrentLowAlert": cmmSysPSUOutputCurrentLowAlert,
       "cmmSysPSUOutputCurrentHighCritical": cmmSysPSUOutputCurrentHighCritical,
       "cmmSysPSUOutputCurrentLowCritical": cmmSysPSUOutputCurrentLowCritical,
       "cmmSysPSUOutputCurrentHighAlertRecovery": cmmSysPSUOutputCurrentHighAlertRecovery,
       "cmmSysPSUOutputCurrentLowAlertRecovery": cmmSysPSUOutputCurrentLowAlertRecovery,
       "cmmSysPSUOutputCurrentHighCriticalRecovery": cmmSysPSUOutputCurrentHighCriticalRecovery,
       "cmmSysPSUOutputCurrentLowCriticalRecovery": cmmSysPSUOutputCurrentLowCriticalRecovery,
       "cmmSysPSUTemperature1HighAlert": cmmSysPSUTemperature1HighAlert,
       "cmmSysPSUTemperature1LowAlert": cmmSysPSUTemperature1LowAlert,
       "cmmSysPSUTemperature1HighCritical": cmmSysPSUTemperature1HighCritical,
       "cmmSysPSUTemperature1LowCritical": cmmSysPSUTemperature1LowCritical,
       "cmmSysPSUTemperature1HighAlertRecovery": cmmSysPSUTemperature1HighAlertRecovery,
       "cmmSysPSUTemperature1LowAlertRecovery": cmmSysPSUTemperature1LowAlertRecovery,
       "cmmSysPSUTemperature1HighCriticalRecovery": cmmSysPSUTemperature1HighCriticalRecovery,
       "cmmSysPSUTemperature1LowCriticalRecovery": cmmSysPSUTemperature1LowCriticalRecovery,
       "cmmSysPSUTemperature2HighAlert": cmmSysPSUTemperature2HighAlert,
       "cmmSysPSUTemperature2LowAlert": cmmSysPSUTemperature2LowAlert,
       "cmmSysPSUTemperature2HighCritical": cmmSysPSUTemperature2HighCritical,
       "cmmSysPSUTemperature2LowCritical": cmmSysPSUTemperature2LowCritical,
       "cmmSysPSUTemperature2HighAlertRecovery": cmmSysPSUTemperature2HighAlertRecovery,
       "cmmSysPSUTemperature2LowAlertRecovery": cmmSysPSUTemperature2LowAlertRecovery,
       "cmmSysPSUTemperature2HighCriticalRecovery": cmmSysPSUTemperature2HighCriticalRecovery,
       "cmmSysPSUTemperature2LowCriticalRecovery": cmmSysPSUTemperature2LowCriticalRecovery,
       "cmmSysPSUTemperature3HighAlert": cmmSysPSUTemperature3HighAlert,
       "cmmSysPSUTemperature3LowAlert": cmmSysPSUTemperature3LowAlert,
       "cmmSysPSUTemperature3HighCritical": cmmSysPSUTemperature3HighCritical,
       "cmmSysPSUTemperature3LowCritical": cmmSysPSUTemperature3LowCritical,
       "cmmSysPSUTemperature3HighAlertRecovery": cmmSysPSUTemperature3HighAlertRecovery,
       "cmmSysPSUTemperature3LowAlertRecovery": cmmSysPSUTemperature3LowAlertRecovery,
       "cmmSysPSUTemperature3HighCriticalRecovery": cmmSysPSUTemperature3HighCriticalRecovery,
       "cmmSysPSUTemperature3LowCriticalRecovery": cmmSysPSUTemperature3LowCriticalRecovery,
       "cmmFanTrayInsertedNotify": cmmFanTrayInsertedNotify,
       "cmmFanTrayRemovedCritical": cmmFanTrayRemovedCritical,
       "cmmFanTrayFaultyCritical": cmmFanTrayFaultyCritical,
       "cmmFanTrayRecovered": cmmFanTrayRecovered,
       "cmmFanTrayStallCritical": cmmFanTrayStallCritical,
       "cmmFanTrayStallRecovered": cmmFanTrayStallRecovered,
       "cmmFanRPMMinNotify": cmmFanRPMMinNotify,
       "cmmFanRPMMaxCritical": cmmFanRPMMaxCritical,
       "cmmFanRPMDecreasedNotify": cmmFanRPMDecreasedNotify,
       "cmmFanRPMIncreasedNotify": cmmFanRPMIncreasedNotify,
       "cmmTransMibNotifications": cmmTransMibNotifications,
       "cmmTransAlertTempHigh": cmmTransAlertTempHigh,
       "cmmTransAlertTempLow": cmmTransAlertTempLow,
       "cmmTransCriticalTempHigh": cmmTransCriticalTempHigh,
       "cmmTransCriticalTempLow": cmmTransCriticalTempLow,
       "cmmTransNotifyTransceiverTempRecovered": cmmTransNotifyTransceiverTempRecovered,
       "cmmTransAlertVoltageHigh": cmmTransAlertVoltageHigh,
       "cmmTransAlertVoltageLow": cmmTransAlertVoltageLow,
       "cmmTransCriticalVoltageHigh": cmmTransCriticalVoltageHigh,
       "cmmTransCriticalVoltageLow": cmmTransCriticalVoltageLow,
       "cmmTransNotifyTransceiverVoltRecovered": cmmTransNotifyTransceiverVoltRecovered,
       "cmmTransAlertBiasHigh": cmmTransAlertBiasHigh,
       "cmmTransAlertBiasLow": cmmTransAlertBiasLow,
       "cmmTransCriticalBiashigh": cmmTransCriticalBiashigh,
       "cmmTransCriticalBiasLow": cmmTransCriticalBiasLow,
       "cmmTransNotifyTransceiverBiasRecovered": cmmTransNotifyTransceiverBiasRecovered,
       "cmmTransAlertRxPowerHigh": cmmTransAlertRxPowerHigh,
       "cmmTransAlertRxPowerLow": cmmTransAlertRxPowerLow,
       "cmmTransCriticalRxPowerHigh": cmmTransCriticalRxPowerHigh,
       "cmmTransCriticalRxPowerLow": cmmTransCriticalRxPowerLow,
       "cmmTransNotifyTransceiverRxPowRecovered": cmmTransNotifyTransceiverRxPowRecovered,
       "cmmTransAlertTxPowerHigh": cmmTransAlertTxPowerHigh,
       "cmmTransAlertTxPowerLow": cmmTransAlertTxPowerLow,
       "cmmTransCriticalTxPowerHigh": cmmTransCriticalTxPowerHigh,
       "cmmTransCriticalTxPowerLow": cmmTransCriticalTxPowerLow,
       "cmmTransNotifyTransceiverTxPowRecovered": cmmTransNotifyTransceiverTxPowRecovered,
       "cmmTransNotifyTransceiverInserted": cmmTransNotifyTransceiverInserted,
       "cmmTransCriticalTransceiverRemoved": cmmTransCriticalTransceiverRemoved,
       "cmmTransCriticalFaultyTransceiverInserted": cmmTransCriticalFaultyTransceiverInserted,
       "cmmCriticalIncompatibleTransceiverPresence": cmmCriticalIncompatibleTransceiverPresence,
       "cmmNotifyIncompatibleTransceiverRecovery": cmmNotifyIncompatibleTransceiverRecovery,
       "cmmTransXFPAlertVoltage2High": cmmTransXFPAlertVoltage2High,
       "cmmTransXFPAlertVoltage2Low": cmmTransXFPAlertVoltage2Low,
       "cmmTransXFPCriticalVoltage2High": cmmTransXFPCriticalVoltage2High,
       "cmmTransXFPCriticalVoltage2Low": cmmTransXFPCriticalVoltage2Low,
       "cmmTransNotifyTransceiverXFPVolt2Recovered": cmmTransNotifyTransceiverXFPVolt2Recovered,
       "cmmTransFrequencyErrorHighAlert": cmmTransFrequencyErrorHighAlert,
       "cmmTransFrequencyErrorLowAlert": cmmTransFrequencyErrorLowAlert,
       "cmmTransFrequencyErrorHighCritical": cmmTransFrequencyErrorHighCritical,
       "cmmTransFrequencyErrorLowCritical": cmmTransFrequencyErrorLowCritical,
       "cmmTransFrequencyErrorRecovery": cmmTransFrequencyErrorRecovery,
       "cmmTransWavelengthErrorHighAlert": cmmTransWavelengthErrorHighAlert,
       "cmmTransWavelengthErrorLowAlert": cmmTransWavelengthErrorLowAlert,
       "cmmTransWavelengthErrorHighCritical": cmmTransWavelengthErrorHighCritical,
       "cmmTransWavelengthErrorLowCritical": cmmTransWavelengthErrorLowCritical,
       "cmmTransWavelengthErrorRecovery": cmmTransWavelengthErrorRecovery,
       "cmmTransTECFaultCritical": cmmTransTECFaultCritical,
       "cmmTransTECFaultRecovery": cmmTransTECFaultRecovery,
       "cmmTransAlertPreFecBerErrHigh": cmmTransAlertPreFecBerErrHigh,
       "cmmTransAlertPreFecBerErrLow": cmmTransAlertPreFecBerErrLow,
       "cmmTransCriticalPreFecBerErrHigh": cmmTransCriticalPreFecBerErrHigh,
       "cmmTransCriticalPreFecBerErrLow": cmmTransCriticalPreFecBerErrLow,
       "cmmTransNotifyTransceiverPreFecBerRecovered": cmmTransNotifyTransceiverPreFecBerRecovered,
       "cmmTransAlertUncorrectedBerHigh": cmmTransAlertUncorrectedBerHigh,
       "cmmTransAlertUncorrectedBerLow": cmmTransAlertUncorrectedBerLow,
       "cmmTransCriticalUncorrectedBerHigh": cmmTransCriticalUncorrectedBerHigh,
       "cmmTransCriticalUncorrectedBerLow": cmmTransCriticalUncorrectedBerLow,
       "cmmTransNotifyTransceiverUncorrectedBerRecovered": cmmTransNotifyTransceiverUncorrectedBerRecovered,
       "cmmTransAlertSnrHigh": cmmTransAlertSnrHigh,
       "cmmTransAlertSnrLow": cmmTransAlertSnrLow,
       "cmmTransCriticalSnrHigh": cmmTransCriticalSnrHigh,
       "cmmTransCriticalSnrLow": cmmTransCriticalSnrLow,
       "cmmTransNotifyTransceiverSnrRecovered": cmmTransNotifyTransceiverSnrRecovered,
       "cmmTransAlertresIsiHigh": cmmTransAlertresIsiHigh,
       "cmmTransAlertresIsiLow": cmmTransAlertresIsiLow,
       "cmmTransCriticalResIsiHigh": cmmTransCriticalResIsiHigh,
       "cmmTransCriticalResIsiLow": cmmTransCriticalResIsiLow,
       "cmmTransNotifyTransceiverResIsiRecovered": cmmTransNotifyTransceiverResIsiRecovered,
       "cmmTransAlertLvlTranHigh": cmmTransAlertLvlTranHigh,
       "cmmTransAlertLvlTranLow": cmmTransAlertLvlTranLow,
       "cmmTransCriticalLvlTranHigh": cmmTransCriticalLvlTranHigh,
       "cmmTransCriticalLvlTranLow": cmmTransCriticalLvlTranLow,
       "cmmTransNotifyTransceiverLvlTranRecovered": cmmTransNotifyTransceiverLvlTranRecovered,
       "cmmTransAlertTecCurrErrHigh": cmmTransAlertTecCurrErrHigh,
       "cmmTransAlertTecCurrErrLow": cmmTransAlertTecCurrErrLow,
       "cmmTransCriticalTecCurrErrHigh": cmmTransCriticalTecCurrErrHigh,
       "cmmTransCriticalTecCurrErrLow": cmmTransCriticalTecCurrErrLow,
       "cmmTransNotifyTransceiverTecCurrErrRecovered": cmmTransNotifyTransceiverTecCurrErrRecovered,
       "cmmTransAlertLaserTempValHigh": cmmTransAlertLaserTempValHigh,
       "cmmTransAlertLaserTempValLow": cmmTransAlertLaserTempValLow,
       "cmmTransCriticalLaserTempValHigh": cmmTransCriticalLaserTempValHigh,
       "cmmTransCriticalLaserTempValLow": cmmTransCriticalLaserTempValLow,
       "cmmTransNotifyTransceiverLaserTempRecovered": cmmTransNotifyTransceiverLaserTempRecovered,
       "cmmTranAlertTransceiverPortRxLoss": cmmTranAlertTransceiverPortRxLoss,
       "cmmTransNotifyTransceiverPortRxLossRecovery": cmmTransNotifyTransceiverPortRxLossRecovery}
)
