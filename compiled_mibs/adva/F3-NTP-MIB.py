# SNMP MIB module (F3-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-NTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:25 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmBinAction,
 CmPmIntervalType,
 F3DisplayString,
 IpVersion,
 OperationalState,
 PerfCounter64,
 SecondaryState) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "F3DisplayString",
    "IpVersion",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortIndex,
 cmEthernetNetPortIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortIndex")

(CmNtpMode,
 CmNtpType) = mibBuilder.importSymbols(
    "CM-SYSTEM-MIB",
    "CmNtpMode",
    "CmNtpType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3NtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47)
)
if mibBuilder.loadTexts:
    f3NtpMIB.setRevisions(
        ("2022-08-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NtpFlowPointType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("server", 1)
    )



class NtpTimeScale(TextualConvention, Integer32):
    status = "current"
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
        *(("utc", 1),
          ("not-available", 2),
          ("local", 3),
          ("gps", 4))
    )



class ToggleValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("not-available", 3))
    )



class GnssSyncLossAction(TextualConvention, Integer32):
    status = "current"
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
        *(("strtm-16-li-nochg", 1),
          ("strtm-16-li-unkn", 2),
          ("strtm-1-li-unkn", 3),
          ("none", 4),
          ("not-available", 5))
    )



class NtpBroadcastInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("pkt1per8secs", 1),
          ("pkt1per16secs", 2),
          ("pkt1per32secs", 3),
          ("pkt1per64secs", 4),
          ("pkt1per128secs", 5),
          ("pkt1per256secs", 6),
          ("pkt1per512secs", 7),
          ("pkt1per1024secs", 8),
          ("pkt1per2048secs", 9),
          ("pkt1per4096secs", 10),
          ("pkt1per8192secs", 11),
          ("pkt1per16384secs", 12),
          ("pkt1per32768secs", 13),
          ("pkt1per65536secs", 14))
    )



class NtpVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntpv3", 1),
          ("ntpv4", 2))
    )



class NtpAssociationType(TextualConvention, Integer32):
    status = "current"
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
        *(("not-available", 1),
          ("symmetric-active", 2),
          ("symmetric-passive", 3),
          ("server-only", 4))
    )



class NtpPollingInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sec16", 1),
          ("sec32", 2),
          ("sec64", 3),
          ("sec128", 4),
          ("sec256", 5),
          ("sec512", 6),
          ("sec1024", 7))
    )



# MIB Managed Objects in the order of their OIDs

_F3NtpObjects_ObjectIdentity = ObjectIdentity
f3NtpObjects = _F3NtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1)
)
_F3NtpClockTable_Object = MibTable
f3NtpClockTable = _F3NtpClockTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1)
)
if mibBuilder.loadTexts:
    f3NtpClockTable.setStatus("current")
_F3NtpClockEntry_Object = MibTableRow
f3NtpClockEntry = _F3NtpClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1)
)
f3NtpClockEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
)
if mibBuilder.loadTexts:
    f3NtpClockEntry.setStatus("current")
_F3NtpClockIndex_Type = Integer32
_F3NtpClockIndex_Object = MibTableColumn
f3NtpClockIndex = _F3NtpClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 1),
    _F3NtpClockIndex_Type()
)
f3NtpClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpClockIndex.setStatus("current")


class _F3NtpClockAlias_Type(DisplayString):
    """Custom type f3NtpClockAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3NtpClockAlias_Type.__name__ = "DisplayString"
_F3NtpClockAlias_Object = MibTableColumn
f3NtpClockAlias = _F3NtpClockAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 2),
    _F3NtpClockAlias_Type()
)
f3NtpClockAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpClockAlias.setStatus("current")
_F3NtpClockAdminState_Type = AdminState
_F3NtpClockAdminState_Object = MibTableColumn
f3NtpClockAdminState = _F3NtpClockAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 3),
    _F3NtpClockAdminState_Type()
)
f3NtpClockAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpClockAdminState.setStatus("current")
_F3NtpClockOperationalState_Type = OperationalState
_F3NtpClockOperationalState_Object = MibTableColumn
f3NtpClockOperationalState = _F3NtpClockOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 4),
    _F3NtpClockOperationalState_Type()
)
f3NtpClockOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockOperationalState.setStatus("current")
_F3NtpClockTimeClock_Type = VariablePointer
_F3NtpClockTimeClock_Object = MibTableColumn
f3NtpClockTimeClock = _F3NtpClockTimeClock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 5),
    _F3NtpClockTimeClock_Type()
)
f3NtpClockTimeClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpClockTimeClock.setStatus("current")
_F3NtpClockStratumLevel_Type = Unsigned32
_F3NtpClockStratumLevel_Object = MibTableColumn
f3NtpClockStratumLevel = _F3NtpClockStratumLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 6),
    _F3NtpClockStratumLevel_Type()
)
f3NtpClockStratumLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockStratumLevel.setStatus("current")
_F3NtpClockLeapIndicator_Type = Unsigned32
_F3NtpClockLeapIndicator_Object = MibTableColumn
f3NtpClockLeapIndicator = _F3NtpClockLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 7),
    _F3NtpClockLeapIndicator_Type()
)
f3NtpClockLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockLeapIndicator.setStatus("current")


class _F3NtpClockTimeScale_Type(DisplayString):
    """Custom type f3NtpClockTimeScale based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_F3NtpClockTimeScale_Type.__name__ = "DisplayString"
_F3NtpClockTimeScale_Object = MibTableColumn
f3NtpClockTimeScale = _F3NtpClockTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 8),
    _F3NtpClockTimeScale_Type()
)
f3NtpClockTimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockTimeScale.setStatus("deprecated")
_F3NtpClockPrecision_Type = Unsigned32
_F3NtpClockPrecision_Object = MibTableColumn
f3NtpClockPrecision = _F3NtpClockPrecision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 9),
    _F3NtpClockPrecision_Type()
)
f3NtpClockPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockPrecision.setStatus("current")
_F3NtpClockRootDelay_Type = Unsigned32
_F3NtpClockRootDelay_Object = MibTableColumn
f3NtpClockRootDelay = _F3NtpClockRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 10),
    _F3NtpClockRootDelay_Type()
)
f3NtpClockRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockRootDelay.setStatus("current")
_F3NtpClockRootDispersion_Type = Unsigned32
_F3NtpClockRootDispersion_Object = MibTableColumn
f3NtpClockRootDispersion = _F3NtpClockRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 11),
    _F3NtpClockRootDispersion_Type()
)
f3NtpClockRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockRootDispersion.setStatus("current")
_F3NtpClockNtpMode_Type = CmNtpMode
_F3NtpClockNtpMode_Object = MibTableColumn
f3NtpClockNtpMode = _F3NtpClockNtpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 12),
    _F3NtpClockNtpMode_Type()
)
f3NtpClockNtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpClockNtpMode.setStatus("current")
_F3NtpClockNtpType_Type = CmNtpType
_F3NtpClockNtpType_Object = MibTableColumn
f3NtpClockNtpType = _F3NtpClockNtpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 13),
    _F3NtpClockNtpType_Type()
)
f3NtpClockNtpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpClockNtpType.setStatus("current")
_F3NtpClockNtpAuthentication_Type = ToggleValue
_F3NtpClockNtpAuthentication_Object = MibTableColumn
f3NtpClockNtpAuthentication = _F3NtpClockNtpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 14),
    _F3NtpClockNtpAuthentication_Type()
)
f3NtpClockNtpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpClockNtpAuthentication.setStatus("current")
_F3NtpClockServerState_Type = ToggleValue
_F3NtpClockServerState_Object = MibTableColumn
f3NtpClockServerState = _F3NtpClockServerState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 15),
    _F3NtpClockServerState_Type()
)
f3NtpClockServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpClockServerState.setStatus("current")
_F3NtpClockTimeReferenceLossHandling_Type = GnssSyncLossAction
_F3NtpClockTimeReferenceLossHandling_Object = MibTableColumn
f3NtpClockTimeReferenceLossHandling = _F3NtpClockTimeReferenceLossHandling_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 16),
    _F3NtpClockTimeReferenceLossHandling_Type()
)
f3NtpClockTimeReferenceLossHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpClockTimeReferenceLossHandling.setStatus("current")


class _F3NtpClockRefClockId_Type(DisplayString):
    """Custom type f3NtpClockRefClockId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_F3NtpClockRefClockId_Type.__name__ = "DisplayString"
_F3NtpClockRefClockId_Object = MibTableColumn
f3NtpClockRefClockId = _F3NtpClockRefClockId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 17),
    _F3NtpClockRefClockId_Type()
)
f3NtpClockRefClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockRefClockId.setStatus("current")
_F3NtpClockStorageType_Type = StorageType
_F3NtpClockStorageType_Object = MibTableColumn
f3NtpClockStorageType = _F3NtpClockStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 18),
    _F3NtpClockStorageType_Type()
)
f3NtpClockStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpClockStorageType.setStatus("current")
_F3NtpClockRowStatus_Type = RowStatus
_F3NtpClockRowStatus_Object = MibTableColumn
f3NtpClockRowStatus = _F3NtpClockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 19),
    _F3NtpClockRowStatus_Type()
)
f3NtpClockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpClockRowStatus.setStatus("current")
_F3NtpAuthenticationSecureMode_Type = ToggleValue
_F3NtpAuthenticationSecureMode_Object = MibTableColumn
f3NtpAuthenticationSecureMode = _F3NtpAuthenticationSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 20),
    _F3NtpAuthenticationSecureMode_Type()
)
f3NtpAuthenticationSecureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpAuthenticationSecureMode.setStatus("current")
_F3NtpAutokeyCtrl_Type = ToggleValue
_F3NtpAutokeyCtrl_Object = MibTableColumn
f3NtpAutokeyCtrl = _F3NtpAutokeyCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 21),
    _F3NtpAutokeyCtrl_Type()
)
f3NtpAutokeyCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAutokeyCtrl.setStatus("current")
_F3NtpClockOffset_Type = PerfCounter64
_F3NtpClockOffset_Object = MibTableColumn
f3NtpClockOffset = _F3NtpClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 22),
    _F3NtpClockOffset_Type()
)
f3NtpClockOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockOffset.setStatus("current")
_F3NtpClockSecondaryState_Type = SecondaryState
_F3NtpClockSecondaryState_Object = MibTableColumn
f3NtpClockSecondaryState = _F3NtpClockSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 1, 1, 23),
    _F3NtpClockSecondaryState_Type()
)
f3NtpClockSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpClockSecondaryState.setStatus("current")
_F3NCITable_Object = MibTable
f3NCITable = _F3NCITable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2)
)
if mibBuilder.loadTexts:
    f3NCITable.setStatus("current")
_F3NCIEntry_Object = MibTableRow
f3NCIEntry = _F3NCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1)
)
f3NCIEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NCIIndex"),
)
if mibBuilder.loadTexts:
    f3NCIEntry.setStatus("current")
_F3NCIIndex_Type = Integer32
_F3NCIIndex_Object = MibTableColumn
f3NCIIndex = _F3NCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 1),
    _F3NCIIndex_Type()
)
f3NCIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NCIIndex.setStatus("current")


class _F3NCIAlias_Type(DisplayString):
    """Custom type f3NCIAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3NCIAlias_Type.__name__ = "DisplayString"
_F3NCIAlias_Object = MibTableColumn
f3NCIAlias = _F3NCIAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 2),
    _F3NCIAlias_Type()
)
f3NCIAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIAlias.setStatus("current")
_F3NCIAdminState_Type = AdminState
_F3NCIAdminState_Object = MibTableColumn
f3NCIAdminState = _F3NCIAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 3),
    _F3NCIAdminState_Type()
)
f3NCIAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIAdminState.setStatus("current")
_F3NCIOperationalState_Type = OperationalState
_F3NCIOperationalState_Object = MibTableColumn
f3NCIOperationalState = _F3NCIOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 4),
    _F3NCIOperationalState_Type()
)
f3NCIOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIOperationalState.setStatus("current")


class _F3NCIIfName_Type(DisplayString):
    """Custom type f3NCIIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3NCIIfName_Type.__name__ = "DisplayString"
_F3NCIIfName_Object = MibTableColumn
f3NCIIfName = _F3NCIIfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 5),
    _F3NCIIfName_Type()
)
f3NCIIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIIfName.setStatus("current")
_F3NCIIpProtocol_Type = IpVersion
_F3NCIIpProtocol_Object = MibTableColumn
f3NCIIpProtocol = _F3NCIIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 6),
    _F3NCIIpProtocol_Type()
)
f3NCIIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIIpProtocol.setStatus("current")
_F3NCIIpV4Address_Type = IpAddress
_F3NCIIpV4Address_Object = MibTableColumn
f3NCIIpV4Address = _F3NCIIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 7),
    _F3NCIIpV4Address_Type()
)
f3NCIIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIIpV4Address.setStatus("current")
_F3NCIIpV4SubnetMask_Type = IpAddress
_F3NCIIpV4SubnetMask_Object = MibTableColumn
f3NCIIpV4SubnetMask = _F3NCIIpV4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 8),
    _F3NCIIpV4SubnetMask_Type()
)
f3NCIIpV4SubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIIpV4SubnetMask.setStatus("current")
_F3NCIDscp_Type = Unsigned32
_F3NCIDscp_Object = MibTableColumn
f3NCIDscp = _F3NCIDscp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 9),
    _F3NCIDscp_Type()
)
f3NCIDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIDscp.setStatus("current")
_F3NCIStorageType_Type = StorageType
_F3NCIStorageType_Object = MibTableColumn
f3NCIStorageType = _F3NCIStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 10),
    _F3NCIStorageType_Type()
)
f3NCIStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIStorageType.setStatus("current")
_F3NCIRowStatus_Type = RowStatus
_F3NCIRowStatus_Object = MibTableColumn
f3NCIRowStatus = _F3NCIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 11),
    _F3NCIRowStatus_Type()
)
f3NCIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIRowStatus.setStatus("current")
_F3NCIIpV6UdpChecksum_Type = ToggleValue
_F3NCIIpV6UdpChecksum_Object = MibTableColumn
f3NCIIpV6UdpChecksum = _F3NCIIpV6UdpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 12),
    _F3NCIIpV6UdpChecksum_Type()
)
f3NCIIpV6UdpChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIIpV6UdpChecksum.setStatus("current")
_F3NCIIpV6Address_Type = Ipv6Address
_F3NCIIpV6Address_Object = MibTableColumn
f3NCIIpV6Address = _F3NCIIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 13),
    _F3NCIIpV6Address_Type()
)
f3NCIIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIIpV6Address.setStatus("current")


class _F3NCIIpV6AddrPrefixLength_Type(Integer32):
    """Custom type f3NCIIpV6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_F3NCIIpV6AddrPrefixLength_Type.__name__ = "Integer32"
_F3NCIIpV6AddrPrefixLength_Object = MibTableColumn
f3NCIIpV6AddrPrefixLength = _F3NCIIpV6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 14),
    _F3NCIIpV6AddrPrefixLength_Type()
)
f3NCIIpV6AddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIIpV6AddrPrefixLength.setStatus("current")
_F3NCIIpV4Gateway_Type = IpAddress
_F3NCIIpV4Gateway_Object = MibTableColumn
f3NCIIpV4Gateway = _F3NCIIpV4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 15),
    _F3NCIIpV4Gateway_Type()
)
f3NCIIpV4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIIpV4Gateway.setStatus("current")
_F3NCIIpV6Gateway_Type = Ipv6Address
_F3NCIIpV6Gateway_Object = MibTableColumn
f3NCIIpV6Gateway = _F3NCIIpV6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 16),
    _F3NCIIpV6Gateway_Type()
)
f3NCIIpV6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIIpV6Gateway.setStatus("current")
_F3NCIDefaultGatewayControl_Type = ToggleValue
_F3NCIDefaultGatewayControl_Object = MibTableColumn
f3NCIDefaultGatewayControl = _F3NCIDefaultGatewayControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 17),
    _F3NCIDefaultGatewayControl_Type()
)
f3NCIDefaultGatewayControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIDefaultGatewayControl.setStatus("current")
_F3NCITimeServiceControl_Type = ToggleValue
_F3NCITimeServiceControl_Object = MibTableColumn
f3NCITimeServiceControl = _F3NCITimeServiceControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 18),
    _F3NCITimeServiceControl_Type()
)
f3NCITimeServiceControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCITimeServiceControl.setStatus("current")
_F3NCIDaytimeServiceControl_Type = ToggleValue
_F3NCIDaytimeServiceControl_Object = MibTableColumn
f3NCIDaytimeServiceControl = _F3NCIDaytimeServiceControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 19),
    _F3NCIDaytimeServiceControl_Type()
)
f3NCIDaytimeServiceControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIDaytimeServiceControl.setStatus("current")
_F3NCIBroadcastState_Type = ToggleValue
_F3NCIBroadcastState_Object = MibTableColumn
f3NCIBroadcastState = _F3NCIBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 20),
    _F3NCIBroadcastState_Type()
)
f3NCIBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIBroadcastState.setStatus("current")
_F3NCIBroadcastIpV4Address_Type = IpAddress
_F3NCIBroadcastIpV4Address_Object = MibTableColumn
f3NCIBroadcastIpV4Address = _F3NCIBroadcastIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 21),
    _F3NCIBroadcastIpV4Address_Type()
)
f3NCIBroadcastIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIBroadcastIpV4Address.setStatus("current")
_F3NCIBroadcastIpV6Address_Type = Ipv6Address
_F3NCIBroadcastIpV6Address_Object = MibTableColumn
f3NCIBroadcastIpV6Address = _F3NCIBroadcastIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 22),
    _F3NCIBroadcastIpV6Address_Type()
)
f3NCIBroadcastIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIBroadcastIpV6Address.setStatus("current")
_F3NCIBroadcastInterval_Type = NtpBroadcastInterval
_F3NCIBroadcastInterval_Object = MibTableColumn
f3NCIBroadcastInterval = _F3NCIBroadcastInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 23),
    _F3NCIBroadcastInterval_Type()
)
f3NCIBroadcastInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIBroadcastInterval.setStatus("current")


class _F3NCIBroadcastMaxHops_Type(Integer32):
    """Custom type f3NCIBroadcastMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3NCIBroadcastMaxHops_Type.__name__ = "Integer32"
_F3NCIBroadcastMaxHops_Object = MibTableColumn
f3NCIBroadcastMaxHops = _F3NCIBroadcastMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 24),
    _F3NCIBroadcastMaxHops_Type()
)
f3NCIBroadcastMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIBroadcastMaxHops.setStatus("current")


class _F3NCIBroadcastSymKeyId_Type(Integer32):
    """Custom type f3NCIBroadcastSymKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NCIBroadcastSymKeyId_Type.__name__ = "Integer32"
_F3NCIBroadcastSymKeyId_Object = MibTableColumn
f3NCIBroadcastSymKeyId = _F3NCIBroadcastSymKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 25),
    _F3NCIBroadcastSymKeyId_Type()
)
f3NCIBroadcastSymKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIBroadcastSymKeyId.setStatus("current")
_F3NCIBroadcastNtpVersion_Type = NtpVersion
_F3NCIBroadcastNtpVersion_Object = MibTableColumn
f3NCIBroadcastNtpVersion = _F3NCIBroadcastNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 26),
    _F3NCIBroadcastNtpVersion_Type()
)
f3NCIBroadcastNtpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIBroadcastNtpVersion.setStatus("current")
_F3NCIAssociationMode_Type = NtpAssociationType
_F3NCIAssociationMode_Object = MibTableColumn
f3NCIAssociationMode = _F3NCIAssociationMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 27),
    _F3NCIAssociationMode_Type()
)
f3NCIAssociationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIAssociationMode.setStatus("current")
_F3NCIPeer1IpV4Address_Type = IpAddress
_F3NCIPeer1IpV4Address_Object = MibTableColumn
f3NCIPeer1IpV4Address = _F3NCIPeer1IpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 28),
    _F3NCIPeer1IpV4Address_Type()
)
f3NCIPeer1IpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIPeer1IpV4Address.setStatus("current")
_F3NCIPeer2IpV4Address_Type = IpAddress
_F3NCIPeer2IpV4Address_Object = MibTableColumn
f3NCIPeer2IpV4Address = _F3NCIPeer2IpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 29),
    _F3NCIPeer2IpV4Address_Type()
)
f3NCIPeer2IpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIPeer2IpV4Address.setStatus("current")
_F3NCIPeer3IpV4Address_Type = IpAddress
_F3NCIPeer3IpV4Address_Object = MibTableColumn
f3NCIPeer3IpV4Address = _F3NCIPeer3IpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 30),
    _F3NCIPeer3IpV4Address_Type()
)
f3NCIPeer3IpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCIPeer3IpV4Address.setStatus("current")
_F3NCIPeer1IpV6Address_Type = Ipv6Address
_F3NCIPeer1IpV6Address_Object = MibTableColumn
f3NCIPeer1IpV6Address = _F3NCIPeer1IpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 31),
    _F3NCIPeer1IpV6Address_Type()
)
f3NCIPeer1IpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIPeer1IpV6Address.setStatus("current")
_F3NCIPeer2IpV6Address_Type = Ipv6Address
_F3NCIPeer2IpV6Address_Object = MibTableColumn
f3NCIPeer2IpV6Address = _F3NCIPeer2IpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 32),
    _F3NCIPeer2IpV6Address_Type()
)
f3NCIPeer2IpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIPeer2IpV6Address.setStatus("current")
_F3NCIPeer3IpV6Address_Type = Ipv6Address
_F3NCIPeer3IpV6Address_Object = MibTableColumn
f3NCIPeer3IpV6Address = _F3NCIPeer3IpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 33),
    _F3NCIPeer3IpV6Address_Type()
)
f3NCIPeer3IpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIPeer3IpV6Address.setStatus("current")
_F3NCIPeerMinInterval_Type = NtpBroadcastInterval
_F3NCIPeerMinInterval_Object = MibTableColumn
f3NCIPeerMinInterval = _F3NCIPeerMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 34),
    _F3NCIPeerMinInterval_Type()
)
f3NCIPeerMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIPeerMinInterval.setStatus("current")
_F3NCIPeerMaxInterval_Type = NtpBroadcastInterval
_F3NCIPeerMaxInterval_Object = MibTableColumn
f3NCIPeerMaxInterval = _F3NCIPeerMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 35),
    _F3NCIPeerMaxInterval_Type()
)
f3NCIPeerMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIPeerMaxInterval.setStatus("current")
_F3NCIPeerSymKeyIdList_Type = DisplayString
_F3NCIPeerSymKeyIdList_Object = MibTableColumn
f3NCIPeerSymKeyIdList = _F3NCIPeerSymKeyIdList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 36),
    _F3NCIPeerSymKeyIdList_Type()
)
f3NCIPeerSymKeyIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIPeerSymKeyIdList.setStatus("current")
_F3NCITimeScale_Type = NtpTimeScale
_F3NCITimeScale_Object = MibTableColumn
f3NCITimeScale = _F3NCITimeScale_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 37),
    _F3NCITimeScale_Type()
)
f3NCITimeScale.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCITimeScale.setStatus("current")
_F3NCICurrentTimeOfDay_Type = DateAndTime
_F3NCICurrentTimeOfDay_Object = MibTableColumn
f3NCICurrentTimeOfDay = _F3NCICurrentTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 38),
    _F3NCICurrentTimeOfDay_Type()
)
f3NCICurrentTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCICurrentTimeOfDay.setStatus("current")
_F3NCINtpHardenedResponderControl_Type = ToggleValue
_F3NCINtpHardenedResponderControl_Object = MibTableColumn
f3NCINtpHardenedResponderControl = _F3NCINtpHardenedResponderControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 2, 1, 39),
    _F3NCINtpHardenedResponderControl_Type()
)
f3NCINtpHardenedResponderControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NCINtpHardenedResponderControl.setStatus("current")
_F3NtpVirtualPortTable_Object = MibTable
f3NtpVirtualPortTable = _F3NtpVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3)
)
if mibBuilder.loadTexts:
    f3NtpVirtualPortTable.setStatus("current")
_F3NtpVirtualPortEntry_Object = MibTableRow
f3NtpVirtualPortEntry = _F3NtpVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1)
)
f3NtpVirtualPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-NTP-MIB", "f3NtpVirtualPortIndex"),
)
if mibBuilder.loadTexts:
    f3NtpVirtualPortEntry.setStatus("current")
_F3NtpVirtualPortIndex_Type = Integer32
_F3NtpVirtualPortIndex_Object = MibTableColumn
f3NtpVirtualPortIndex = _F3NtpVirtualPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1, 1),
    _F3NtpVirtualPortIndex_Type()
)
f3NtpVirtualPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpVirtualPortIndex.setStatus("current")


class _F3NtpVirtualPortAlias_Type(DisplayString):
    """Custom type f3NtpVirtualPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3NtpVirtualPortAlias_Type.__name__ = "DisplayString"
_F3NtpVirtualPortAlias_Object = MibTableColumn
f3NtpVirtualPortAlias = _F3NtpVirtualPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1, 2),
    _F3NtpVirtualPortAlias_Type()
)
f3NtpVirtualPortAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpVirtualPortAlias.setStatus("current")
_F3NtpVirtualPortAdminState_Type = AdminState
_F3NtpVirtualPortAdminState_Object = MibTableColumn
f3NtpVirtualPortAdminState = _F3NtpVirtualPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1, 3),
    _F3NtpVirtualPortAdminState_Type()
)
f3NtpVirtualPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpVirtualPortAdminState.setStatus("current")
_F3NtpVirtualPortOperationalState_Type = OperationalState
_F3NtpVirtualPortOperationalState_Object = MibTableColumn
f3NtpVirtualPortOperationalState = _F3NtpVirtualPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1, 4),
    _F3NtpVirtualPortOperationalState_Type()
)
f3NtpVirtualPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpVirtualPortOperationalState.setStatus("current")
_F3NtpVirtualPortNtpFlowPoint_Type = VariablePointer
_F3NtpVirtualPortNtpFlowPoint_Object = MibTableColumn
f3NtpVirtualPortNtpFlowPoint = _F3NtpVirtualPortNtpFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1, 5),
    _F3NtpVirtualPortNtpFlowPoint_Type()
)
f3NtpVirtualPortNtpFlowPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpVirtualPortNtpFlowPoint.setStatus("current")
_F3NtpVirtualPortStorageType_Type = StorageType
_F3NtpVirtualPortStorageType_Object = MibTableColumn
f3NtpVirtualPortStorageType = _F3NtpVirtualPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1, 6),
    _F3NtpVirtualPortStorageType_Type()
)
f3NtpVirtualPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpVirtualPortStorageType.setStatus("current")
_F3NtpVirtualPortRowStatus_Type = RowStatus
_F3NtpVirtualPortRowStatus_Object = MibTableColumn
f3NtpVirtualPortRowStatus = _F3NtpVirtualPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 3, 1, 7),
    _F3NtpVirtualPortRowStatus_Type()
)
f3NtpVirtualPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpVirtualPortRowStatus.setStatus("current")
_F3NtpRemoteClientTable_Object = MibTable
f3NtpRemoteClientTable = _F3NtpRemoteClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4)
)
if mibBuilder.loadTexts:
    f3NtpRemoteClientTable.setStatus("current")
_F3NtpRemoteClientEntry_Object = MibTableRow
f3NtpRemoteClientEntry = _F3NtpRemoteClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1)
)
f3NtpRemoteClientEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-NTP-MIB", "f3NtpRemoteClientIndex"),
)
if mibBuilder.loadTexts:
    f3NtpRemoteClientEntry.setStatus("current")
_F3NtpRemoteClientIndex_Type = Integer32
_F3NtpRemoteClientIndex_Object = MibTableColumn
f3NtpRemoteClientIndex = _F3NtpRemoteClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 1),
    _F3NtpRemoteClientIndex_Type()
)
f3NtpRemoteClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpRemoteClientIndex.setStatus("current")
_F3NtpRemoteClientIpV4Address_Type = IpAddress
_F3NtpRemoteClientIpV4Address_Object = MibTableColumn
f3NtpRemoteClientIpV4Address = _F3NtpRemoteClientIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 2),
    _F3NtpRemoteClientIpV4Address_Type()
)
f3NtpRemoteClientIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteClientIpV4Address.setStatus("current")
_F3NtpRemoteClientRxPackets_Type = PerfCounter64
_F3NtpRemoteClientRxPackets_Object = MibTableColumn
f3NtpRemoteClientRxPackets = _F3NtpRemoteClientRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 3),
    _F3NtpRemoteClientRxPackets_Type()
)
f3NtpRemoteClientRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteClientRxPackets.setStatus("current")
_F3NtpRemoteClientAvgPollInterval_Type = PerfCounter64
_F3NtpRemoteClientAvgPollInterval_Object = MibTableColumn
f3NtpRemoteClientAvgPollInterval = _F3NtpRemoteClientAvgPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 4),
    _F3NtpRemoteClientAvgPollInterval_Type()
)
f3NtpRemoteClientAvgPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteClientAvgPollInterval.setStatus("current")
_F3NtpRemoteClientLastPollInterval_Type = PerfCounter64
_F3NtpRemoteClientLastPollInterval_Object = MibTableColumn
f3NtpRemoteClientLastPollInterval = _F3NtpRemoteClientLastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 5),
    _F3NtpRemoteClientLastPollInterval_Type()
)
f3NtpRemoteClientLastPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteClientLastPollInterval.setStatus("current")
_F3NtpRemoteClientNtpMode_Type = Integer32
_F3NtpRemoteClientNtpMode_Object = MibTableColumn
f3NtpRemoteClientNtpMode = _F3NtpRemoteClientNtpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 6),
    _F3NtpRemoteClientNtpMode_Type()
)
f3NtpRemoteClientNtpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteClientNtpMode.setStatus("current")
_F3NtpRemoteClientNtpVersion_Type = Integer32
_F3NtpRemoteClientNtpVersion_Object = MibTableColumn
f3NtpRemoteClientNtpVersion = _F3NtpRemoteClientNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 7),
    _F3NtpRemoteClientNtpVersion_Type()
)
f3NtpRemoteClientNtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteClientNtpVersion.setStatus("current")
_F3NtpRemoteClientStorageType_Type = StorageType
_F3NtpRemoteClientStorageType_Object = MibTableColumn
f3NtpRemoteClientStorageType = _F3NtpRemoteClientStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 8),
    _F3NtpRemoteClientStorageType_Type()
)
f3NtpRemoteClientStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpRemoteClientStorageType.setStatus("current")
_F3NtpRemoteClientRowStatus_Type = RowStatus
_F3NtpRemoteClientRowStatus_Object = MibTableColumn
f3NtpRemoteClientRowStatus = _F3NtpRemoteClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 4, 1, 9),
    _F3NtpRemoteClientRowStatus_Type()
)
f3NtpRemoteClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpRemoteClientRowStatus.setStatus("current")
_F3NtpAccPortFlowPointTable_Object = MibTable
f3NtpAccPortFlowPointTable = _F3NtpAccPortFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5)
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointTable.setStatus("current")
_F3NtpAccPortFlowPointEntry_Object = MibTableRow
f3NtpAccPortFlowPointEntry = _F3NtpAccPortFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1)
)
f3NtpAccPortFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointEntry.setStatus("current")
_F3NtpAccPortFlowPointIndex_Type = Integer32
_F3NtpAccPortFlowPointIndex_Object = MibTableColumn
f3NtpAccPortFlowPointIndex = _F3NtpAccPortFlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 1),
    _F3NtpAccPortFlowPointIndex_Type()
)
f3NtpAccPortFlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointIndex.setStatus("current")


class _F3NtpAccPortFlowPointAlias_Type(DisplayString):
    """Custom type f3NtpAccPortFlowPointAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3NtpAccPortFlowPointAlias_Type.__name__ = "DisplayString"
_F3NtpAccPortFlowPointAlias_Object = MibTableColumn
f3NtpAccPortFlowPointAlias = _F3NtpAccPortFlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 2),
    _F3NtpAccPortFlowPointAlias_Type()
)
f3NtpAccPortFlowPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointAlias.setStatus("current")
_F3NtpAccPortFlowPointAdminState_Type = AdminState
_F3NtpAccPortFlowPointAdminState_Object = MibTableColumn
f3NtpAccPortFlowPointAdminState = _F3NtpAccPortFlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 3),
    _F3NtpAccPortFlowPointAdminState_Type()
)
f3NtpAccPortFlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointAdminState.setStatus("current")
_F3NtpAccPortFlowPointOperationalState_Type = OperationalState
_F3NtpAccPortFlowPointOperationalState_Object = MibTableColumn
f3NtpAccPortFlowPointOperationalState = _F3NtpAccPortFlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 4),
    _F3NtpAccPortFlowPointOperationalState_Type()
)
f3NtpAccPortFlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointOperationalState.setStatus("current")
_F3NtpAccPortFlowPointType_Type = NtpFlowPointType
_F3NtpAccPortFlowPointType_Object = MibTableColumn
f3NtpAccPortFlowPointType = _F3NtpAccPortFlowPointType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 5),
    _F3NtpAccPortFlowPointType_Type()
)
f3NtpAccPortFlowPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointType.setStatus("current")
_F3NtpAccPortFlowPointOuterVlanEtherType_Type = Integer32
_F3NtpAccPortFlowPointOuterVlanEtherType_Object = MibTableColumn
f3NtpAccPortFlowPointOuterVlanEtherType = _F3NtpAccPortFlowPointOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 6),
    _F3NtpAccPortFlowPointOuterVlanEtherType_Type()
)
f3NtpAccPortFlowPointOuterVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointOuterVlanEtherType.setStatus("current")
_F3NtpAccPortFlowPointOuterVlanMemberList_Type = DisplayString
_F3NtpAccPortFlowPointOuterVlanMemberList_Object = MibTableColumn
f3NtpAccPortFlowPointOuterVlanMemberList = _F3NtpAccPortFlowPointOuterVlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 7),
    _F3NtpAccPortFlowPointOuterVlanMemberList_Type()
)
f3NtpAccPortFlowPointOuterVlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointOuterVlanMemberList.setStatus("current")
_F3NtpAccPortFlowPointOuterUntaggedEnabled_Type = TruthValue
_F3NtpAccPortFlowPointOuterUntaggedEnabled_Object = MibTableColumn
f3NtpAccPortFlowPointOuterUntaggedEnabled = _F3NtpAccPortFlowPointOuterUntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 8),
    _F3NtpAccPortFlowPointOuterUntaggedEnabled_Type()
)
f3NtpAccPortFlowPointOuterUntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointOuterUntaggedEnabled.setStatus("current")
_F3NtpAccPortFlowPointInner1VlanEtherType_Type = Integer32
_F3NtpAccPortFlowPointInner1VlanEtherType_Object = MibTableColumn
f3NtpAccPortFlowPointInner1VlanEtherType = _F3NtpAccPortFlowPointInner1VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 9),
    _F3NtpAccPortFlowPointInner1VlanEtherType_Type()
)
f3NtpAccPortFlowPointInner1VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointInner1VlanEtherType.setStatus("current")
_F3NtpAccPortFlowPointInner1VlanMemberList_Type = DisplayString
_F3NtpAccPortFlowPointInner1VlanMemberList_Object = MibTableColumn
f3NtpAccPortFlowPointInner1VlanMemberList = _F3NtpAccPortFlowPointInner1VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 10),
    _F3NtpAccPortFlowPointInner1VlanMemberList_Type()
)
f3NtpAccPortFlowPointInner1VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointInner1VlanMemberList.setStatus("current")
_F3NtpAccPortFlowPointInner1UntaggedEnabled_Type = TruthValue
_F3NtpAccPortFlowPointInner1UntaggedEnabled_Object = MibTableColumn
f3NtpAccPortFlowPointInner1UntaggedEnabled = _F3NtpAccPortFlowPointInner1UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 11),
    _F3NtpAccPortFlowPointInner1UntaggedEnabled_Type()
)
f3NtpAccPortFlowPointInner1UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointInner1UntaggedEnabled.setStatus("current")
_F3NtpAccPortFlowPointInner2VlanEtherType_Type = Integer32
_F3NtpAccPortFlowPointInner2VlanEtherType_Object = MibTableColumn
f3NtpAccPortFlowPointInner2VlanEtherType = _F3NtpAccPortFlowPointInner2VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 12),
    _F3NtpAccPortFlowPointInner2VlanEtherType_Type()
)
f3NtpAccPortFlowPointInner2VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointInner2VlanEtherType.setStatus("current")
_F3NtpAccPortFlowPointInner2VlanMemberList_Type = DisplayString
_F3NtpAccPortFlowPointInner2VlanMemberList_Object = MibTableColumn
f3NtpAccPortFlowPointInner2VlanMemberList = _F3NtpAccPortFlowPointInner2VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 13),
    _F3NtpAccPortFlowPointInner2VlanMemberList_Type()
)
f3NtpAccPortFlowPointInner2VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointInner2VlanMemberList.setStatus("current")
_F3NtpAccPortFlowPointInner2UntaggedEnabled_Type = TruthValue
_F3NtpAccPortFlowPointInner2UntaggedEnabled_Object = MibTableColumn
f3NtpAccPortFlowPointInner2UntaggedEnabled = _F3NtpAccPortFlowPointInner2UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 14),
    _F3NtpAccPortFlowPointInner2UntaggedEnabled_Type()
)
f3NtpAccPortFlowPointInner2UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointInner2UntaggedEnabled.setStatus("current")


class _F3NtpAccPortFlowPointCOS_Type(Integer32):
    """Custom type f3NtpAccPortFlowPointCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3NtpAccPortFlowPointCOS_Type.__name__ = "Integer32"
_F3NtpAccPortFlowPointCOS_Object = MibTableColumn
f3NtpAccPortFlowPointCOS = _F3NtpAccPortFlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 15),
    _F3NtpAccPortFlowPointCOS_Type()
)
f3NtpAccPortFlowPointCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointCOS.setStatus("current")
_F3NtpAccPortFlowPointCIRLo_Type = Unsigned32
_F3NtpAccPortFlowPointCIRLo_Object = MibTableColumn
f3NtpAccPortFlowPointCIRLo = _F3NtpAccPortFlowPointCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 16),
    _F3NtpAccPortFlowPointCIRLo_Type()
)
f3NtpAccPortFlowPointCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointCIRLo.setStatus("current")
_F3NtpAccPortFlowPointCIRHi_Type = Unsigned32
_F3NtpAccPortFlowPointCIRHi_Object = MibTableColumn
f3NtpAccPortFlowPointCIRHi = _F3NtpAccPortFlowPointCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 17),
    _F3NtpAccPortFlowPointCIRHi_Type()
)
f3NtpAccPortFlowPointCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointCIRHi.setStatus("current")
_F3NtpAccPortFlowPointEIRLo_Type = Unsigned32
_F3NtpAccPortFlowPointEIRLo_Object = MibTableColumn
f3NtpAccPortFlowPointEIRLo = _F3NtpAccPortFlowPointEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 18),
    _F3NtpAccPortFlowPointEIRLo_Type()
)
f3NtpAccPortFlowPointEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointEIRLo.setStatus("current")
_F3NtpAccPortFlowPointEIRHi_Type = Unsigned32
_F3NtpAccPortFlowPointEIRHi_Object = MibTableColumn
f3NtpAccPortFlowPointEIRHi = _F3NtpAccPortFlowPointEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 19),
    _F3NtpAccPortFlowPointEIRHi_Type()
)
f3NtpAccPortFlowPointEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointEIRHi.setStatus("current")
_F3NtpAccPortFlowPointBufferSize_Type = Unsigned32
_F3NtpAccPortFlowPointBufferSize_Object = MibTableColumn
f3NtpAccPortFlowPointBufferSize = _F3NtpAccPortFlowPointBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 20),
    _F3NtpAccPortFlowPointBufferSize_Type()
)
f3NtpAccPortFlowPointBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointBufferSize.setStatus("current")
_F3NtpAccPortFlowPointStorageType_Type = StorageType
_F3NtpAccPortFlowPointStorageType_Object = MibTableColumn
f3NtpAccPortFlowPointStorageType = _F3NtpAccPortFlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 21),
    _F3NtpAccPortFlowPointStorageType_Type()
)
f3NtpAccPortFlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStorageType.setStatus("current")
_F3NtpAccPortFlowPointRowStatus_Type = RowStatus
_F3NtpAccPortFlowPointRowStatus_Object = MibTableColumn
f3NtpAccPortFlowPointRowStatus = _F3NtpAccPortFlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 5, 1, 22),
    _F3NtpAccPortFlowPointRowStatus_Type()
)
f3NtpAccPortFlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointRowStatus.setStatus("current")
_F3NtpNetPortFlowPointTable_Object = MibTable
f3NtpNetPortFlowPointTable = _F3NtpNetPortFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6)
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointTable.setStatus("current")
_F3NtpNetPortFlowPointEntry_Object = MibTableRow
f3NtpNetPortFlowPointEntry = _F3NtpNetPortFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1)
)
f3NtpNetPortFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointEntry.setStatus("current")
_F3NtpNetPortFlowPointIndex_Type = Integer32
_F3NtpNetPortFlowPointIndex_Object = MibTableColumn
f3NtpNetPortFlowPointIndex = _F3NtpNetPortFlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 1),
    _F3NtpNetPortFlowPointIndex_Type()
)
f3NtpNetPortFlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointIndex.setStatus("current")


class _F3NtpNetPortFlowPointAlias_Type(DisplayString):
    """Custom type f3NtpNetPortFlowPointAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3NtpNetPortFlowPointAlias_Type.__name__ = "DisplayString"
_F3NtpNetPortFlowPointAlias_Object = MibTableColumn
f3NtpNetPortFlowPointAlias = _F3NtpNetPortFlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 2),
    _F3NtpNetPortFlowPointAlias_Type()
)
f3NtpNetPortFlowPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointAlias.setStatus("current")
_F3NtpNetPortFlowPointAdminState_Type = AdminState
_F3NtpNetPortFlowPointAdminState_Object = MibTableColumn
f3NtpNetPortFlowPointAdminState = _F3NtpNetPortFlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 3),
    _F3NtpNetPortFlowPointAdminState_Type()
)
f3NtpNetPortFlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointAdminState.setStatus("current")
_F3NtpNetPortFlowPointOperationalState_Type = OperationalState
_F3NtpNetPortFlowPointOperationalState_Object = MibTableColumn
f3NtpNetPortFlowPointOperationalState = _F3NtpNetPortFlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 4),
    _F3NtpNetPortFlowPointOperationalState_Type()
)
f3NtpNetPortFlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointOperationalState.setStatus("current")
_F3NtpNetPortFlowPointType_Type = NtpFlowPointType
_F3NtpNetPortFlowPointType_Object = MibTableColumn
f3NtpNetPortFlowPointType = _F3NtpNetPortFlowPointType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 5),
    _F3NtpNetPortFlowPointType_Type()
)
f3NtpNetPortFlowPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointType.setStatus("current")
_F3NtpNetPortFlowPointOuterVlanEtherType_Type = Integer32
_F3NtpNetPortFlowPointOuterVlanEtherType_Object = MibTableColumn
f3NtpNetPortFlowPointOuterVlanEtherType = _F3NtpNetPortFlowPointOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 6),
    _F3NtpNetPortFlowPointOuterVlanEtherType_Type()
)
f3NtpNetPortFlowPointOuterVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointOuterVlanEtherType.setStatus("current")
_F3NtpNetPortFlowPointOuterVlanMemberList_Type = DisplayString
_F3NtpNetPortFlowPointOuterVlanMemberList_Object = MibTableColumn
f3NtpNetPortFlowPointOuterVlanMemberList = _F3NtpNetPortFlowPointOuterVlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 7),
    _F3NtpNetPortFlowPointOuterVlanMemberList_Type()
)
f3NtpNetPortFlowPointOuterVlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointOuterVlanMemberList.setStatus("current")
_F3NtpNetPortFlowPointOuterUntaggedEnabled_Type = TruthValue
_F3NtpNetPortFlowPointOuterUntaggedEnabled_Object = MibTableColumn
f3NtpNetPortFlowPointOuterUntaggedEnabled = _F3NtpNetPortFlowPointOuterUntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 8),
    _F3NtpNetPortFlowPointOuterUntaggedEnabled_Type()
)
f3NtpNetPortFlowPointOuterUntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointOuterUntaggedEnabled.setStatus("current")
_F3NtpNetPortFlowPointInner1VlanEtherType_Type = Integer32
_F3NtpNetPortFlowPointInner1VlanEtherType_Object = MibTableColumn
f3NtpNetPortFlowPointInner1VlanEtherType = _F3NtpNetPortFlowPointInner1VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 9),
    _F3NtpNetPortFlowPointInner1VlanEtherType_Type()
)
f3NtpNetPortFlowPointInner1VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointInner1VlanEtherType.setStatus("current")
_F3NtpNetPortFlowPointInner1VlanMemberList_Type = DisplayString
_F3NtpNetPortFlowPointInner1VlanMemberList_Object = MibTableColumn
f3NtpNetPortFlowPointInner1VlanMemberList = _F3NtpNetPortFlowPointInner1VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 10),
    _F3NtpNetPortFlowPointInner1VlanMemberList_Type()
)
f3NtpNetPortFlowPointInner1VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointInner1VlanMemberList.setStatus("current")
_F3NtpNetPortFlowPointInner1UntaggedEnabled_Type = TruthValue
_F3NtpNetPortFlowPointInner1UntaggedEnabled_Object = MibTableColumn
f3NtpNetPortFlowPointInner1UntaggedEnabled = _F3NtpNetPortFlowPointInner1UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 11),
    _F3NtpNetPortFlowPointInner1UntaggedEnabled_Type()
)
f3NtpNetPortFlowPointInner1UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointInner1UntaggedEnabled.setStatus("current")
_F3NtpNetPortFlowPointInner2VlanEtherType_Type = Integer32
_F3NtpNetPortFlowPointInner2VlanEtherType_Object = MibTableColumn
f3NtpNetPortFlowPointInner2VlanEtherType = _F3NtpNetPortFlowPointInner2VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 12),
    _F3NtpNetPortFlowPointInner2VlanEtherType_Type()
)
f3NtpNetPortFlowPointInner2VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointInner2VlanEtherType.setStatus("current")
_F3NtpNetPortFlowPointInner2VlanMemberList_Type = DisplayString
_F3NtpNetPortFlowPointInner2VlanMemberList_Object = MibTableColumn
f3NtpNetPortFlowPointInner2VlanMemberList = _F3NtpNetPortFlowPointInner2VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 13),
    _F3NtpNetPortFlowPointInner2VlanMemberList_Type()
)
f3NtpNetPortFlowPointInner2VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointInner2VlanMemberList.setStatus("current")
_F3NtpNetPortFlowPointInner2UntaggedEnabled_Type = TruthValue
_F3NtpNetPortFlowPointInner2UntaggedEnabled_Object = MibTableColumn
f3NtpNetPortFlowPointInner2UntaggedEnabled = _F3NtpNetPortFlowPointInner2UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 14),
    _F3NtpNetPortFlowPointInner2UntaggedEnabled_Type()
)
f3NtpNetPortFlowPointInner2UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointInner2UntaggedEnabled.setStatus("current")


class _F3NtpNetPortFlowPointCOS_Type(Integer32):
    """Custom type f3NtpNetPortFlowPointCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3NtpNetPortFlowPointCOS_Type.__name__ = "Integer32"
_F3NtpNetPortFlowPointCOS_Object = MibTableColumn
f3NtpNetPortFlowPointCOS = _F3NtpNetPortFlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 15),
    _F3NtpNetPortFlowPointCOS_Type()
)
f3NtpNetPortFlowPointCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointCOS.setStatus("current")
_F3NtpNetPortFlowPointCIRLo_Type = Unsigned32
_F3NtpNetPortFlowPointCIRLo_Object = MibTableColumn
f3NtpNetPortFlowPointCIRLo = _F3NtpNetPortFlowPointCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 16),
    _F3NtpNetPortFlowPointCIRLo_Type()
)
f3NtpNetPortFlowPointCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointCIRLo.setStatus("current")
_F3NtpNetPortFlowPointCIRHi_Type = Unsigned32
_F3NtpNetPortFlowPointCIRHi_Object = MibTableColumn
f3NtpNetPortFlowPointCIRHi = _F3NtpNetPortFlowPointCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 17),
    _F3NtpNetPortFlowPointCIRHi_Type()
)
f3NtpNetPortFlowPointCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointCIRHi.setStatus("current")
_F3NtpNetPortFlowPointEIRLo_Type = Unsigned32
_F3NtpNetPortFlowPointEIRLo_Object = MibTableColumn
f3NtpNetPortFlowPointEIRLo = _F3NtpNetPortFlowPointEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 18),
    _F3NtpNetPortFlowPointEIRLo_Type()
)
f3NtpNetPortFlowPointEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointEIRLo.setStatus("current")
_F3NtpNetPortFlowPointEIRHi_Type = Unsigned32
_F3NtpNetPortFlowPointEIRHi_Object = MibTableColumn
f3NtpNetPortFlowPointEIRHi = _F3NtpNetPortFlowPointEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 19),
    _F3NtpNetPortFlowPointEIRHi_Type()
)
f3NtpNetPortFlowPointEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointEIRHi.setStatus("current")
_F3NtpNetPortFlowPointBufferSize_Type = Unsigned32
_F3NtpNetPortFlowPointBufferSize_Object = MibTableColumn
f3NtpNetPortFlowPointBufferSize = _F3NtpNetPortFlowPointBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 20),
    _F3NtpNetPortFlowPointBufferSize_Type()
)
f3NtpNetPortFlowPointBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointBufferSize.setStatus("current")
_F3NtpNetPortFlowPointStorageType_Type = StorageType
_F3NtpNetPortFlowPointStorageType_Object = MibTableColumn
f3NtpNetPortFlowPointStorageType = _F3NtpNetPortFlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 21),
    _F3NtpNetPortFlowPointStorageType_Type()
)
f3NtpNetPortFlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStorageType.setStatus("current")
_F3NtpNetPortFlowPointRowStatus_Type = RowStatus
_F3NtpNetPortFlowPointRowStatus_Object = MibTableColumn
f3NtpNetPortFlowPointRowStatus = _F3NtpNetPortFlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 6, 1, 22),
    _F3NtpNetPortFlowPointRowStatus_Type()
)
f3NtpNetPortFlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointRowStatus.setStatus("current")
_F3NtpTrackedClientTable_Object = MibTable
f3NtpTrackedClientTable = _F3NtpTrackedClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7)
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientTable.setStatus("current")
_F3NtpTrackedClientEntry_Object = MibTableRow
f3NtpTrackedClientEntry = _F3NtpTrackedClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7, 1)
)
f3NtpTrackedClientEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientIndex"),
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientEntry.setStatus("current")
_F3NtpTrackedClientIndex_Type = Integer32
_F3NtpTrackedClientIndex_Object = MibTableColumn
f3NtpTrackedClientIndex = _F3NtpTrackedClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7, 1, 1),
    _F3NtpTrackedClientIndex_Type()
)
f3NtpTrackedClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpTrackedClientIndex.setStatus("current")


class _F3NtpTrackedClientAlias_Type(DisplayString):
    """Custom type f3NtpTrackedClientAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3NtpTrackedClientAlias_Type.__name__ = "DisplayString"
_F3NtpTrackedClientAlias_Object = MibTableColumn
f3NtpTrackedClientAlias = _F3NtpTrackedClientAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7, 1, 2),
    _F3NtpTrackedClientAlias_Type()
)
f3NtpTrackedClientAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpTrackedClientAlias.setStatus("current")
_F3NtpTrackedClientIpV4Address_Type = IpAddress
_F3NtpTrackedClientIpV4Address_Object = MibTableColumn
f3NtpTrackedClientIpV4Address = _F3NtpTrackedClientIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7, 1, 3),
    _F3NtpTrackedClientIpV4Address_Type()
)
f3NtpTrackedClientIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpTrackedClientIpV4Address.setStatus("current")
_F3NtpTrackedClientIpV6Address_Type = Ipv6Address
_F3NtpTrackedClientIpV6Address_Object = MibTableColumn
f3NtpTrackedClientIpV6Address = _F3NtpTrackedClientIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7, 1, 4),
    _F3NtpTrackedClientIpV6Address_Type()
)
f3NtpTrackedClientIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpTrackedClientIpV6Address.setStatus("current")
_F3NtpTrackedClientStorageType_Type = StorageType
_F3NtpTrackedClientStorageType_Object = MibTableColumn
f3NtpTrackedClientStorageType = _F3NtpTrackedClientStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7, 1, 5),
    _F3NtpTrackedClientStorageType_Type()
)
f3NtpTrackedClientStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStorageType.setStatus("current")
_F3NtpTrackedClientRowStatus_Type = RowStatus
_F3NtpTrackedClientRowStatus_Object = MibTableColumn
f3NtpTrackedClientRowStatus = _F3NtpTrackedClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 7, 1, 6),
    _F3NtpTrackedClientRowStatus_Type()
)
f3NtpTrackedClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpTrackedClientRowStatus.setStatus("current")
_F3NtpRemoteServerTable_Object = MibTable
f3NtpRemoteServerTable = _F3NtpRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8)
)
if mibBuilder.loadTexts:
    f3NtpRemoteServerTable.setStatus("current")
_F3NtpRemoteServerEntry_Object = MibTableRow
f3NtpRemoteServerEntry = _F3NtpRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1)
)
f3NtpRemoteServerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NtpRemoteServerIndex"),
)
if mibBuilder.loadTexts:
    f3NtpRemoteServerEntry.setStatus("current")
_F3NtpRemoteServerIndex_Type = Integer32
_F3NtpRemoteServerIndex_Object = MibTableColumn
f3NtpRemoteServerIndex = _F3NtpRemoteServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 1),
    _F3NtpRemoteServerIndex_Type()
)
f3NtpRemoteServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpRemoteServerIndex.setStatus("current")


class _F3NtpRemoteServerAlias_Type(DisplayString):
    """Custom type f3NtpRemoteServerAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3NtpRemoteServerAlias_Type.__name__ = "DisplayString"
_F3NtpRemoteServerAlias_Object = MibTableColumn
f3NtpRemoteServerAlias = _F3NtpRemoteServerAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 2),
    _F3NtpRemoteServerAlias_Type()
)
f3NtpRemoteServerAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpRemoteServerAlias.setStatus("current")
_F3NtpRemoteServerAdminState_Type = AdminState
_F3NtpRemoteServerAdminState_Object = MibTableColumn
f3NtpRemoteServerAdminState = _F3NtpRemoteServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 3),
    _F3NtpRemoteServerAdminState_Type()
)
f3NtpRemoteServerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpRemoteServerAdminState.setStatus("current")
_F3NtpRemoteServerOperationalState_Type = OperationalState
_F3NtpRemoteServerOperationalState_Object = MibTableColumn
f3NtpRemoteServerOperationalState = _F3NtpRemoteServerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 4),
    _F3NtpRemoteServerOperationalState_Type()
)
f3NtpRemoteServerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteServerOperationalState.setStatus("current")
_F3NtpRemoteServerSecondaryState_Type = SecondaryState
_F3NtpRemoteServerSecondaryState_Object = MibTableColumn
f3NtpRemoteServerSecondaryState = _F3NtpRemoteServerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 5),
    _F3NtpRemoteServerSecondaryState_Type()
)
f3NtpRemoteServerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteServerSecondaryState.setStatus("current")
_F3NtpRemoteServerServerAddress_Type = DisplayString
_F3NtpRemoteServerServerAddress_Object = MibTableColumn
f3NtpRemoteServerServerAddress = _F3NtpRemoteServerServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 6),
    _F3NtpRemoteServerServerAddress_Type()
)
f3NtpRemoteServerServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpRemoteServerServerAddress.setStatus("current")
_F3NtpRemoteServerMinPollInterval_Type = NtpPollingInterval
_F3NtpRemoteServerMinPollInterval_Object = MibTableColumn
f3NtpRemoteServerMinPollInterval = _F3NtpRemoteServerMinPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 7),
    _F3NtpRemoteServerMinPollInterval_Type()
)
f3NtpRemoteServerMinPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpRemoteServerMinPollInterval.setStatus("current")
_F3NtpRemoteServerMaxPollInterval_Type = NtpPollingInterval
_F3NtpRemoteServerMaxPollInterval_Object = MibTableColumn
f3NtpRemoteServerMaxPollInterval = _F3NtpRemoteServerMaxPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 8),
    _F3NtpRemoteServerMaxPollInterval_Type()
)
f3NtpRemoteServerMaxPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpRemoteServerMaxPollInterval.setStatus("current")
_F3NtpRemoteServerPreferred_Type = ToggleValue
_F3NtpRemoteServerPreferred_Object = MibTableColumn
f3NtpRemoteServerPreferred = _F3NtpRemoteServerPreferred_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 9),
    _F3NtpRemoteServerPreferred_Type()
)
f3NtpRemoteServerPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpRemoteServerPreferred.setStatus("current")
_F3NtpRemoteServerReach_Type = Unsigned32
_F3NtpRemoteServerReach_Object = MibTableColumn
f3NtpRemoteServerReach = _F3NtpRemoteServerReach_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 10),
    _F3NtpRemoteServerReach_Type()
)
f3NtpRemoteServerReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpRemoteServerReach.setStatus("current")
_F3NtpRemoteServerStorageType_Type = StorageType
_F3NtpRemoteServerStorageType_Object = MibTableColumn
f3NtpRemoteServerStorageType = _F3NtpRemoteServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 11),
    _F3NtpRemoteServerStorageType_Type()
)
f3NtpRemoteServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpRemoteServerStorageType.setStatus("current")
_F3NtpRemoteServerRowStatus_Type = RowStatus
_F3NtpRemoteServerRowStatus_Object = MibTableColumn
f3NtpRemoteServerRowStatus = _F3NtpRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 1, 8, 1, 12),
    _F3NtpRemoteServerRowStatus_Type()
)
f3NtpRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NtpRemoteServerRowStatus.setStatus("current")
_F3NtpConformance_ObjectIdentity = ObjectIdentity
f3NtpConformance = _F3NtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 2)
)
_F3NtpCompliances_ObjectIdentity = ObjectIdentity
f3NtpCompliances = _F3NtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 2, 1)
)
_F3NtpGroups_ObjectIdentity = ObjectIdentity
f3NtpGroups = _F3NtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 2, 2)
)
_F3NtpPerformanceObjects_ObjectIdentity = ObjectIdentity
f3NtpPerformanceObjects = _F3NtpPerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3)
)
_F3NCIStatsTable_Object = MibTable
f3NCIStatsTable = _F3NCIStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1)
)
if mibBuilder.loadTexts:
    f3NCIStatsTable.setStatus("current")
_F3NCIStatsEntry_Object = MibTableRow
f3NCIStatsEntry = _F3NCIStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1)
)
f3NCIStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NCIIndex"),
    (0, "F3-NTP-MIB", "f3NCIStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NCIStatsEntry.setStatus("current")


class _F3NCIStatsIndex_Type(Integer32):
    """Custom type f3NCIStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3NCIStatsIndex_Type.__name__ = "Integer32"
_F3NCIStatsIndex_Object = MibTableColumn
f3NCIStatsIndex = _F3NCIStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 1),
    _F3NCIStatsIndex_Type()
)
f3NCIStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NCIStatsIndex.setStatus("current")
_F3NCIStatsIntervalType_Type = CmPmIntervalType
_F3NCIStatsIntervalType_Object = MibTableColumn
f3NCIStatsIntervalType = _F3NCIStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 2),
    _F3NCIStatsIntervalType_Type()
)
f3NCIStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsIntervalType.setStatus("current")
_F3NCIStatsValid_Type = TruthValue
_F3NCIStatsValid_Object = MibTableColumn
f3NCIStatsValid = _F3NCIStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 3),
    _F3NCIStatsValid_Type()
)
f3NCIStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsValid.setStatus("current")
_F3NCIStatsAction_Type = CmPmBinAction
_F3NCIStatsAction_Object = MibTableColumn
f3NCIStatsAction = _F3NCIStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 4),
    _F3NCIStatsAction_Type()
)
f3NCIStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIStatsAction.setStatus("current")
_F3NCIStatsRequestsProcessed_Type = PerfCounter64
_F3NCIStatsRequestsProcessed_Object = MibTableColumn
f3NCIStatsRequestsProcessed = _F3NCIStatsRequestsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 5),
    _F3NCIStatsRequestsProcessed_Type()
)
f3NCIStatsRequestsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsRequestsProcessed.setStatus("current")
_F3NCIStatsResponsesError_Type = PerfCounter64
_F3NCIStatsResponsesError_Object = MibTableColumn
f3NCIStatsResponsesError = _F3NCIStatsResponsesError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 6),
    _F3NCIStatsResponsesError_Type()
)
f3NCIStatsResponsesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsResponsesError.setStatus("current")
_F3NCIStatsAuthFailures_Type = PerfCounter64
_F3NCIStatsAuthFailures_Object = MibTableColumn
f3NCIStatsAuthFailures = _F3NCIStatsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 7),
    _F3NCIStatsAuthFailures_Type()
)
f3NCIStatsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsAuthFailures.setStatus("current")
_F3NCIStatsReqsDiscarded_Type = PerfCounter64
_F3NCIStatsReqsDiscarded_Object = MibTableColumn
f3NCIStatsReqsDiscarded = _F3NCIStatsReqsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 8),
    _F3NCIStatsReqsDiscarded_Type()
)
f3NCIStatsReqsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsReqsDiscarded.setStatus("current")
_F3NCIStatsAvgTPS_Type = PerfCounter64
_F3NCIStatsAvgTPS_Object = MibTableColumn
f3NCIStatsAvgTPS = _F3NCIStatsAvgTPS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 9),
    _F3NCIStatsAvgTPS_Type()
)
f3NCIStatsAvgTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsAvgTPS.setStatus("current")
_F3NCIStatsMaxTPS_Type = PerfCounter64
_F3NCIStatsMaxTPS_Object = MibTableColumn
f3NCIStatsMaxTPS = _F3NCIStatsMaxTPS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 1, 1, 10),
    _F3NCIStatsMaxTPS_Type()
)
f3NCIStatsMaxTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIStatsMaxTPS.setStatus("current")
_F3NCIHistoryTable_Object = MibTable
f3NCIHistoryTable = _F3NCIHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2)
)
if mibBuilder.loadTexts:
    f3NCIHistoryTable.setStatus("current")
_F3NCIHistoryEntry_Object = MibTableRow
f3NCIHistoryEntry = _F3NCIHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1)
)
f3NCIHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NCIIndex"),
    (0, "F3-NTP-MIB", "f3NCIStatsIndex"),
    (0, "F3-NTP-MIB", "f3NCIHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NCIHistoryEntry.setStatus("current")


class _F3NCIHistoryIndex_Type(Integer32):
    """Custom type f3NCIHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3NCIHistoryIndex_Type.__name__ = "Integer32"
_F3NCIHistoryIndex_Object = MibTableColumn
f3NCIHistoryIndex = _F3NCIHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 1),
    _F3NCIHistoryIndex_Type()
)
f3NCIHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NCIHistoryIndex.setStatus("current")
_F3NCIHistoryTime_Type = DateAndTime
_F3NCIHistoryTime_Object = MibTableColumn
f3NCIHistoryTime = _F3NCIHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 2),
    _F3NCIHistoryTime_Type()
)
f3NCIHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryTime.setStatus("current")
_F3NCIHistoryValid_Type = TruthValue
_F3NCIHistoryValid_Object = MibTableColumn
f3NCIHistoryValid = _F3NCIHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 3),
    _F3NCIHistoryValid_Type()
)
f3NCIHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryValid.setStatus("current")
_F3NCIHistoryAction_Type = CmPmBinAction
_F3NCIHistoryAction_Object = MibTableColumn
f3NCIHistoryAction = _F3NCIHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 4),
    _F3NCIHistoryAction_Type()
)
f3NCIHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIHistoryAction.setStatus("current")
_F3NCIHistoryRequestsProcessed_Type = PerfCounter64
_F3NCIHistoryRequestsProcessed_Object = MibTableColumn
f3NCIHistoryRequestsProcessed = _F3NCIHistoryRequestsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 5),
    _F3NCIHistoryRequestsProcessed_Type()
)
f3NCIHistoryRequestsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryRequestsProcessed.setStatus("current")
_F3NCIHistoryResponsesError_Type = PerfCounter64
_F3NCIHistoryResponsesError_Object = MibTableColumn
f3NCIHistoryResponsesError = _F3NCIHistoryResponsesError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 6),
    _F3NCIHistoryResponsesError_Type()
)
f3NCIHistoryResponsesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryResponsesError.setStatus("current")
_F3NCIHistoryAuthFailures_Type = PerfCounter64
_F3NCIHistoryAuthFailures_Object = MibTableColumn
f3NCIHistoryAuthFailures = _F3NCIHistoryAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 7),
    _F3NCIHistoryAuthFailures_Type()
)
f3NCIHistoryAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryAuthFailures.setStatus("current")
_F3NCIHistoryReqsDiscarded_Type = PerfCounter64
_F3NCIHistoryReqsDiscarded_Object = MibTableColumn
f3NCIHistoryReqsDiscarded = _F3NCIHistoryReqsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 8),
    _F3NCIHistoryReqsDiscarded_Type()
)
f3NCIHistoryReqsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryReqsDiscarded.setStatus("current")
_F3NCIHistoryAvgTPS_Type = PerfCounter64
_F3NCIHistoryAvgTPS_Object = MibTableColumn
f3NCIHistoryAvgTPS = _F3NCIHistoryAvgTPS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 9),
    _F3NCIHistoryAvgTPS_Type()
)
f3NCIHistoryAvgTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryAvgTPS.setStatus("current")
_F3NCIHistoryMaxTPS_Type = PerfCounter64
_F3NCIHistoryMaxTPS_Object = MibTableColumn
f3NCIHistoryMaxTPS = _F3NCIHistoryMaxTPS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 2, 1, 10),
    _F3NCIHistoryMaxTPS_Type()
)
f3NCIHistoryMaxTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIHistoryMaxTPS.setStatus("current")
_F3NCIThresholdTable_Object = MibTable
f3NCIThresholdTable = _F3NCIThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3)
)
if mibBuilder.loadTexts:
    f3NCIThresholdTable.setStatus("current")
_F3NCIThresholdEntry_Object = MibTableRow
f3NCIThresholdEntry = _F3NCIThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3, 1)
)
f3NCIThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NCIIndex"),
    (0, "F3-NTP-MIB", "f3NCIStatsIndex"),
    (0, "F3-NTP-MIB", "f3NCIThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NCIThresholdEntry.setStatus("current")


class _F3NCIThresholdIndex_Type(Integer32):
    """Custom type f3NCIThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NCIThresholdIndex_Type.__name__ = "Integer32"
_F3NCIThresholdIndex_Object = MibTableColumn
f3NCIThresholdIndex = _F3NCIThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3, 1, 1),
    _F3NCIThresholdIndex_Type()
)
f3NCIThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NCIThresholdIndex.setStatus("current")
_F3NCIThresholdInterval_Type = CmPmIntervalType
_F3NCIThresholdInterval_Object = MibTableColumn
f3NCIThresholdInterval = _F3NCIThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3, 1, 2),
    _F3NCIThresholdInterval_Type()
)
f3NCIThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIThresholdInterval.setStatus("current")
_F3NCIThresholdVariable_Type = VariablePointer
_F3NCIThresholdVariable_Object = MibTableColumn
f3NCIThresholdVariable = _F3NCIThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3, 1, 3),
    _F3NCIThresholdVariable_Type()
)
f3NCIThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIThresholdVariable.setStatus("current")
_F3NCIThresholdValueLo_Type = Unsigned32
_F3NCIThresholdValueLo_Object = MibTableColumn
f3NCIThresholdValueLo = _F3NCIThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3, 1, 4),
    _F3NCIThresholdValueLo_Type()
)
f3NCIThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIThresholdValueLo.setStatus("current")
_F3NCIThresholdValueHi_Type = Unsigned32
_F3NCIThresholdValueHi_Object = MibTableColumn
f3NCIThresholdValueHi = _F3NCIThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3, 1, 5),
    _F3NCIThresholdValueHi_Type()
)
f3NCIThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NCIThresholdValueHi.setStatus("current")
_F3NCIThresholdMonValue_Type = PerfCounter64
_F3NCIThresholdMonValue_Object = MibTableColumn
f3NCIThresholdMonValue = _F3NCIThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 3, 1, 6),
    _F3NCIThresholdMonValue_Type()
)
f3NCIThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NCIThresholdMonValue.setStatus("current")
_F3NtpAccPortFlowPointStatsTable_Object = MibTable
f3NtpAccPortFlowPointStatsTable = _F3NtpAccPortFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4)
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsTable.setStatus("current")
_F3NtpAccPortFlowPointStatsEntry_Object = MibTableRow
f3NtpAccPortFlowPointStatsEntry = _F3NtpAccPortFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1)
)
f3NtpAccPortFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsEntry.setStatus("current")


class _F3NtpAccPortFlowPointStatsIndex_Type(Integer32):
    """Custom type f3NtpAccPortFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3NtpAccPortFlowPointStatsIndex_Type.__name__ = "Integer32"
_F3NtpAccPortFlowPointStatsIndex_Object = MibTableColumn
f3NtpAccPortFlowPointStatsIndex = _F3NtpAccPortFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1, 1),
    _F3NtpAccPortFlowPointStatsIndex_Type()
)
f3NtpAccPortFlowPointStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsIndex.setStatus("current")
_F3NtpAccPortFlowPointStatsIntervalType_Type = CmPmIntervalType
_F3NtpAccPortFlowPointStatsIntervalType_Object = MibTableColumn
f3NtpAccPortFlowPointStatsIntervalType = _F3NtpAccPortFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1, 2),
    _F3NtpAccPortFlowPointStatsIntervalType_Type()
)
f3NtpAccPortFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsIntervalType.setStatus("current")
_F3NtpAccPortFlowPointStatsValid_Type = TruthValue
_F3NtpAccPortFlowPointStatsValid_Object = MibTableColumn
f3NtpAccPortFlowPointStatsValid = _F3NtpAccPortFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1, 3),
    _F3NtpAccPortFlowPointStatsValid_Type()
)
f3NtpAccPortFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsValid.setStatus("current")
_F3NtpAccPortFlowPointStatsAction_Type = CmPmBinAction
_F3NtpAccPortFlowPointStatsAction_Object = MibTableColumn
f3NtpAccPortFlowPointStatsAction = _F3NtpAccPortFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1, 4),
    _F3NtpAccPortFlowPointStatsAction_Type()
)
f3NtpAccPortFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsAction.setStatus("current")
_F3NtpAccPortFlowPointStatsRequestsDropped_Type = PerfCounter64
_F3NtpAccPortFlowPointStatsRequestsDropped_Object = MibTableColumn
f3NtpAccPortFlowPointStatsRequestsDropped = _F3NtpAccPortFlowPointStatsRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1, 5),
    _F3NtpAccPortFlowPointStatsRequestsDropped_Type()
)
f3NtpAccPortFlowPointStatsRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsRequestsDropped.setStatus("current")
_F3NtpAccPortFlowPointStatsRequestsReceived_Type = PerfCounter64
_F3NtpAccPortFlowPointStatsRequestsReceived_Object = MibTableColumn
f3NtpAccPortFlowPointStatsRequestsReceived = _F3NtpAccPortFlowPointStatsRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1, 6),
    _F3NtpAccPortFlowPointStatsRequestsReceived_Type()
)
f3NtpAccPortFlowPointStatsRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsRequestsReceived.setStatus("current")
_F3NtpAccPortFlowPointStatsResponsesTransmitted_Type = PerfCounter64
_F3NtpAccPortFlowPointStatsResponsesTransmitted_Object = MibTableColumn
f3NtpAccPortFlowPointStatsResponsesTransmitted = _F3NtpAccPortFlowPointStatsResponsesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 4, 1, 7),
    _F3NtpAccPortFlowPointStatsResponsesTransmitted_Type()
)
f3NtpAccPortFlowPointStatsResponsesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointStatsResponsesTransmitted.setStatus("current")
_F3NtpAccPortFlowPointHistoryTable_Object = MibTable
f3NtpAccPortFlowPointHistoryTable = _F3NtpAccPortFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5)
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryTable.setStatus("current")
_F3NtpAccPortFlowPointHistoryEntry_Object = MibTableRow
f3NtpAccPortFlowPointHistoryEntry = _F3NtpAccPortFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1)
)
f3NtpAccPortFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointStatsIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryEntry.setStatus("current")


class _F3NtpAccPortFlowPointHistoryIndex_Type(Integer32):
    """Custom type f3NtpAccPortFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3NtpAccPortFlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3NtpAccPortFlowPointHistoryIndex_Object = MibTableColumn
f3NtpAccPortFlowPointHistoryIndex = _F3NtpAccPortFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1, 1),
    _F3NtpAccPortFlowPointHistoryIndex_Type()
)
f3NtpAccPortFlowPointHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryIndex.setStatus("current")
_F3NtpAccPortFlowPointHistoryTime_Type = DateAndTime
_F3NtpAccPortFlowPointHistoryTime_Object = MibTableColumn
f3NtpAccPortFlowPointHistoryTime = _F3NtpAccPortFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1, 2),
    _F3NtpAccPortFlowPointHistoryTime_Type()
)
f3NtpAccPortFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryTime.setStatus("current")
_F3NtpAccPortFlowPointHistoryValid_Type = TruthValue
_F3NtpAccPortFlowPointHistoryValid_Object = MibTableColumn
f3NtpAccPortFlowPointHistoryValid = _F3NtpAccPortFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1, 3),
    _F3NtpAccPortFlowPointHistoryValid_Type()
)
f3NtpAccPortFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryValid.setStatus("current")
_F3NtpAccPortFlowPointHistoryAction_Type = CmPmBinAction
_F3NtpAccPortFlowPointHistoryAction_Object = MibTableColumn
f3NtpAccPortFlowPointHistoryAction = _F3NtpAccPortFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1, 4),
    _F3NtpAccPortFlowPointHistoryAction_Type()
)
f3NtpAccPortFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryAction.setStatus("current")
_F3NtpAccPortFlowPointHistoryRequestsDropped_Type = PerfCounter64
_F3NtpAccPortFlowPointHistoryRequestsDropped_Object = MibTableColumn
f3NtpAccPortFlowPointHistoryRequestsDropped = _F3NtpAccPortFlowPointHistoryRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1, 5),
    _F3NtpAccPortFlowPointHistoryRequestsDropped_Type()
)
f3NtpAccPortFlowPointHistoryRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryRequestsDropped.setStatus("current")
_F3NtpAccPortFlowPointHistoryRequestsReceived_Type = PerfCounter64
_F3NtpAccPortFlowPointHistoryRequestsReceived_Object = MibTableColumn
f3NtpAccPortFlowPointHistoryRequestsReceived = _F3NtpAccPortFlowPointHistoryRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1, 6),
    _F3NtpAccPortFlowPointHistoryRequestsReceived_Type()
)
f3NtpAccPortFlowPointHistoryRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryRequestsReceived.setStatus("current")
_F3NtpAccPortFlowPointHistoryResponsesTransmitted_Type = PerfCounter64
_F3NtpAccPortFlowPointHistoryResponsesTransmitted_Object = MibTableColumn
f3NtpAccPortFlowPointHistoryResponsesTransmitted = _F3NtpAccPortFlowPointHistoryResponsesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 5, 1, 7),
    _F3NtpAccPortFlowPointHistoryResponsesTransmitted_Type()
)
f3NtpAccPortFlowPointHistoryResponsesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointHistoryResponsesTransmitted.setStatus("current")
_F3NtpAccPortFlowPointThresholdTable_Object = MibTable
f3NtpAccPortFlowPointThresholdTable = _F3NtpAccPortFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6)
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdTable.setStatus("current")
_F3NtpAccPortFlowPointThresholdEntry_Object = MibTableRow
f3NtpAccPortFlowPointThresholdEntry = _F3NtpAccPortFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6, 1)
)
f3NtpAccPortFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointStatsIndex"),
    (0, "F3-NTP-MIB", "f3NtpAccPortFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdEntry.setStatus("current")


class _F3NtpAccPortFlowPointThresholdIndex_Type(Integer32):
    """Custom type f3NtpAccPortFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NtpAccPortFlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3NtpAccPortFlowPointThresholdIndex_Object = MibTableColumn
f3NtpAccPortFlowPointThresholdIndex = _F3NtpAccPortFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6, 1, 1),
    _F3NtpAccPortFlowPointThresholdIndex_Type()
)
f3NtpAccPortFlowPointThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdIndex.setStatus("current")
_F3NtpAccPortFlowPointThresholdInterval_Type = CmPmIntervalType
_F3NtpAccPortFlowPointThresholdInterval_Object = MibTableColumn
f3NtpAccPortFlowPointThresholdInterval = _F3NtpAccPortFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6, 1, 2),
    _F3NtpAccPortFlowPointThresholdInterval_Type()
)
f3NtpAccPortFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdInterval.setStatus("current")
_F3NtpAccPortFlowPointThresholdVariable_Type = VariablePointer
_F3NtpAccPortFlowPointThresholdVariable_Object = MibTableColumn
f3NtpAccPortFlowPointThresholdVariable = _F3NtpAccPortFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6, 1, 3),
    _F3NtpAccPortFlowPointThresholdVariable_Type()
)
f3NtpAccPortFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdVariable.setStatus("current")
_F3NtpAccPortFlowPointThresholdValueLo_Type = Unsigned32
_F3NtpAccPortFlowPointThresholdValueLo_Object = MibTableColumn
f3NtpAccPortFlowPointThresholdValueLo = _F3NtpAccPortFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6, 1, 4),
    _F3NtpAccPortFlowPointThresholdValueLo_Type()
)
f3NtpAccPortFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdValueLo.setStatus("current")
_F3NtpAccPortFlowPointThresholdValueHi_Type = Unsigned32
_F3NtpAccPortFlowPointThresholdValueHi_Object = MibTableColumn
f3NtpAccPortFlowPointThresholdValueHi = _F3NtpAccPortFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6, 1, 5),
    _F3NtpAccPortFlowPointThresholdValueHi_Type()
)
f3NtpAccPortFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdValueHi.setStatus("current")
_F3NtpAccPortFlowPointThresholdMonValue_Type = PerfCounter64
_F3NtpAccPortFlowPointThresholdMonValue_Object = MibTableColumn
f3NtpAccPortFlowPointThresholdMonValue = _F3NtpAccPortFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 6, 1, 6),
    _F3NtpAccPortFlowPointThresholdMonValue_Type()
)
f3NtpAccPortFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpAccPortFlowPointThresholdMonValue.setStatus("current")
_F3NtpNetPortFlowPointStatsTable_Object = MibTable
f3NtpNetPortFlowPointStatsTable = _F3NtpNetPortFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7)
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsTable.setStatus("current")
_F3NtpNetPortFlowPointStatsEntry_Object = MibTableRow
f3NtpNetPortFlowPointStatsEntry = _F3NtpNetPortFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1)
)
f3NtpNetPortFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsEntry.setStatus("current")


class _F3NtpNetPortFlowPointStatsIndex_Type(Integer32):
    """Custom type f3NtpNetPortFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3NtpNetPortFlowPointStatsIndex_Type.__name__ = "Integer32"
_F3NtpNetPortFlowPointStatsIndex_Object = MibTableColumn
f3NtpNetPortFlowPointStatsIndex = _F3NtpNetPortFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1, 1),
    _F3NtpNetPortFlowPointStatsIndex_Type()
)
f3NtpNetPortFlowPointStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsIndex.setStatus("current")
_F3NtpNetPortFlowPointStatsIntervalType_Type = CmPmIntervalType
_F3NtpNetPortFlowPointStatsIntervalType_Object = MibTableColumn
f3NtpNetPortFlowPointStatsIntervalType = _F3NtpNetPortFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1, 2),
    _F3NtpNetPortFlowPointStatsIntervalType_Type()
)
f3NtpNetPortFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsIntervalType.setStatus("current")
_F3NtpNetPortFlowPointStatsValid_Type = TruthValue
_F3NtpNetPortFlowPointStatsValid_Object = MibTableColumn
f3NtpNetPortFlowPointStatsValid = _F3NtpNetPortFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1, 3),
    _F3NtpNetPortFlowPointStatsValid_Type()
)
f3NtpNetPortFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsValid.setStatus("current")
_F3NtpNetPortFlowPointStatsAction_Type = CmPmBinAction
_F3NtpNetPortFlowPointStatsAction_Object = MibTableColumn
f3NtpNetPortFlowPointStatsAction = _F3NtpNetPortFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1, 4),
    _F3NtpNetPortFlowPointStatsAction_Type()
)
f3NtpNetPortFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsAction.setStatus("current")
_F3NtpNetPortFlowPointStatsRequestsDropped_Type = PerfCounter64
_F3NtpNetPortFlowPointStatsRequestsDropped_Object = MibTableColumn
f3NtpNetPortFlowPointStatsRequestsDropped = _F3NtpNetPortFlowPointStatsRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1, 5),
    _F3NtpNetPortFlowPointStatsRequestsDropped_Type()
)
f3NtpNetPortFlowPointStatsRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsRequestsDropped.setStatus("current")
_F3NtpNetPortFlowPointStatsRequestsReceived_Type = PerfCounter64
_F3NtpNetPortFlowPointStatsRequestsReceived_Object = MibTableColumn
f3NtpNetPortFlowPointStatsRequestsReceived = _F3NtpNetPortFlowPointStatsRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1, 6),
    _F3NtpNetPortFlowPointStatsRequestsReceived_Type()
)
f3NtpNetPortFlowPointStatsRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsRequestsReceived.setStatus("current")
_F3NtpNetPortFlowPointStatsResponsesTransmitted_Type = PerfCounter64
_F3NtpNetPortFlowPointStatsResponsesTransmitted_Object = MibTableColumn
f3NtpNetPortFlowPointStatsResponsesTransmitted = _F3NtpNetPortFlowPointStatsResponsesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 7, 1, 7),
    _F3NtpNetPortFlowPointStatsResponsesTransmitted_Type()
)
f3NtpNetPortFlowPointStatsResponsesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointStatsResponsesTransmitted.setStatus("current")
_F3NtpNetPortFlowPointHistoryTable_Object = MibTable
f3NtpNetPortFlowPointHistoryTable = _F3NtpNetPortFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8)
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryTable.setStatus("current")
_F3NtpNetPortFlowPointHistoryEntry_Object = MibTableRow
f3NtpNetPortFlowPointHistoryEntry = _F3NtpNetPortFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1)
)
f3NtpNetPortFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointStatsIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryEntry.setStatus("current")


class _F3NtpNetPortFlowPointHistoryIndex_Type(Integer32):
    """Custom type f3NtpNetPortFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3NtpNetPortFlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3NtpNetPortFlowPointHistoryIndex_Object = MibTableColumn
f3NtpNetPortFlowPointHistoryIndex = _F3NtpNetPortFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1, 1),
    _F3NtpNetPortFlowPointHistoryIndex_Type()
)
f3NtpNetPortFlowPointHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryIndex.setStatus("current")
_F3NtpNetPortFlowPointHistoryTime_Type = DateAndTime
_F3NtpNetPortFlowPointHistoryTime_Object = MibTableColumn
f3NtpNetPortFlowPointHistoryTime = _F3NtpNetPortFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1, 2),
    _F3NtpNetPortFlowPointHistoryTime_Type()
)
f3NtpNetPortFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryTime.setStatus("current")
_F3NtpNetPortFlowPointHistoryValid_Type = TruthValue
_F3NtpNetPortFlowPointHistoryValid_Object = MibTableColumn
f3NtpNetPortFlowPointHistoryValid = _F3NtpNetPortFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1, 3),
    _F3NtpNetPortFlowPointHistoryValid_Type()
)
f3NtpNetPortFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryValid.setStatus("current")
_F3NtpNetPortFlowPointHistoryAction_Type = CmPmBinAction
_F3NtpNetPortFlowPointHistoryAction_Object = MibTableColumn
f3NtpNetPortFlowPointHistoryAction = _F3NtpNetPortFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1, 4),
    _F3NtpNetPortFlowPointHistoryAction_Type()
)
f3NtpNetPortFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryAction.setStatus("current")
_F3NtpNetPortFlowPointHistoryRequestsDropped_Type = PerfCounter64
_F3NtpNetPortFlowPointHistoryRequestsDropped_Object = MibTableColumn
f3NtpNetPortFlowPointHistoryRequestsDropped = _F3NtpNetPortFlowPointHistoryRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1, 5),
    _F3NtpNetPortFlowPointHistoryRequestsDropped_Type()
)
f3NtpNetPortFlowPointHistoryRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryRequestsDropped.setStatus("current")
_F3NtpNetPortFlowPointHistoryRequestsReceived_Type = PerfCounter64
_F3NtpNetPortFlowPointHistoryRequestsReceived_Object = MibTableColumn
f3NtpNetPortFlowPointHistoryRequestsReceived = _F3NtpNetPortFlowPointHistoryRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1, 6),
    _F3NtpNetPortFlowPointHistoryRequestsReceived_Type()
)
f3NtpNetPortFlowPointHistoryRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryRequestsReceived.setStatus("current")
_F3NtpNetPortFlowPointHistoryResponsesTransmitted_Type = PerfCounter64
_F3NtpNetPortFlowPointHistoryResponsesTransmitted_Object = MibTableColumn
f3NtpNetPortFlowPointHistoryResponsesTransmitted = _F3NtpNetPortFlowPointHistoryResponsesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 8, 1, 7),
    _F3NtpNetPortFlowPointHistoryResponsesTransmitted_Type()
)
f3NtpNetPortFlowPointHistoryResponsesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointHistoryResponsesTransmitted.setStatus("current")
_F3NtpNetPortFlowPointThresholdTable_Object = MibTable
f3NtpNetPortFlowPointThresholdTable = _F3NtpNetPortFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9)
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdTable.setStatus("current")
_F3NtpNetPortFlowPointThresholdEntry_Object = MibTableRow
f3NtpNetPortFlowPointThresholdEntry = _F3NtpNetPortFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9, 1)
)
f3NtpNetPortFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointStatsIndex"),
    (0, "F3-NTP-MIB", "f3NtpNetPortFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdEntry.setStatus("current")


class _F3NtpNetPortFlowPointThresholdIndex_Type(Integer32):
    """Custom type f3NtpNetPortFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NtpNetPortFlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3NtpNetPortFlowPointThresholdIndex_Object = MibTableColumn
f3NtpNetPortFlowPointThresholdIndex = _F3NtpNetPortFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9, 1, 1),
    _F3NtpNetPortFlowPointThresholdIndex_Type()
)
f3NtpNetPortFlowPointThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdIndex.setStatus("current")
_F3NtpNetPortFlowPointThresholdInterval_Type = CmPmIntervalType
_F3NtpNetPortFlowPointThresholdInterval_Object = MibTableColumn
f3NtpNetPortFlowPointThresholdInterval = _F3NtpNetPortFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9, 1, 2),
    _F3NtpNetPortFlowPointThresholdInterval_Type()
)
f3NtpNetPortFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdInterval.setStatus("current")
_F3NtpNetPortFlowPointThresholdVariable_Type = VariablePointer
_F3NtpNetPortFlowPointThresholdVariable_Object = MibTableColumn
f3NtpNetPortFlowPointThresholdVariable = _F3NtpNetPortFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9, 1, 3),
    _F3NtpNetPortFlowPointThresholdVariable_Type()
)
f3NtpNetPortFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdVariable.setStatus("current")
_F3NtpNetPortFlowPointThresholdValueLo_Type = Unsigned32
_F3NtpNetPortFlowPointThresholdValueLo_Object = MibTableColumn
f3NtpNetPortFlowPointThresholdValueLo = _F3NtpNetPortFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9, 1, 4),
    _F3NtpNetPortFlowPointThresholdValueLo_Type()
)
f3NtpNetPortFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdValueLo.setStatus("current")
_F3NtpNetPortFlowPointThresholdValueHi_Type = Unsigned32
_F3NtpNetPortFlowPointThresholdValueHi_Object = MibTableColumn
f3NtpNetPortFlowPointThresholdValueHi = _F3NtpNetPortFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9, 1, 5),
    _F3NtpNetPortFlowPointThresholdValueHi_Type()
)
f3NtpNetPortFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdValueHi.setStatus("current")
_F3NtpNetPortFlowPointThresholdMonValue_Type = PerfCounter64
_F3NtpNetPortFlowPointThresholdMonValue_Object = MibTableColumn
f3NtpNetPortFlowPointThresholdMonValue = _F3NtpNetPortFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 9, 1, 6),
    _F3NtpNetPortFlowPointThresholdMonValue_Type()
)
f3NtpNetPortFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpNetPortFlowPointThresholdMonValue.setStatus("current")
_F3NtpTrackedClientStatsTable_Object = MibTable
f3NtpTrackedClientStatsTable = _F3NtpTrackedClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10)
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsTable.setStatus("current")
_F3NtpTrackedClientStatsEntry_Object = MibTableRow
f3NtpTrackedClientStatsEntry = _F3NtpTrackedClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1)
)
f3NtpTrackedClientStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NCIIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientStatsClientIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsEntry.setStatus("current")


class _F3NtpTrackedClientStatsIndex_Type(Integer32):
    """Custom type f3NtpTrackedClientStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3NtpTrackedClientStatsIndex_Type.__name__ = "Integer32"
_F3NtpTrackedClientStatsIndex_Object = MibTableColumn
f3NtpTrackedClientStatsIndex = _F3NtpTrackedClientStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1, 1),
    _F3NtpTrackedClientStatsIndex_Type()
)
f3NtpTrackedClientStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsIndex.setStatus("current")


class _F3NtpTrackedClientStatsClientIndex_Type(Integer32):
    """Custom type f3NtpTrackedClientStatsClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3NtpTrackedClientStatsClientIndex_Type.__name__ = "Integer32"
_F3NtpTrackedClientStatsClientIndex_Object = MibTableColumn
f3NtpTrackedClientStatsClientIndex = _F3NtpTrackedClientStatsClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1, 2),
    _F3NtpTrackedClientStatsClientIndex_Type()
)
f3NtpTrackedClientStatsClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsClientIndex.setStatus("current")
_F3NtpTrackedClientStatsIntervalType_Type = CmPmIntervalType
_F3NtpTrackedClientStatsIntervalType_Object = MibTableColumn
f3NtpTrackedClientStatsIntervalType = _F3NtpTrackedClientStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1, 3),
    _F3NtpTrackedClientStatsIntervalType_Type()
)
f3NtpTrackedClientStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsIntervalType.setStatus("current")
_F3NtpTrackedClientStatsValid_Type = TruthValue
_F3NtpTrackedClientStatsValid_Object = MibTableColumn
f3NtpTrackedClientStatsValid = _F3NtpTrackedClientStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1, 4),
    _F3NtpTrackedClientStatsValid_Type()
)
f3NtpTrackedClientStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsValid.setStatus("current")
_F3NtpTrackedClientStatsAction_Type = CmPmBinAction
_F3NtpTrackedClientStatsAction_Object = MibTableColumn
f3NtpTrackedClientStatsAction = _F3NtpTrackedClientStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1, 5),
    _F3NtpTrackedClientStatsAction_Type()
)
f3NtpTrackedClientStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsAction.setStatus("current")
_F3NtpTrackedClientStatsResponsesTransmitted_Type = PerfCounter64
_F3NtpTrackedClientStatsResponsesTransmitted_Object = MibTableColumn
f3NtpTrackedClientStatsResponsesTransmitted = _F3NtpTrackedClientStatsResponsesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1, 6),
    _F3NtpTrackedClientStatsResponsesTransmitted_Type()
)
f3NtpTrackedClientStatsResponsesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsResponsesTransmitted.setStatus("current")
_F3NtpTrackedClientStatsRequestsReceived_Type = PerfCounter64
_F3NtpTrackedClientStatsRequestsReceived_Object = MibTableColumn
f3NtpTrackedClientStatsRequestsReceived = _F3NtpTrackedClientStatsRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 10, 1, 7),
    _F3NtpTrackedClientStatsRequestsReceived_Type()
)
f3NtpTrackedClientStatsRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientStatsRequestsReceived.setStatus("current")
_F3NtpTrackedClientHistoryTable_Object = MibTable
f3NtpTrackedClientHistoryTable = _F3NtpTrackedClientHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11)
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryTable.setStatus("current")
_F3NtpTrackedClientHistoryEntry_Object = MibTableRow
f3NtpTrackedClientHistoryEntry = _F3NtpTrackedClientHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11, 1)
)
f3NtpTrackedClientHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NCIIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientStatsClientIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientStatsIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryEntry.setStatus("current")


class _F3NtpTrackedClientHistoryIndex_Type(Integer32):
    """Custom type f3NtpTrackedClientHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3NtpTrackedClientHistoryIndex_Type.__name__ = "Integer32"
_F3NtpTrackedClientHistoryIndex_Object = MibTableColumn
f3NtpTrackedClientHistoryIndex = _F3NtpTrackedClientHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11, 1, 1),
    _F3NtpTrackedClientHistoryIndex_Type()
)
f3NtpTrackedClientHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryIndex.setStatus("current")
_F3NtpTrackedClientHistoryTime_Type = DateAndTime
_F3NtpTrackedClientHistoryTime_Object = MibTableColumn
f3NtpTrackedClientHistoryTime = _F3NtpTrackedClientHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11, 1, 2),
    _F3NtpTrackedClientHistoryTime_Type()
)
f3NtpTrackedClientHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryTime.setStatus("current")
_F3NtpTrackedClientHistoryValid_Type = TruthValue
_F3NtpTrackedClientHistoryValid_Object = MibTableColumn
f3NtpTrackedClientHistoryValid = _F3NtpTrackedClientHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11, 1, 3),
    _F3NtpTrackedClientHistoryValid_Type()
)
f3NtpTrackedClientHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryValid.setStatus("current")
_F3NtpTrackedClientHistoryAction_Type = CmPmBinAction
_F3NtpTrackedClientHistoryAction_Object = MibTableColumn
f3NtpTrackedClientHistoryAction = _F3NtpTrackedClientHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11, 1, 4),
    _F3NtpTrackedClientHistoryAction_Type()
)
f3NtpTrackedClientHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryAction.setStatus("current")
_F3NtpTrackedClientHistoryResponsesTransmitted_Type = PerfCounter64
_F3NtpTrackedClientHistoryResponsesTransmitted_Object = MibTableColumn
f3NtpTrackedClientHistoryResponsesTransmitted = _F3NtpTrackedClientHistoryResponsesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11, 1, 5),
    _F3NtpTrackedClientHistoryResponsesTransmitted_Type()
)
f3NtpTrackedClientHistoryResponsesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryResponsesTransmitted.setStatus("current")
_F3NtpTrackedClientHistoryRequestsReceived_Type = PerfCounter64
_F3NtpTrackedClientHistoryRequestsReceived_Object = MibTableColumn
f3NtpTrackedClientHistoryRequestsReceived = _F3NtpTrackedClientHistoryRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 11, 1, 6),
    _F3NtpTrackedClientHistoryRequestsReceived_Type()
)
f3NtpTrackedClientHistoryRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientHistoryRequestsReceived.setStatus("current")
_F3NtpTrackedClientThresholdTable_Object = MibTable
f3NtpTrackedClientThresholdTable = _F3NtpTrackedClientThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12)
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdTable.setStatus("current")
_F3NtpTrackedClientThresholdEntry_Object = MibTableRow
f3NtpTrackedClientThresholdEntry = _F3NtpTrackedClientThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12, 1)
)
f3NtpTrackedClientThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-NTP-MIB", "f3NtpClockIndex"),
    (0, "F3-NTP-MIB", "f3NCIIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientStatsClientIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientStatsIndex"),
    (0, "F3-NTP-MIB", "f3NtpTrackedClientThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdEntry.setStatus("current")


class _F3NtpTrackedClientThresholdIndex_Type(Integer32):
    """Custom type f3NtpTrackedClientThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NtpTrackedClientThresholdIndex_Type.__name__ = "Integer32"
_F3NtpTrackedClientThresholdIndex_Object = MibTableColumn
f3NtpTrackedClientThresholdIndex = _F3NtpTrackedClientThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12, 1, 1),
    _F3NtpTrackedClientThresholdIndex_Type()
)
f3NtpTrackedClientThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdIndex.setStatus("current")
_F3NtpTrackedClientThresholdInterval_Type = CmPmIntervalType
_F3NtpTrackedClientThresholdInterval_Object = MibTableColumn
f3NtpTrackedClientThresholdInterval = _F3NtpTrackedClientThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12, 1, 2),
    _F3NtpTrackedClientThresholdInterval_Type()
)
f3NtpTrackedClientThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdInterval.setStatus("current")
_F3NtpTrackedClientThresholdVariable_Type = VariablePointer
_F3NtpTrackedClientThresholdVariable_Object = MibTableColumn
f3NtpTrackedClientThresholdVariable = _F3NtpTrackedClientThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12, 1, 3),
    _F3NtpTrackedClientThresholdVariable_Type()
)
f3NtpTrackedClientThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdVariable.setStatus("current")
_F3NtpTrackedClientThresholdValueLo_Type = Unsigned32
_F3NtpTrackedClientThresholdValueLo_Object = MibTableColumn
f3NtpTrackedClientThresholdValueLo = _F3NtpTrackedClientThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12, 1, 4),
    _F3NtpTrackedClientThresholdValueLo_Type()
)
f3NtpTrackedClientThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdValueLo.setStatus("current")
_F3NtpTrackedClientThresholdValueHi_Type = Unsigned32
_F3NtpTrackedClientThresholdValueHi_Object = MibTableColumn
f3NtpTrackedClientThresholdValueHi = _F3NtpTrackedClientThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12, 1, 5),
    _F3NtpTrackedClientThresholdValueHi_Type()
)
f3NtpTrackedClientThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdValueHi.setStatus("current")
_F3NtpTrackedClientThresholdMonValue_Type = PerfCounter64
_F3NtpTrackedClientThresholdMonValue_Object = MibTableColumn
f3NtpTrackedClientThresholdMonValue = _F3NtpTrackedClientThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 3, 12, 1, 6),
    _F3NtpTrackedClientThresholdMonValue_Type()
)
f3NtpTrackedClientThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NtpTrackedClientThresholdMonValue.setStatus("current")
_F3NtpPerformanceNotifications_ObjectIdentity = ObjectIdentity
f3NtpPerformanceNotifications = _F3NtpPerformanceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 4)
)

# Managed Objects groups

f3NtpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 2, 2, 1)
)
f3NtpObjectGroup.setObjects(
      *(("F3-NTP-MIB", "f3NtpClockIndex"),
        ("F3-NTP-MIB", "f3NtpClockAlias"),
        ("F3-NTP-MIB", "f3NtpClockAdminState"),
        ("F3-NTP-MIB", "f3NtpClockOperationalState"),
        ("F3-NTP-MIB", "f3NtpClockTimeClock"),
        ("F3-NTP-MIB", "f3NtpClockStratumLevel"),
        ("F3-NTP-MIB", "f3NtpClockLeapIndicator"),
        ("F3-NTP-MIB", "f3NtpClockTimeScale"),
        ("F3-NTP-MIB", "f3NtpClockPrecision"),
        ("F3-NTP-MIB", "f3NtpClockRootDelay"),
        ("F3-NTP-MIB", "f3NtpClockRootDispersion"),
        ("F3-NTP-MIB", "f3NtpClockNtpMode"),
        ("F3-NTP-MIB", "f3NtpClockNtpType"),
        ("F3-NTP-MIB", "f3NtpClockNtpAuthentication"),
        ("F3-NTP-MIB", "f3NtpClockServerState"),
        ("F3-NTP-MIB", "f3NtpClockTimeReferenceLossHandling"),
        ("F3-NTP-MIB", "f3NtpClockRefClockId"),
        ("F3-NTP-MIB", "f3NtpClockStorageType"),
        ("F3-NTP-MIB", "f3NtpClockRowStatus"),
        ("F3-NTP-MIB", "f3NtpAuthenticationSecureMode"),
        ("F3-NTP-MIB", "f3NtpAutokeyCtrl"),
        ("F3-NTP-MIB", "f3NtpClockOffset"),
        ("F3-NTP-MIB", "f3NtpClockSecondaryState"),
        ("F3-NTP-MIB", "f3NCIIndex"),
        ("F3-NTP-MIB", "f3NCIAlias"),
        ("F3-NTP-MIB", "f3NCIAdminState"),
        ("F3-NTP-MIB", "f3NCIOperationalState"),
        ("F3-NTP-MIB", "f3NCIIfName"),
        ("F3-NTP-MIB", "f3NCIIpProtocol"),
        ("F3-NTP-MIB", "f3NCIIpV4Address"),
        ("F3-NTP-MIB", "f3NCIIpV4SubnetMask"),
        ("F3-NTP-MIB", "f3NCIDscp"),
        ("F3-NTP-MIB", "f3NCIStorageType"),
        ("F3-NTP-MIB", "f3NCIRowStatus"),
        ("F3-NTP-MIB", "f3NCIIpV6UdpChecksum"),
        ("F3-NTP-MIB", "f3NCIIpV6Address"),
        ("F3-NTP-MIB", "f3NCIIpV6AddrPrefixLength"),
        ("F3-NTP-MIB", "f3NCIIpV4Gateway"),
        ("F3-NTP-MIB", "f3NCIIpV6Gateway"),
        ("F3-NTP-MIB", "f3NCIDefaultGatewayControl"),
        ("F3-NTP-MIB", "f3NCIDaytimeServiceControl"),
        ("F3-NTP-MIB", "f3NCITimeServiceControl"),
        ("F3-NTP-MIB", "f3NCIBroadcastState"),
        ("F3-NTP-MIB", "f3NCIBroadcastIpV4Address"),
        ("F3-NTP-MIB", "f3NCIBroadcastIpV6Address"),
        ("F3-NTP-MIB", "f3NCIBroadcastInterval"),
        ("F3-NTP-MIB", "f3NCIBroadcastMaxHops"),
        ("F3-NTP-MIB", "f3NCIBroadcastSymKeyId"),
        ("F3-NTP-MIB", "f3NCIBroadcastNtpVersion"),
        ("F3-NTP-MIB", "f3NCIAssociationMode"),
        ("F3-NTP-MIB", "f3NCIPeer1IpV4Address"),
        ("F3-NTP-MIB", "f3NCIPeer2IpV4Address"),
        ("F3-NTP-MIB", "f3NCIPeer3IpV4Address"),
        ("F3-NTP-MIB", "f3NCIPeer1IpV6Address"),
        ("F3-NTP-MIB", "f3NCIPeer2IpV6Address"),
        ("F3-NTP-MIB", "f3NCIPeer3IpV6Address"),
        ("F3-NTP-MIB", "f3NCIPeerMinInterval"),
        ("F3-NTP-MIB", "f3NCIPeerMaxInterval"),
        ("F3-NTP-MIB", "f3NCIPeerSymKeyIdList"),
        ("F3-NTP-MIB", "f3NCITimeScale"),
        ("F3-NTP-MIB", "f3NCICurrentTimeOfDay"),
        ("F3-NTP-MIB", "f3NCINtpHardenedResponderControl"),
        ("F3-NTP-MIB", "f3NtpVirtualPortIndex"),
        ("F3-NTP-MIB", "f3NtpVirtualPortAlias"),
        ("F3-NTP-MIB", "f3NtpVirtualPortAdminState"),
        ("F3-NTP-MIB", "f3NtpVirtualPortOperationalState"),
        ("F3-NTP-MIB", "f3NtpVirtualPortNtpFlowPoint"),
        ("F3-NTP-MIB", "f3NtpVirtualPortStorageType"),
        ("F3-NTP-MIB", "f3NtpVirtualPortRowStatus"),
        ("F3-NTP-MIB", "f3NtpRemoteClientIndex"),
        ("F3-NTP-MIB", "f3NtpRemoteClientIpV4Address"),
        ("F3-NTP-MIB", "f3NtpRemoteClientRxPackets"),
        ("F3-NTP-MIB", "f3NtpRemoteClientAvgPollInterval"),
        ("F3-NTP-MIB", "f3NtpRemoteClientLastPollInterval"),
        ("F3-NTP-MIB", "f3NtpRemoteClientNtpMode"),
        ("F3-NTP-MIB", "f3NtpRemoteClientNtpVersion"),
        ("F3-NTP-MIB", "f3NtpRemoteClientStorageType"),
        ("F3-NTP-MIB", "f3NtpRemoteClientRowStatus"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointIndex"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointAlias"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointAdminState"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointOperationalState"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointType"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointOuterVlanEtherType"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointOuterVlanMemberList"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointOuterUntaggedEnabled"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointInner1VlanEtherType"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointInner1VlanMemberList"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointInner1UntaggedEnabled"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointInner2VlanEtherType"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointInner2VlanMemberList"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointInner2UntaggedEnabled"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointCOS"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointCIRLo"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointCIRHi"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointEIRLo"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointEIRHi"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointBufferSize"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStorageType"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointRowStatus"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointIndex"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointAlias"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointAdminState"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointOperationalState"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointType"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointOuterVlanEtherType"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointOuterVlanMemberList"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointOuterUntaggedEnabled"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointInner1VlanEtherType"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointInner1VlanMemberList"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointInner1UntaggedEnabled"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointInner2VlanEtherType"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointInner2VlanMemberList"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointInner2UntaggedEnabled"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointCOS"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointCIRLo"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointCIRHi"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointEIRLo"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointEIRHi"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointBufferSize"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStorageType"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointRowStatus"),
        ("F3-NTP-MIB", "f3NtpTrackedClientIndex"),
        ("F3-NTP-MIB", "f3NtpTrackedClientAlias"),
        ("F3-NTP-MIB", "f3NtpTrackedClientIpV4Address"),
        ("F3-NTP-MIB", "f3NtpTrackedClientIpV6Address"),
        ("F3-NTP-MIB", "f3NtpTrackedClientStorageType"),
        ("F3-NTP-MIB", "f3NtpTrackedClientRowStatus"),
        ("F3-NTP-MIB", "f3NtpRemoteServerIndex"),
        ("F3-NTP-MIB", "f3NtpRemoteServerAlias"),
        ("F3-NTP-MIB", "f3NtpRemoteServerAdminState"),
        ("F3-NTP-MIB", "f3NtpRemoteServerOperationalState"),
        ("F3-NTP-MIB", "f3NtpRemoteServerServerAddress"),
        ("F3-NTP-MIB", "f3NtpRemoteServerMinPollInterval"),
        ("F3-NTP-MIB", "f3NtpRemoteServerMaxPollInterval"),
        ("F3-NTP-MIB", "f3NtpRemoteServerPreferred"),
        ("F3-NTP-MIB", "f3NtpRemoteServerReach"),
        ("F3-NTP-MIB", "f3NtpRemoteServerStorageType"),
        ("F3-NTP-MIB", "f3NtpRemoteServerRowStatus"))
)
if mibBuilder.loadTexts:
    f3NtpObjectGroup.setStatus("current")

f3NtpPerfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 2, 2, 2)
)
f3NtpPerfObjectGroup.setObjects(
      *(("F3-NTP-MIB", "f3NCIStatsIndex"),
        ("F3-NTP-MIB", "f3NCIStatsIntervalType"),
        ("F3-NTP-MIB", "f3NCIStatsValid"),
        ("F3-NTP-MIB", "f3NCIStatsAction"),
        ("F3-NTP-MIB", "f3NCIStatsRequestsProcessed"),
        ("F3-NTP-MIB", "f3NCIStatsResponsesError"),
        ("F3-NTP-MIB", "f3NCIStatsAuthFailures"),
        ("F3-NTP-MIB", "f3NCIStatsReqsDiscarded"),
        ("F3-NTP-MIB", "f3NCIStatsAvgTPS"),
        ("F3-NTP-MIB", "f3NCIStatsMaxTPS"),
        ("F3-NTP-MIB", "f3NCIHistoryIndex"),
        ("F3-NTP-MIB", "f3NCIHistoryTime"),
        ("F3-NTP-MIB", "f3NCIHistoryValid"),
        ("F3-NTP-MIB", "f3NCIHistoryAction"),
        ("F3-NTP-MIB", "f3NCIHistoryRequestsProcessed"),
        ("F3-NTP-MIB", "f3NCIHistoryResponsesError"),
        ("F3-NTP-MIB", "f3NCIHistoryAuthFailures"),
        ("F3-NTP-MIB", "f3NCIHistoryReqsDiscarded"),
        ("F3-NTP-MIB", "f3NCIHistoryAvgTPS"),
        ("F3-NTP-MIB", "f3NCIHistoryMaxTPS"),
        ("F3-NTP-MIB", "f3NCIThresholdIndex"),
        ("F3-NTP-MIB", "f3NCIThresholdInterval"),
        ("F3-NTP-MIB", "f3NCIThresholdVariable"),
        ("F3-NTP-MIB", "f3NCIThresholdValueLo"),
        ("F3-NTP-MIB", "f3NCIThresholdValueHi"),
        ("F3-NTP-MIB", "f3NCIThresholdMonValue"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStatsIndex"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStatsIntervalType"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStatsValid"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStatsAction"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStatsRequestsDropped"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStatsRequestsReceived"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointStatsResponsesTransmitted"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryIndex"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryTime"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryValid"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryAction"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryRequestsDropped"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryRequestsReceived"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointHistoryResponsesTransmitted"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointThresholdIndex"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointThresholdInterval"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointThresholdVariable"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointThresholdValueLo"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointThresholdValueHi"),
        ("F3-NTP-MIB", "f3NtpAccPortFlowPointThresholdMonValue"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStatsIndex"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStatsIntervalType"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStatsValid"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStatsAction"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStatsRequestsDropped"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStatsRequestsReceived"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointStatsResponsesTransmitted"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryIndex"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryTime"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryValid"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryAction"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryRequestsDropped"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryRequestsReceived"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointHistoryResponsesTransmitted"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointThresholdIndex"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointThresholdInterval"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointThresholdVariable"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointThresholdValueLo"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointThresholdValueHi"),
        ("F3-NTP-MIB", "f3NtpNetPortFlowPointThresholdMonValue"),
        ("F3-NTP-MIB", "f3NtpTrackedClientStatsIndex"),
        ("F3-NTP-MIB", "f3NtpTrackedClientStatsIntervalType"),
        ("F3-NTP-MIB", "f3NtpTrackedClientStatsValid"),
        ("F3-NTP-MIB", "f3NtpTrackedClientStatsAction"),
        ("F3-NTP-MIB", "f3NtpTrackedClientStatsResponsesTransmitted"),
        ("F3-NTP-MIB", "f3NtpTrackedClientStatsRequestsReceived"),
        ("F3-NTP-MIB", "f3NtpTrackedClientHistoryIndex"),
        ("F3-NTP-MIB", "f3NtpTrackedClientHistoryTime"),
        ("F3-NTP-MIB", "f3NtpTrackedClientHistoryValid"),
        ("F3-NTP-MIB", "f3NtpTrackedClientHistoryAction"),
        ("F3-NTP-MIB", "f3NtpTrackedClientHistoryResponsesTransmitted"),
        ("F3-NTP-MIB", "f3NtpTrackedClientHistoryRequestsReceived"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdIndex"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdInterval"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdVariable"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdValueLo"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdValueHi"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NtpPerfObjectGroup.setStatus("current")


# Notification objects

f3NtpTrackedClientCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 4, 1)
)
f3NtpTrackedClientCrossingAlert.setObjects(
      *(("F3-NTP-MIB", "f3NtpTrackedClientThresholdIndex"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdInterval"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdVariable"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdValueLo"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdValueHi"),
        ("F3-NTP-MIB", "f3NtpTrackedClientThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NtpTrackedClientCrossingAlert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

f3NtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 47, 2, 1, 1)
)
f3NtpCompliance.setObjects(
      *(("F3-NTP-MIB", "f3NtpObjectGroup"),
        ("F3-NTP-MIB", "f3NtpPerfObjectGroup"))
)
if mibBuilder.loadTexts:
    f3NtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-NTP-MIB",
    **{"NtpFlowPointType": NtpFlowPointType,
       "NtpTimeScale": NtpTimeScale,
       "ToggleValue": ToggleValue,
       "GnssSyncLossAction": GnssSyncLossAction,
       "NtpBroadcastInterval": NtpBroadcastInterval,
       "NtpVersion": NtpVersion,
       "NtpAssociationType": NtpAssociationType,
       "NtpPollingInterval": NtpPollingInterval,
       "f3NtpMIB": f3NtpMIB,
       "f3NtpObjects": f3NtpObjects,
       "f3NtpClockTable": f3NtpClockTable,
       "f3NtpClockEntry": f3NtpClockEntry,
       "f3NtpClockIndex": f3NtpClockIndex,
       "f3NtpClockAlias": f3NtpClockAlias,
       "f3NtpClockAdminState": f3NtpClockAdminState,
       "f3NtpClockOperationalState": f3NtpClockOperationalState,
       "f3NtpClockTimeClock": f3NtpClockTimeClock,
       "f3NtpClockStratumLevel": f3NtpClockStratumLevel,
       "f3NtpClockLeapIndicator": f3NtpClockLeapIndicator,
       "f3NtpClockTimeScale": f3NtpClockTimeScale,
       "f3NtpClockPrecision": f3NtpClockPrecision,
       "f3NtpClockRootDelay": f3NtpClockRootDelay,
       "f3NtpClockRootDispersion": f3NtpClockRootDispersion,
       "f3NtpClockNtpMode": f3NtpClockNtpMode,
       "f3NtpClockNtpType": f3NtpClockNtpType,
       "f3NtpClockNtpAuthentication": f3NtpClockNtpAuthentication,
       "f3NtpClockServerState": f3NtpClockServerState,
       "f3NtpClockTimeReferenceLossHandling": f3NtpClockTimeReferenceLossHandling,
       "f3NtpClockRefClockId": f3NtpClockRefClockId,
       "f3NtpClockStorageType": f3NtpClockStorageType,
       "f3NtpClockRowStatus": f3NtpClockRowStatus,
       "f3NtpAuthenticationSecureMode": f3NtpAuthenticationSecureMode,
       "f3NtpAutokeyCtrl": f3NtpAutokeyCtrl,
       "f3NtpClockOffset": f3NtpClockOffset,
       "f3NtpClockSecondaryState": f3NtpClockSecondaryState,
       "f3NCITable": f3NCITable,
       "f3NCIEntry": f3NCIEntry,
       "f3NCIIndex": f3NCIIndex,
       "f3NCIAlias": f3NCIAlias,
       "f3NCIAdminState": f3NCIAdminState,
       "f3NCIOperationalState": f3NCIOperationalState,
       "f3NCIIfName": f3NCIIfName,
       "f3NCIIpProtocol": f3NCIIpProtocol,
       "f3NCIIpV4Address": f3NCIIpV4Address,
       "f3NCIIpV4SubnetMask": f3NCIIpV4SubnetMask,
       "f3NCIDscp": f3NCIDscp,
       "f3NCIStorageType": f3NCIStorageType,
       "f3NCIRowStatus": f3NCIRowStatus,
       "f3NCIIpV6UdpChecksum": f3NCIIpV6UdpChecksum,
       "f3NCIIpV6Address": f3NCIIpV6Address,
       "f3NCIIpV6AddrPrefixLength": f3NCIIpV6AddrPrefixLength,
       "f3NCIIpV4Gateway": f3NCIIpV4Gateway,
       "f3NCIIpV6Gateway": f3NCIIpV6Gateway,
       "f3NCIDefaultGatewayControl": f3NCIDefaultGatewayControl,
       "f3NCITimeServiceControl": f3NCITimeServiceControl,
       "f3NCIDaytimeServiceControl": f3NCIDaytimeServiceControl,
       "f3NCIBroadcastState": f3NCIBroadcastState,
       "f3NCIBroadcastIpV4Address": f3NCIBroadcastIpV4Address,
       "f3NCIBroadcastIpV6Address": f3NCIBroadcastIpV6Address,
       "f3NCIBroadcastInterval": f3NCIBroadcastInterval,
       "f3NCIBroadcastMaxHops": f3NCIBroadcastMaxHops,
       "f3NCIBroadcastSymKeyId": f3NCIBroadcastSymKeyId,
       "f3NCIBroadcastNtpVersion": f3NCIBroadcastNtpVersion,
       "f3NCIAssociationMode": f3NCIAssociationMode,
       "f3NCIPeer1IpV4Address": f3NCIPeer1IpV4Address,
       "f3NCIPeer2IpV4Address": f3NCIPeer2IpV4Address,
       "f3NCIPeer3IpV4Address": f3NCIPeer3IpV4Address,
       "f3NCIPeer1IpV6Address": f3NCIPeer1IpV6Address,
       "f3NCIPeer2IpV6Address": f3NCIPeer2IpV6Address,
       "f3NCIPeer3IpV6Address": f3NCIPeer3IpV6Address,
       "f3NCIPeerMinInterval": f3NCIPeerMinInterval,
       "f3NCIPeerMaxInterval": f3NCIPeerMaxInterval,
       "f3NCIPeerSymKeyIdList": f3NCIPeerSymKeyIdList,
       "f3NCITimeScale": f3NCITimeScale,
       "f3NCICurrentTimeOfDay": f3NCICurrentTimeOfDay,
       "f3NCINtpHardenedResponderControl": f3NCINtpHardenedResponderControl,
       "f3NtpVirtualPortTable": f3NtpVirtualPortTable,
       "f3NtpVirtualPortEntry": f3NtpVirtualPortEntry,
       "f3NtpVirtualPortIndex": f3NtpVirtualPortIndex,
       "f3NtpVirtualPortAlias": f3NtpVirtualPortAlias,
       "f3NtpVirtualPortAdminState": f3NtpVirtualPortAdminState,
       "f3NtpVirtualPortOperationalState": f3NtpVirtualPortOperationalState,
       "f3NtpVirtualPortNtpFlowPoint": f3NtpVirtualPortNtpFlowPoint,
       "f3NtpVirtualPortStorageType": f3NtpVirtualPortStorageType,
       "f3NtpVirtualPortRowStatus": f3NtpVirtualPortRowStatus,
       "f3NtpRemoteClientTable": f3NtpRemoteClientTable,
       "f3NtpRemoteClientEntry": f3NtpRemoteClientEntry,
       "f3NtpRemoteClientIndex": f3NtpRemoteClientIndex,
       "f3NtpRemoteClientIpV4Address": f3NtpRemoteClientIpV4Address,
       "f3NtpRemoteClientRxPackets": f3NtpRemoteClientRxPackets,
       "f3NtpRemoteClientAvgPollInterval": f3NtpRemoteClientAvgPollInterval,
       "f3NtpRemoteClientLastPollInterval": f3NtpRemoteClientLastPollInterval,
       "f3NtpRemoteClientNtpMode": f3NtpRemoteClientNtpMode,
       "f3NtpRemoteClientNtpVersion": f3NtpRemoteClientNtpVersion,
       "f3NtpRemoteClientStorageType": f3NtpRemoteClientStorageType,
       "f3NtpRemoteClientRowStatus": f3NtpRemoteClientRowStatus,
       "f3NtpAccPortFlowPointTable": f3NtpAccPortFlowPointTable,
       "f3NtpAccPortFlowPointEntry": f3NtpAccPortFlowPointEntry,
       "f3NtpAccPortFlowPointIndex": f3NtpAccPortFlowPointIndex,
       "f3NtpAccPortFlowPointAlias": f3NtpAccPortFlowPointAlias,
       "f3NtpAccPortFlowPointAdminState": f3NtpAccPortFlowPointAdminState,
       "f3NtpAccPortFlowPointOperationalState": f3NtpAccPortFlowPointOperationalState,
       "f3NtpAccPortFlowPointType": f3NtpAccPortFlowPointType,
       "f3NtpAccPortFlowPointOuterVlanEtherType": f3NtpAccPortFlowPointOuterVlanEtherType,
       "f3NtpAccPortFlowPointOuterVlanMemberList": f3NtpAccPortFlowPointOuterVlanMemberList,
       "f3NtpAccPortFlowPointOuterUntaggedEnabled": f3NtpAccPortFlowPointOuterUntaggedEnabled,
       "f3NtpAccPortFlowPointInner1VlanEtherType": f3NtpAccPortFlowPointInner1VlanEtherType,
       "f3NtpAccPortFlowPointInner1VlanMemberList": f3NtpAccPortFlowPointInner1VlanMemberList,
       "f3NtpAccPortFlowPointInner1UntaggedEnabled": f3NtpAccPortFlowPointInner1UntaggedEnabled,
       "f3NtpAccPortFlowPointInner2VlanEtherType": f3NtpAccPortFlowPointInner2VlanEtherType,
       "f3NtpAccPortFlowPointInner2VlanMemberList": f3NtpAccPortFlowPointInner2VlanMemberList,
       "f3NtpAccPortFlowPointInner2UntaggedEnabled": f3NtpAccPortFlowPointInner2UntaggedEnabled,
       "f3NtpAccPortFlowPointCOS": f3NtpAccPortFlowPointCOS,
       "f3NtpAccPortFlowPointCIRLo": f3NtpAccPortFlowPointCIRLo,
       "f3NtpAccPortFlowPointCIRHi": f3NtpAccPortFlowPointCIRHi,
       "f3NtpAccPortFlowPointEIRLo": f3NtpAccPortFlowPointEIRLo,
       "f3NtpAccPortFlowPointEIRHi": f3NtpAccPortFlowPointEIRHi,
       "f3NtpAccPortFlowPointBufferSize": f3NtpAccPortFlowPointBufferSize,
       "f3NtpAccPortFlowPointStorageType": f3NtpAccPortFlowPointStorageType,
       "f3NtpAccPortFlowPointRowStatus": f3NtpAccPortFlowPointRowStatus,
       "f3NtpNetPortFlowPointTable": f3NtpNetPortFlowPointTable,
       "f3NtpNetPortFlowPointEntry": f3NtpNetPortFlowPointEntry,
       "f3NtpNetPortFlowPointIndex": f3NtpNetPortFlowPointIndex,
       "f3NtpNetPortFlowPointAlias": f3NtpNetPortFlowPointAlias,
       "f3NtpNetPortFlowPointAdminState": f3NtpNetPortFlowPointAdminState,
       "f3NtpNetPortFlowPointOperationalState": f3NtpNetPortFlowPointOperationalState,
       "f3NtpNetPortFlowPointType": f3NtpNetPortFlowPointType,
       "f3NtpNetPortFlowPointOuterVlanEtherType": f3NtpNetPortFlowPointOuterVlanEtherType,
       "f3NtpNetPortFlowPointOuterVlanMemberList": f3NtpNetPortFlowPointOuterVlanMemberList,
       "f3NtpNetPortFlowPointOuterUntaggedEnabled": f3NtpNetPortFlowPointOuterUntaggedEnabled,
       "f3NtpNetPortFlowPointInner1VlanEtherType": f3NtpNetPortFlowPointInner1VlanEtherType,
       "f3NtpNetPortFlowPointInner1VlanMemberList": f3NtpNetPortFlowPointInner1VlanMemberList,
       "f3NtpNetPortFlowPointInner1UntaggedEnabled": f3NtpNetPortFlowPointInner1UntaggedEnabled,
       "f3NtpNetPortFlowPointInner2VlanEtherType": f3NtpNetPortFlowPointInner2VlanEtherType,
       "f3NtpNetPortFlowPointInner2VlanMemberList": f3NtpNetPortFlowPointInner2VlanMemberList,
       "f3NtpNetPortFlowPointInner2UntaggedEnabled": f3NtpNetPortFlowPointInner2UntaggedEnabled,
       "f3NtpNetPortFlowPointCOS": f3NtpNetPortFlowPointCOS,
       "f3NtpNetPortFlowPointCIRLo": f3NtpNetPortFlowPointCIRLo,
       "f3NtpNetPortFlowPointCIRHi": f3NtpNetPortFlowPointCIRHi,
       "f3NtpNetPortFlowPointEIRLo": f3NtpNetPortFlowPointEIRLo,
       "f3NtpNetPortFlowPointEIRHi": f3NtpNetPortFlowPointEIRHi,
       "f3NtpNetPortFlowPointBufferSize": f3NtpNetPortFlowPointBufferSize,
       "f3NtpNetPortFlowPointStorageType": f3NtpNetPortFlowPointStorageType,
       "f3NtpNetPortFlowPointRowStatus": f3NtpNetPortFlowPointRowStatus,
       "f3NtpTrackedClientTable": f3NtpTrackedClientTable,
       "f3NtpTrackedClientEntry": f3NtpTrackedClientEntry,
       "f3NtpTrackedClientIndex": f3NtpTrackedClientIndex,
       "f3NtpTrackedClientAlias": f3NtpTrackedClientAlias,
       "f3NtpTrackedClientIpV4Address": f3NtpTrackedClientIpV4Address,
       "f3NtpTrackedClientIpV6Address": f3NtpTrackedClientIpV6Address,
       "f3NtpTrackedClientStorageType": f3NtpTrackedClientStorageType,
       "f3NtpTrackedClientRowStatus": f3NtpTrackedClientRowStatus,
       "f3NtpRemoteServerTable": f3NtpRemoteServerTable,
       "f3NtpRemoteServerEntry": f3NtpRemoteServerEntry,
       "f3NtpRemoteServerIndex": f3NtpRemoteServerIndex,
       "f3NtpRemoteServerAlias": f3NtpRemoteServerAlias,
       "f3NtpRemoteServerAdminState": f3NtpRemoteServerAdminState,
       "f3NtpRemoteServerOperationalState": f3NtpRemoteServerOperationalState,
       "f3NtpRemoteServerSecondaryState": f3NtpRemoteServerSecondaryState,
       "f3NtpRemoteServerServerAddress": f3NtpRemoteServerServerAddress,
       "f3NtpRemoteServerMinPollInterval": f3NtpRemoteServerMinPollInterval,
       "f3NtpRemoteServerMaxPollInterval": f3NtpRemoteServerMaxPollInterval,
       "f3NtpRemoteServerPreferred": f3NtpRemoteServerPreferred,
       "f3NtpRemoteServerReach": f3NtpRemoteServerReach,
       "f3NtpRemoteServerStorageType": f3NtpRemoteServerStorageType,
       "f3NtpRemoteServerRowStatus": f3NtpRemoteServerRowStatus,
       "f3NtpConformance": f3NtpConformance,
       "f3NtpCompliances": f3NtpCompliances,
       "f3NtpCompliance": f3NtpCompliance,
       "f3NtpGroups": f3NtpGroups,
       "f3NtpObjectGroup": f3NtpObjectGroup,
       "f3NtpPerfObjectGroup": f3NtpPerfObjectGroup,
       "f3NtpPerformanceObjects": f3NtpPerformanceObjects,
       "f3NCIStatsTable": f3NCIStatsTable,
       "f3NCIStatsEntry": f3NCIStatsEntry,
       "f3NCIStatsIndex": f3NCIStatsIndex,
       "f3NCIStatsIntervalType": f3NCIStatsIntervalType,
       "f3NCIStatsValid": f3NCIStatsValid,
       "f3NCIStatsAction": f3NCIStatsAction,
       "f3NCIStatsRequestsProcessed": f3NCIStatsRequestsProcessed,
       "f3NCIStatsResponsesError": f3NCIStatsResponsesError,
       "f3NCIStatsAuthFailures": f3NCIStatsAuthFailures,
       "f3NCIStatsReqsDiscarded": f3NCIStatsReqsDiscarded,
       "f3NCIStatsAvgTPS": f3NCIStatsAvgTPS,
       "f3NCIStatsMaxTPS": f3NCIStatsMaxTPS,
       "f3NCIHistoryTable": f3NCIHistoryTable,
       "f3NCIHistoryEntry": f3NCIHistoryEntry,
       "f3NCIHistoryIndex": f3NCIHistoryIndex,
       "f3NCIHistoryTime": f3NCIHistoryTime,
       "f3NCIHistoryValid": f3NCIHistoryValid,
       "f3NCIHistoryAction": f3NCIHistoryAction,
       "f3NCIHistoryRequestsProcessed": f3NCIHistoryRequestsProcessed,
       "f3NCIHistoryResponsesError": f3NCIHistoryResponsesError,
       "f3NCIHistoryAuthFailures": f3NCIHistoryAuthFailures,
       "f3NCIHistoryReqsDiscarded": f3NCIHistoryReqsDiscarded,
       "f3NCIHistoryAvgTPS": f3NCIHistoryAvgTPS,
       "f3NCIHistoryMaxTPS": f3NCIHistoryMaxTPS,
       "f3NCIThresholdTable": f3NCIThresholdTable,
       "f3NCIThresholdEntry": f3NCIThresholdEntry,
       "f3NCIThresholdIndex": f3NCIThresholdIndex,
       "f3NCIThresholdInterval": f3NCIThresholdInterval,
       "f3NCIThresholdVariable": f3NCIThresholdVariable,
       "f3NCIThresholdValueLo": f3NCIThresholdValueLo,
       "f3NCIThresholdValueHi": f3NCIThresholdValueHi,
       "f3NCIThresholdMonValue": f3NCIThresholdMonValue,
       "f3NtpAccPortFlowPointStatsTable": f3NtpAccPortFlowPointStatsTable,
       "f3NtpAccPortFlowPointStatsEntry": f3NtpAccPortFlowPointStatsEntry,
       "f3NtpAccPortFlowPointStatsIndex": f3NtpAccPortFlowPointStatsIndex,
       "f3NtpAccPortFlowPointStatsIntervalType": f3NtpAccPortFlowPointStatsIntervalType,
       "f3NtpAccPortFlowPointStatsValid": f3NtpAccPortFlowPointStatsValid,
       "f3NtpAccPortFlowPointStatsAction": f3NtpAccPortFlowPointStatsAction,
       "f3NtpAccPortFlowPointStatsRequestsDropped": f3NtpAccPortFlowPointStatsRequestsDropped,
       "f3NtpAccPortFlowPointStatsRequestsReceived": f3NtpAccPortFlowPointStatsRequestsReceived,
       "f3NtpAccPortFlowPointStatsResponsesTransmitted": f3NtpAccPortFlowPointStatsResponsesTransmitted,
       "f3NtpAccPortFlowPointHistoryTable": f3NtpAccPortFlowPointHistoryTable,
       "f3NtpAccPortFlowPointHistoryEntry": f3NtpAccPortFlowPointHistoryEntry,
       "f3NtpAccPortFlowPointHistoryIndex": f3NtpAccPortFlowPointHistoryIndex,
       "f3NtpAccPortFlowPointHistoryTime": f3NtpAccPortFlowPointHistoryTime,
       "f3NtpAccPortFlowPointHistoryValid": f3NtpAccPortFlowPointHistoryValid,
       "f3NtpAccPortFlowPointHistoryAction": f3NtpAccPortFlowPointHistoryAction,
       "f3NtpAccPortFlowPointHistoryRequestsDropped": f3NtpAccPortFlowPointHistoryRequestsDropped,
       "f3NtpAccPortFlowPointHistoryRequestsReceived": f3NtpAccPortFlowPointHistoryRequestsReceived,
       "f3NtpAccPortFlowPointHistoryResponsesTransmitted": f3NtpAccPortFlowPointHistoryResponsesTransmitted,
       "f3NtpAccPortFlowPointThresholdTable": f3NtpAccPortFlowPointThresholdTable,
       "f3NtpAccPortFlowPointThresholdEntry": f3NtpAccPortFlowPointThresholdEntry,
       "f3NtpAccPortFlowPointThresholdIndex": f3NtpAccPortFlowPointThresholdIndex,
       "f3NtpAccPortFlowPointThresholdInterval": f3NtpAccPortFlowPointThresholdInterval,
       "f3NtpAccPortFlowPointThresholdVariable": f3NtpAccPortFlowPointThresholdVariable,
       "f3NtpAccPortFlowPointThresholdValueLo": f3NtpAccPortFlowPointThresholdValueLo,
       "f3NtpAccPortFlowPointThresholdValueHi": f3NtpAccPortFlowPointThresholdValueHi,
       "f3NtpAccPortFlowPointThresholdMonValue": f3NtpAccPortFlowPointThresholdMonValue,
       "f3NtpNetPortFlowPointStatsTable": f3NtpNetPortFlowPointStatsTable,
       "f3NtpNetPortFlowPointStatsEntry": f3NtpNetPortFlowPointStatsEntry,
       "f3NtpNetPortFlowPointStatsIndex": f3NtpNetPortFlowPointStatsIndex,
       "f3NtpNetPortFlowPointStatsIntervalType": f3NtpNetPortFlowPointStatsIntervalType,
       "f3NtpNetPortFlowPointStatsValid": f3NtpNetPortFlowPointStatsValid,
       "f3NtpNetPortFlowPointStatsAction": f3NtpNetPortFlowPointStatsAction,
       "f3NtpNetPortFlowPointStatsRequestsDropped": f3NtpNetPortFlowPointStatsRequestsDropped,
       "f3NtpNetPortFlowPointStatsRequestsReceived": f3NtpNetPortFlowPointStatsRequestsReceived,
       "f3NtpNetPortFlowPointStatsResponsesTransmitted": f3NtpNetPortFlowPointStatsResponsesTransmitted,
       "f3NtpNetPortFlowPointHistoryTable": f3NtpNetPortFlowPointHistoryTable,
       "f3NtpNetPortFlowPointHistoryEntry": f3NtpNetPortFlowPointHistoryEntry,
       "f3NtpNetPortFlowPointHistoryIndex": f3NtpNetPortFlowPointHistoryIndex,
       "f3NtpNetPortFlowPointHistoryTime": f3NtpNetPortFlowPointHistoryTime,
       "f3NtpNetPortFlowPointHistoryValid": f3NtpNetPortFlowPointHistoryValid,
       "f3NtpNetPortFlowPointHistoryAction": f3NtpNetPortFlowPointHistoryAction,
       "f3NtpNetPortFlowPointHistoryRequestsDropped": f3NtpNetPortFlowPointHistoryRequestsDropped,
       "f3NtpNetPortFlowPointHistoryRequestsReceived": f3NtpNetPortFlowPointHistoryRequestsReceived,
       "f3NtpNetPortFlowPointHistoryResponsesTransmitted": f3NtpNetPortFlowPointHistoryResponsesTransmitted,
       "f3NtpNetPortFlowPointThresholdTable": f3NtpNetPortFlowPointThresholdTable,
       "f3NtpNetPortFlowPointThresholdEntry": f3NtpNetPortFlowPointThresholdEntry,
       "f3NtpNetPortFlowPointThresholdIndex": f3NtpNetPortFlowPointThresholdIndex,
       "f3NtpNetPortFlowPointThresholdInterval": f3NtpNetPortFlowPointThresholdInterval,
       "f3NtpNetPortFlowPointThresholdVariable": f3NtpNetPortFlowPointThresholdVariable,
       "f3NtpNetPortFlowPointThresholdValueLo": f3NtpNetPortFlowPointThresholdValueLo,
       "f3NtpNetPortFlowPointThresholdValueHi": f3NtpNetPortFlowPointThresholdValueHi,
       "f3NtpNetPortFlowPointThresholdMonValue": f3NtpNetPortFlowPointThresholdMonValue,
       "f3NtpTrackedClientStatsTable": f3NtpTrackedClientStatsTable,
       "f3NtpTrackedClientStatsEntry": f3NtpTrackedClientStatsEntry,
       "f3NtpTrackedClientStatsIndex": f3NtpTrackedClientStatsIndex,
       "f3NtpTrackedClientStatsClientIndex": f3NtpTrackedClientStatsClientIndex,
       "f3NtpTrackedClientStatsIntervalType": f3NtpTrackedClientStatsIntervalType,
       "f3NtpTrackedClientStatsValid": f3NtpTrackedClientStatsValid,
       "f3NtpTrackedClientStatsAction": f3NtpTrackedClientStatsAction,
       "f3NtpTrackedClientStatsResponsesTransmitted": f3NtpTrackedClientStatsResponsesTransmitted,
       "f3NtpTrackedClientStatsRequestsReceived": f3NtpTrackedClientStatsRequestsReceived,
       "f3NtpTrackedClientHistoryTable": f3NtpTrackedClientHistoryTable,
       "f3NtpTrackedClientHistoryEntry": f3NtpTrackedClientHistoryEntry,
       "f3NtpTrackedClientHistoryIndex": f3NtpTrackedClientHistoryIndex,
       "f3NtpTrackedClientHistoryTime": f3NtpTrackedClientHistoryTime,
       "f3NtpTrackedClientHistoryValid": f3NtpTrackedClientHistoryValid,
       "f3NtpTrackedClientHistoryAction": f3NtpTrackedClientHistoryAction,
       "f3NtpTrackedClientHistoryResponsesTransmitted": f3NtpTrackedClientHistoryResponsesTransmitted,
       "f3NtpTrackedClientHistoryRequestsReceived": f3NtpTrackedClientHistoryRequestsReceived,
       "f3NtpTrackedClientThresholdTable": f3NtpTrackedClientThresholdTable,
       "f3NtpTrackedClientThresholdEntry": f3NtpTrackedClientThresholdEntry,
       "f3NtpTrackedClientThresholdIndex": f3NtpTrackedClientThresholdIndex,
       "f3NtpTrackedClientThresholdInterval": f3NtpTrackedClientThresholdInterval,
       "f3NtpTrackedClientThresholdVariable": f3NtpTrackedClientThresholdVariable,
       "f3NtpTrackedClientThresholdValueLo": f3NtpTrackedClientThresholdValueLo,
       "f3NtpTrackedClientThresholdValueHi": f3NtpTrackedClientThresholdValueHi,
       "f3NtpTrackedClientThresholdMonValue": f3NtpTrackedClientThresholdMonValue,
       "f3NtpPerformanceNotifications": f3NtpPerformanceNotifications,
       "f3NtpTrackedClientCrossingAlert": f3NtpTrackedClientCrossingAlert}
)
