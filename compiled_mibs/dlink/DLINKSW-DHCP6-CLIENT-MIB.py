# SNMP MIB module (DLINKSW-DHCP6-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP6-CLIENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:54 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDhcp6ClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222)
)
if mibBuilder.loadTexts:
    dlinkSwDhcp6ClientMIB.setRevisions(
        ("2013-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDhcp6ClientNotifications_ObjectIdentity = ObjectIdentity
dDhcp6ClientNotifications = _DDhcp6ClientNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 0)
)
_DDhcp6ClientObjects_ObjectIdentity = ObjectIdentity
dDhcp6ClientObjects = _DDhcp6ClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1)
)
_DDhcp6ClientGeneral_ObjectIdentity = ObjectIdentity
dDhcp6ClientGeneral = _DDhcp6ClientGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 1)
)
_DDhcp6ClientDuid_Type = OctetString
_DDhcp6ClientDuid_Object = MibScalar
dDhcp6ClientDuid = _DDhcp6ClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 1, 1),
    _DDhcp6ClientDuid_Type()
)
dDhcp6ClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6ClientDuid.setStatus("current")
_Dhcp6ClientRestartIf_Type = InterfaceIndexOrZero
_Dhcp6ClientRestartIf_Object = MibScalar
dhcp6ClientRestartIf = _Dhcp6ClientRestartIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 1, 2),
    _Dhcp6ClientRestartIf_Type()
)
dhcp6ClientRestartIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6ClientRestartIf.setStatus("current")
_DDhcp6ClientIfObjects_ObjectIdentity = ObjectIdentity
dDhcp6ClientIfObjects = _DDhcp6ClientIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2)
)
_DDhcp6CIfTable_Object = MibTable
dDhcp6CIfTable = _DDhcp6CIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dDhcp6CIfTable.setStatus("current")
_DDhcp6CIfEntry_Object = MibTableRow
dDhcp6CIfEntry = _DDhcp6CIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 1, 1)
)
dDhcp6CIfEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6CIfEntry.setStatus("current")
_DDhcp6CIfIndex_Type = InterfaceIndex
_DDhcp6CIfIndex_Object = MibTableColumn
dDhcp6CIfIndex = _DDhcp6CIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 1, 1, 1),
    _DDhcp6CIfIndex_Type()
)
dDhcp6CIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfIndex.setStatus("current")


class _DDhcp6CIfAcquireAddrEnabled_Type(TruthValue):
    """Custom type dDhcp6CIfAcquireAddrEnabled based on TruthValue"""
    defaultValue = 2


_DDhcp6CIfAcquireAddrEnabled_Type.__name__ = "TruthValue"
_DDhcp6CIfAcquireAddrEnabled_Object = MibTableColumn
dDhcp6CIfAcquireAddrEnabled = _DDhcp6CIfAcquireAddrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 1, 1, 2),
    _DDhcp6CIfAcquireAddrEnabled_Type()
)
dDhcp6CIfAcquireAddrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquireAddrEnabled.setStatus("current")


class _DDhcp6CIfAcqAddrRapidCommit_Type(TruthValue):
    """Custom type dDhcp6CIfAcqAddrRapidCommit based on TruthValue"""
    defaultValue = 2


_DDhcp6CIfAcqAddrRapidCommit_Type.__name__ = "TruthValue"
_DDhcp6CIfAcqAddrRapidCommit_Object = MibTableColumn
dDhcp6CIfAcqAddrRapidCommit = _DDhcp6CIfAcqAddrRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 1, 1, 3),
    _DDhcp6CIfAcqAddrRapidCommit_Type()
)
dDhcp6CIfAcqAddrRapidCommit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfAcqAddrRapidCommit.setStatus("current")


class _DDhcp6CIfMinRefresh_Type(Unsigned32):
    """Custom type dDhcp6CIfMinRefresh based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4294967295),
    )


_DDhcp6CIfMinRefresh_Type.__name__ = "Unsigned32"
_DDhcp6CIfMinRefresh_Object = MibTableColumn
dDhcp6CIfMinRefresh = _DDhcp6CIfMinRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 1, 1, 4),
    _DDhcp6CIfMinRefresh_Type()
)
dDhcp6CIfMinRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfMinRefresh.setStatus("current")
_DDhcp6CIfRowStatus_Type = RowStatus
_DDhcp6CIfRowStatus_Object = MibTableColumn
dDhcp6CIfRowStatus = _DDhcp6CIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 1, 1, 5),
    _DDhcp6CIfRowStatus_Type()
)
dDhcp6CIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfRowStatus.setStatus("current")
_DDhcp6CIfPrefixDeleCfgTable_Object = MibTable
dDhcp6CIfPrefixDeleCfgTable = _DDhcp6CIfPrefixDeleCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixDeleCfgTable.setStatus("current")
_DDhcp6CIfPrefixDeleCfgEntry_Object = MibTableRow
dDhcp6CIfPrefixDeleCfgEntry = _DDhcp6CIfPrefixDeleCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3, 1)
)
dDhcp6CIfPrefixDeleCfgEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPdCfgIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixDeleCfgEntry.setStatus("current")
_DDhcp6CIfPdCfgIfIndex_Type = InterfaceIndex
_DDhcp6CIfPdCfgIfIndex_Object = MibTableColumn
dDhcp6CIfPdCfgIfIndex = _DDhcp6CIfPdCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3, 1, 1),
    _DDhcp6CIfPdCfgIfIndex_Type()
)
dDhcp6CIfPdCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfPdCfgIfIndex.setStatus("current")


class _DDhcp6CIfPdCfgPrefixName_Type(DisplayString):
    """Custom type dDhcp6CIfPdCfgPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcp6CIfPdCfgPrefixName_Type.__name__ = "DisplayString"
_DDhcp6CIfPdCfgPrefixName_Object = MibTableColumn
dDhcp6CIfPdCfgPrefixName = _DDhcp6CIfPdCfgPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3, 1, 2),
    _DDhcp6CIfPdCfgPrefixName_Type()
)
dDhcp6CIfPdCfgPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfPdCfgPrefixName.setStatus("current")
_DDhcp6CIfPdCfgHintAddr_Type = InetAddressIPv6
_DDhcp6CIfPdCfgHintAddr_Object = MibTableColumn
dDhcp6CIfPdCfgHintAddr = _DDhcp6CIfPdCfgHintAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3, 1, 3),
    _DDhcp6CIfPdCfgHintAddr_Type()
)
dDhcp6CIfPdCfgHintAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfPdCfgHintAddr.setStatus("current")
_DDhcp6CIfPdCfgHintLen_Type = InetAddressPrefixLength
_DDhcp6CIfPdCfgHintLen_Object = MibTableColumn
dDhcp6CIfPdCfgHintLen = _DDhcp6CIfPdCfgHintLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3, 1, 4),
    _DDhcp6CIfPdCfgHintLen_Type()
)
dDhcp6CIfPdCfgHintLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfPdCfgHintLen.setStatus("current")
_DDhcp6CIfPdCfgRapidCommit_Type = TruthValue
_DDhcp6CIfPdCfgRapidCommit_Object = MibTableColumn
dDhcp6CIfPdCfgRapidCommit = _DDhcp6CIfPdCfgRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3, 1, 5),
    _DDhcp6CIfPdCfgRapidCommit_Type()
)
dDhcp6CIfPdCfgRapidCommit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfPdCfgRapidCommit.setStatus("current")
_DDhcp6CIfPdCfgRowStatus_Type = RowStatus
_DDhcp6CIfPdCfgRowStatus_Object = MibTableColumn
dDhcp6CIfPdCfgRowStatus = _DDhcp6CIfPdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 2, 3, 1, 6),
    _DDhcp6CIfPdCfgRowStatus_Type()
)
dDhcp6CIfPdCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6CIfPdCfgRowStatus.setStatus("current")
_DDhcp6ClientStatusObjects_ObjectIdentity = ObjectIdentity
dDhcp6ClientStatusObjects = _DDhcp6ClientStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3)
)
_DDhcp6CIfStateTable_Object = MibTable
dDhcp6CIfStateTable = _DDhcp6CIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dDhcp6CIfStateTable.setStatus("current")
_DDhcp6CIfStateEntry_Object = MibTableRow
dDhcp6CIfStateEntry = _DDhcp6CIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 1, 1)
)
dDhcp6CIfStateEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfStateIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6CIfStateEntry.setStatus("current")
_DDhcp6CIfStateIfIndex_Type = InterfaceIndex
_DDhcp6CIfStateIfIndex_Object = MibTableColumn
dDhcp6CIfStateIfIndex = _DDhcp6CIfStateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 1, 1, 1),
    _DDhcp6CIfStateIfIndex_Type()
)
dDhcp6CIfStateIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfStateIfIndex.setStatus("current")


class _DDhcp6CIfStateCode_Type(Integer32):
    """Custom type dDhcp6CIfStateCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("init", 1),
          ("request", 2),
          ("release", 3),
          ("active", 4),
          ("renew", 5),
          ("rebind", 6))
    )


_DDhcp6CIfStateCode_Type.__name__ = "Integer32"
_DDhcp6CIfStateCode_Object = MibTableColumn
dDhcp6CIfStateCode = _DDhcp6CIfStateCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 1, 1, 2),
    _DDhcp6CIfStateCode_Type()
)
dDhcp6CIfStateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfStateCode.setStatus("current")
_DDhcp6CIfStatusEventExpire_Type = Unsigned32
_DDhcp6CIfStatusEventExpire_Object = MibTableColumn
dDhcp6CIfStatusEventExpire = _DDhcp6CIfStatusEventExpire_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 1, 1, 3),
    _DDhcp6CIfStatusEventExpire_Type()
)
dDhcp6CIfStatusEventExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfStatusEventExpire.setStatus("current")
_DDhcp6CIfAcquiredIaTable_Object = MibTable
dDhcp6CIfAcquiredIaTable = _DDhcp6CIfAcquiredIaTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaTable.setStatus("current")
_DDhcp6CIfAcquiredIaEntry_Object = MibTableRow
dDhcp6CIfAcquiredIaEntry = _DDhcp6CIfAcquiredIaEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1)
)
dDhcp6CIfAcquiredIaEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaType"),
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaId"),
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaEntry.setStatus("current")


class _DDhcp6CIfAcquiredIaType_Type(Integer32):
    """Custom type dDhcp6CIfAcquiredIaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("iapd", 1),
          ("iana", 2))
    )


_DDhcp6CIfAcquiredIaType_Type.__name__ = "Integer32"
_DDhcp6CIfAcquiredIaType_Object = MibTableColumn
dDhcp6CIfAcquiredIaType = _DDhcp6CIfAcquiredIaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 1),
    _DDhcp6CIfAcquiredIaType_Type()
)
dDhcp6CIfAcquiredIaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaType.setStatus("current")


class _DDhcp6CIfAcquiredIaId_Type(Unsigned32):
    """Custom type dDhcp6CIfAcquiredIaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DDhcp6CIfAcquiredIaId_Type.__name__ = "Unsigned32"
_DDhcp6CIfAcquiredIaId_Object = MibTableColumn
dDhcp6CIfAcquiredIaId = _DDhcp6CIfAcquiredIaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 2),
    _DDhcp6CIfAcquiredIaId_Type()
)
dDhcp6CIfAcquiredIaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaId.setStatus("current")
_DDhcp6CIfAcquiredIaIfIndex_Type = InterfaceIndex
_DDhcp6CIfAcquiredIaIfIndex_Object = MibTableColumn
dDhcp6CIfAcquiredIaIfIndex = _DDhcp6CIfAcquiredIaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 3),
    _DDhcp6CIfAcquiredIaIfIndex_Type()
)
dDhcp6CIfAcquiredIaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaIfIndex.setStatus("current")
_DDhcp6CIfAcquiredIaServerAddr_Type = InetAddressIPv6
_DDhcp6CIfAcquiredIaServerAddr_Object = MibTableColumn
dDhcp6CIfAcquiredIaServerAddr = _DDhcp6CIfAcquiredIaServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 4),
    _DDhcp6CIfAcquiredIaServerAddr_Type()
)
dDhcp6CIfAcquiredIaServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaServerAddr.setStatus("current")
_DDhcp6CIfAcquiredIaServerDUID_Type = OctetString
_DDhcp6CIfAcquiredIaServerDUID_Object = MibTableColumn
dDhcp6CIfAcquiredIaServerDUID = _DDhcp6CIfAcquiredIaServerDUID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 5),
    _DDhcp6CIfAcquiredIaServerDUID_Type()
)
dDhcp6CIfAcquiredIaServerDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaServerDUID.setStatus("current")


class _DDhcp6CIfAcquiredIaServerPref_Type(Unsigned32):
    """Custom type dDhcp6CIfAcquiredIaServerPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DDhcp6CIfAcquiredIaServerPref_Type.__name__ = "Unsigned32"
_DDhcp6CIfAcquiredIaServerPref_Object = MibTableColumn
dDhcp6CIfAcquiredIaServerPref = _DDhcp6CIfAcquiredIaServerPref_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 6),
    _DDhcp6CIfAcquiredIaServerPref_Type()
)
dDhcp6CIfAcquiredIaServerPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaServerPref.setStatus("current")
_DDhcp6CIfAcquiredIaT1_Type = Unsigned32
_DDhcp6CIfAcquiredIaT1_Object = MibTableColumn
dDhcp6CIfAcquiredIaT1 = _DDhcp6CIfAcquiredIaT1_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 7),
    _DDhcp6CIfAcquiredIaT1_Type()
)
dDhcp6CIfAcquiredIaT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaT1.setStatus("current")
_DDhcp6CIfAcquiredIaT2_Type = Unsigned32
_DDhcp6CIfAcquiredIaT2_Object = MibTableColumn
dDhcp6CIfAcquiredIaT2 = _DDhcp6CIfAcquiredIaT2_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 8),
    _DDhcp6CIfAcquiredIaT2_Type()
)
dDhcp6CIfAcquiredIaT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaT2.setStatus("current")
_DDhcp6CIfAcquiredIaExpireTime_Type = Unsigned32
_DDhcp6CIfAcquiredIaExpireTime_Object = MibTableColumn
dDhcp6CIfAcquiredIaExpireTime = _DDhcp6CIfAcquiredIaExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 2, 1, 9),
    _DDhcp6CIfAcquiredIaExpireTime_Type()
)
dDhcp6CIfAcquiredIaExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAcquiredIaExpireTime.setStatus("current")
_DDhcp6CIfAddrTable_Object = MibTable
dDhcp6CIfAddrTable = _DDhcp6CIfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dDhcp6CIfAddrTable.setStatus("current")
_DDhcp6CIfAddrEntry_Object = MibTableRow
dDhcp6CIfAddrEntry = _DDhcp6CIfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 3, 1)
)
dDhcp6CIfAddrEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaId"),
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAddrInetAddr"),
)
if mibBuilder.loadTexts:
    dDhcp6CIfAddrEntry.setStatus("current")
_DDhcp6CIfAddrInetAddr_Type = InetAddressIPv6
_DDhcp6CIfAddrInetAddr_Object = MibTableColumn
dDhcp6CIfAddrInetAddr = _DDhcp6CIfAddrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 3, 1, 1),
    _DDhcp6CIfAddrInetAddr_Type()
)
dDhcp6CIfAddrInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfAddrInetAddr.setStatus("current")
_DDhcp6CIfAddrPreferLifeTime_Type = Unsigned32
_DDhcp6CIfAddrPreferLifeTime_Object = MibTableColumn
dDhcp6CIfAddrPreferLifeTime = _DDhcp6CIfAddrPreferLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 3, 1, 2),
    _DDhcp6CIfAddrPreferLifeTime_Type()
)
dDhcp6CIfAddrPreferLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAddrPreferLifeTime.setStatus("current")
_DDhcp6CIfAddrValidLifeTime_Type = Unsigned32
_DDhcp6CIfAddrValidLifeTime_Object = MibTableColumn
dDhcp6CIfAddrValidLifeTime = _DDhcp6CIfAddrValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 3, 1, 3),
    _DDhcp6CIfAddrValidLifeTime_Type()
)
dDhcp6CIfAddrValidLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAddrValidLifeTime.setStatus("current")
_DDhcp6CIfAddrExpireTime_Type = Unsigned32
_DDhcp6CIfAddrExpireTime_Object = MibTableColumn
dDhcp6CIfAddrExpireTime = _DDhcp6CIfAddrExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 3, 1, 4),
    _DDhcp6CIfAddrExpireTime_Type()
)
dDhcp6CIfAddrExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfAddrExpireTime.setStatus("current")
_DDhcp6CIfPrefixTable_Object = MibTable
dDhcp6CIfPrefixTable = _DDhcp6CIfPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixTable.setStatus("current")
_DDhcp6CIfPrefixEntry_Object = MibTableRow
dDhcp6CIfPrefixEntry = _DDhcp6CIfPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 4, 1)
)
dDhcp6CIfPrefixEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaId"),
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPrefixAddr"),
    (0, "DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPrefixAddrLen"),
)
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixEntry.setStatus("current")
_DDhcp6CIfPrefixAddr_Type = InetAddressIPv6
_DDhcp6CIfPrefixAddr_Object = MibTableColumn
dDhcp6CIfPrefixAddr = _DDhcp6CIfPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 4, 1, 1),
    _DDhcp6CIfPrefixAddr_Type()
)
dDhcp6CIfPrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixAddr.setStatus("current")
_DDhcp6CIfPrefixAddrLen_Type = InetAddressPrefixLength
_DDhcp6CIfPrefixAddrLen_Object = MibTableColumn
dDhcp6CIfPrefixAddrLen = _DDhcp6CIfPrefixAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 4, 1, 2),
    _DDhcp6CIfPrefixAddrLen_Type()
)
dDhcp6CIfPrefixAddrLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixAddrLen.setStatus("current")
_DDhcp6CIfPrefixPreferLifeTime_Type = Unsigned32
_DDhcp6CIfPrefixPreferLifeTime_Object = MibTableColumn
dDhcp6CIfPrefixPreferLifeTime = _DDhcp6CIfPrefixPreferLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 4, 1, 3),
    _DDhcp6CIfPrefixPreferLifeTime_Type()
)
dDhcp6CIfPrefixPreferLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixPreferLifeTime.setStatus("current")
_DDhcp6CIfPrefixValidLifeTime_Type = Unsigned32
_DDhcp6CIfPrefixValidLifeTime_Object = MibTableColumn
dDhcp6CIfPrefixValidLifeTime = _DDhcp6CIfPrefixValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 4, 1, 4),
    _DDhcp6CIfPrefixValidLifeTime_Type()
)
dDhcp6CIfPrefixValidLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixValidLifeTime.setStatus("current")
_DDhcp6CIfPrefixExpireTime_Type = Unsigned32
_DDhcp6CIfPrefixExpireTime_Object = MibTableColumn
dDhcp6CIfPrefixExpireTime = _DDhcp6CIfPrefixExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 1, 3, 4, 1, 5),
    _DDhcp6CIfPrefixExpireTime_Type()
)
dDhcp6CIfPrefixExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6CIfPrefixExpireTime.setStatus("current")
_DDhcp6ClientConformance_ObjectIdentity = ObjectIdentity
dDhcp6ClientConformance = _DDhcp6ClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2)
)
_DDhcp6ClientCompliances_ObjectIdentity = ObjectIdentity
dDhcp6ClientCompliances = _DDhcp6ClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2, 1)
)
_DDhcp6ClientGroups_ObjectIdentity = ObjectIdentity
dDhcp6ClientGroups = _DDhcp6ClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2, 1, 2)
)

# Managed Objects groups

dDhcp6CBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2, 1, 2, 1)
)
dDhcp6CBasicGroup.setObjects(
      *(("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6ClientDuid"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dhcp6ClientRestartIf"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquireAddrEnabled"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcqAddrRapidCommit"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfMinRefresh"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6CBasicGroup.setStatus("current")

dDhcp6CBasicStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2, 1, 2, 2)
)
dDhcp6CBasicStatusGroup.setObjects(
      *(("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfStateCode"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfStatusEventExpire"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaServerAddr"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaServerDUID"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaServerPref"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaT1"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaT2"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAcquiredIaExpireTime"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAddrPreferLifeTime"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAddrValidLifeTime"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfAddrExpireTime"))
)
if mibBuilder.loadTexts:
    dDhcp6CBasicStatusGroup.setStatus("current")

dDhcp6CPrefixDelegationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2, 1, 2, 3)
)
dDhcp6CPrefixDelegationGroup.setObjects(
      *(("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPdCfgPrefixName"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPdCfgHintAddr"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPdCfgHintLen"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPdCfgRapidCommit"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPdCfgRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6CPrefixDelegationGroup.setStatus("current")

dDhcp6CPrefixDelegStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2, 1, 2, 4)
)
dDhcp6CPrefixDelegStatusGroup.setObjects(
      *(("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPrefixPreferLifeTime"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPrefixValidLifeTime"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CIfPrefixExpireTime"))
)
if mibBuilder.loadTexts:
    dDhcp6CPrefixDelegStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDhcp6ClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 222, 2, 1, 1)
)
dDhcp6ClientCompliance.setObjects(
      *(("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CBasicGroup"),
        ("DLINKSW-DHCP6-CLIENT-MIB", "dDhcp6CBasicStatusGroup"))
)
if mibBuilder.loadTexts:
    dDhcp6ClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP6-CLIENT-MIB",
    **{"dlinkSwDhcp6ClientMIB": dlinkSwDhcp6ClientMIB,
       "dDhcp6ClientNotifications": dDhcp6ClientNotifications,
       "dDhcp6ClientObjects": dDhcp6ClientObjects,
       "dDhcp6ClientGeneral": dDhcp6ClientGeneral,
       "dDhcp6ClientDuid": dDhcp6ClientDuid,
       "dhcp6ClientRestartIf": dhcp6ClientRestartIf,
       "dDhcp6ClientIfObjects": dDhcp6ClientIfObjects,
       "dDhcp6CIfTable": dDhcp6CIfTable,
       "dDhcp6CIfEntry": dDhcp6CIfEntry,
       "dDhcp6CIfIndex": dDhcp6CIfIndex,
       "dDhcp6CIfAcquireAddrEnabled": dDhcp6CIfAcquireAddrEnabled,
       "dDhcp6CIfAcqAddrRapidCommit": dDhcp6CIfAcqAddrRapidCommit,
       "dDhcp6CIfMinRefresh": dDhcp6CIfMinRefresh,
       "dDhcp6CIfRowStatus": dDhcp6CIfRowStatus,
       "dDhcp6CIfPrefixDeleCfgTable": dDhcp6CIfPrefixDeleCfgTable,
       "dDhcp6CIfPrefixDeleCfgEntry": dDhcp6CIfPrefixDeleCfgEntry,
       "dDhcp6CIfPdCfgIfIndex": dDhcp6CIfPdCfgIfIndex,
       "dDhcp6CIfPdCfgPrefixName": dDhcp6CIfPdCfgPrefixName,
       "dDhcp6CIfPdCfgHintAddr": dDhcp6CIfPdCfgHintAddr,
       "dDhcp6CIfPdCfgHintLen": dDhcp6CIfPdCfgHintLen,
       "dDhcp6CIfPdCfgRapidCommit": dDhcp6CIfPdCfgRapidCommit,
       "dDhcp6CIfPdCfgRowStatus": dDhcp6CIfPdCfgRowStatus,
       "dDhcp6ClientStatusObjects": dDhcp6ClientStatusObjects,
       "dDhcp6CIfStateTable": dDhcp6CIfStateTable,
       "dDhcp6CIfStateEntry": dDhcp6CIfStateEntry,
       "dDhcp6CIfStateIfIndex": dDhcp6CIfStateIfIndex,
       "dDhcp6CIfStateCode": dDhcp6CIfStateCode,
       "dDhcp6CIfStatusEventExpire": dDhcp6CIfStatusEventExpire,
       "dDhcp6CIfAcquiredIaTable": dDhcp6CIfAcquiredIaTable,
       "dDhcp6CIfAcquiredIaEntry": dDhcp6CIfAcquiredIaEntry,
       "dDhcp6CIfAcquiredIaType": dDhcp6CIfAcquiredIaType,
       "dDhcp6CIfAcquiredIaId": dDhcp6CIfAcquiredIaId,
       "dDhcp6CIfAcquiredIaIfIndex": dDhcp6CIfAcquiredIaIfIndex,
       "dDhcp6CIfAcquiredIaServerAddr": dDhcp6CIfAcquiredIaServerAddr,
       "dDhcp6CIfAcquiredIaServerDUID": dDhcp6CIfAcquiredIaServerDUID,
       "dDhcp6CIfAcquiredIaServerPref": dDhcp6CIfAcquiredIaServerPref,
       "dDhcp6CIfAcquiredIaT1": dDhcp6CIfAcquiredIaT1,
       "dDhcp6CIfAcquiredIaT2": dDhcp6CIfAcquiredIaT2,
       "dDhcp6CIfAcquiredIaExpireTime": dDhcp6CIfAcquiredIaExpireTime,
       "dDhcp6CIfAddrTable": dDhcp6CIfAddrTable,
       "dDhcp6CIfAddrEntry": dDhcp6CIfAddrEntry,
       "dDhcp6CIfAddrInetAddr": dDhcp6CIfAddrInetAddr,
       "dDhcp6CIfAddrPreferLifeTime": dDhcp6CIfAddrPreferLifeTime,
       "dDhcp6CIfAddrValidLifeTime": dDhcp6CIfAddrValidLifeTime,
       "dDhcp6CIfAddrExpireTime": dDhcp6CIfAddrExpireTime,
       "dDhcp6CIfPrefixTable": dDhcp6CIfPrefixTable,
       "dDhcp6CIfPrefixEntry": dDhcp6CIfPrefixEntry,
       "dDhcp6CIfPrefixAddr": dDhcp6CIfPrefixAddr,
       "dDhcp6CIfPrefixAddrLen": dDhcp6CIfPrefixAddrLen,
       "dDhcp6CIfPrefixPreferLifeTime": dDhcp6CIfPrefixPreferLifeTime,
       "dDhcp6CIfPrefixValidLifeTime": dDhcp6CIfPrefixValidLifeTime,
       "dDhcp6CIfPrefixExpireTime": dDhcp6CIfPrefixExpireTime,
       "dDhcp6ClientConformance": dDhcp6ClientConformance,
       "dDhcp6ClientCompliances": dDhcp6ClientCompliances,
       "dDhcp6ClientCompliance": dDhcp6ClientCompliance,
       "dDhcp6ClientGroups": dDhcp6ClientGroups,
       "dDhcp6CBasicGroup": dDhcp6CBasicGroup,
       "dDhcp6CBasicStatusGroup": dDhcp6CBasicStatusGroup,
       "dDhcp6CPrefixDelegationGroup": dDhcp6CPrefixDelegationGroup,
       "dDhcp6CPrefixDelegStatusGroup": dDhcp6CPrefixDelegStatusGroup}
)
