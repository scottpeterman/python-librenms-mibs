# SNMP MIB module (SLE-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-NETWORK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:53 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleNetwork = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11)
)
if mibBuilder.loadTexts:
    sleNetwork.setRevisions(
        ("2004-12-10 16:32",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleNetInterface_ObjectIdentity = ObjectIdentity
sleNetInterface = _SleNetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1)
)
_SleNetIfTable_Object = MibTable
sleNetIfTable = _SleNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1)
)
if mibBuilder.loadTexts:
    sleNetIfTable.setStatus("current")
_SleNetIfEntry_Object = MibTableRow
sleNetIfEntry = _SleNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1)
)
sleNetIfEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
)
if mibBuilder.loadTexts:
    sleNetIfEntry.setStatus("current")


class _SleNetIfIndex_Type(Integer32):
    """Custom type sleNetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11023),
    )


_SleNetIfIndex_Type.__name__ = "Integer32"
_SleNetIfIndex_Object = MibTableColumn
sleNetIfIndex = _SleNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 1),
    _SleNetIfIndex_Type()
)
sleNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIndex.setStatus("current")


class _SleNetIfName_Type(OctetString):
    """Custom type sleNetIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SleNetIfName_Type.__name__ = "OctetString"
_SleNetIfName_Object = MibTableColumn
sleNetIfName = _SleNetIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 2),
    _SleNetIfName_Type()
)
sleNetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfName.setStatus("current")


class _SleNetIfDescription_Type(OctetString):
    """Custom type sleNetIfDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SleNetIfDescription_Type.__name__ = "OctetString"
_SleNetIfDescription_Object = MibTableColumn
sleNetIfDescription = _SleNetIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 3),
    _SleNetIfDescription_Type()
)
sleNetIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfDescription.setStatus("current")
_SleNetIfTableIndex_Type = InterfaceIndex
_SleNetIfTableIndex_Object = MibTableColumn
sleNetIfTableIndex = _SleNetIfTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 4),
    _SleNetIfTableIndex_Type()
)
sleNetIfTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfTableIndex.setStatus("current")


class _SleNetIfRegState_Type(Integer32):
    """Custom type sleNetIfRegState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unregistered", 0),
          ("registered", 1))
    )


_SleNetIfRegState_Type.__name__ = "Integer32"
_SleNetIfRegState_Object = MibTableColumn
sleNetIfRegState = _SleNetIfRegState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 5),
    _SleNetIfRegState_Type()
)
sleNetIfRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfRegState.setStatus("current")


class _SleNetIfAdminState_Type(Integer32):
    """Custom type sleNetIfAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_SleNetIfAdminState_Type.__name__ = "Integer32"
_SleNetIfAdminState_Object = MibTableColumn
sleNetIfAdminState = _SleNetIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 6),
    _SleNetIfAdminState_Type()
)
sleNetIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfAdminState.setStatus("current")


class _SleNetIfOperState_Type(Integer32):
    """Custom type sleNetIfOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_SleNetIfOperState_Type.__name__ = "Integer32"
_SleNetIfOperState_Object = MibTableColumn
sleNetIfOperState = _SleNetIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 7),
    _SleNetIfOperState_Type()
)
sleNetIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfOperState.setStatus("current")


class _SleNetIfMulticast_Type(Integer32):
    """Custom type sleNetIfMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfMulticast_Type.__name__ = "Integer32"
_SleNetIfMulticast_Object = MibTableColumn
sleNetIfMulticast = _SleNetIfMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 8),
    _SleNetIfMulticast_Type()
)
sleNetIfMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfMulticast.setStatus("current")


class _SleNetIfMtu_Type(Integer32):
    """Custom type sleNetIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 17940),
    )


_SleNetIfMtu_Type.__name__ = "Integer32"
_SleNetIfMtu_Object = MibTableColumn
sleNetIfMtu = _SleNetIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 9),
    _SleNetIfMtu_Type()
)
sleNetIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfMtu.setStatus("current")


class _SleNetIfIpSetMode_Type(Integer32):
    """Custom type sleNetIfIpSetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_SleNetIfIpSetMode_Type.__name__ = "Integer32"
_SleNetIfIpSetMode_Object = MibTableColumn
sleNetIfIpSetMode = _SleNetIfIpSetMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 10),
    _SleNetIfIpSetMode_Type()
)
sleNetIfIpSetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpSetMode.setStatus("current")


class _SleNetIfIpMartianFilter_Type(Integer32):
    """Custom type sleNetIfIpMartianFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfIpMartianFilter_Type.__name__ = "Integer32"
_SleNetIfIpMartianFilter_Object = MibTableColumn
sleNetIfIpMartianFilter = _SleNetIfIpMartianFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 11),
    _SleNetIfIpMartianFilter_Type()
)
sleNetIfIpMartianFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpMartianFilter.setStatus("current")
_SleNetIfUpCnt_Type = Integer32
_SleNetIfUpCnt_Object = MibTableColumn
sleNetIfUpCnt = _SleNetIfUpCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 12),
    _SleNetIfUpCnt_Type()
)
sleNetIfUpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfUpCnt.setStatus("current")
_SleNetIfDownCnt_Type = Integer32
_SleNetIfDownCnt_Object = MibTableColumn
sleNetIfDownCnt = _SleNetIfDownCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 13),
    _SleNetIfDownCnt_Type()
)
sleNetIfDownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfDownCnt.setStatus("current")
_SleNetIfLinkUpTime_Type = Counter64
_SleNetIfLinkUpTime_Object = MibTableColumn
sleNetIfLinkUpTime = _SleNetIfLinkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 14),
    _SleNetIfLinkUpTime_Type()
)
sleNetIfLinkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfLinkUpTime.setStatus("current")
if mibBuilder.loadTexts:
    sleNetIfLinkUpTime.setUnits("1 sec")
_SleNetIfElapsedTimeAfterClearStats_Type = Counter64
_SleNetIfElapsedTimeAfterClearStats_Object = MibTableColumn
sleNetIfElapsedTimeAfterClearStats = _SleNetIfElapsedTimeAfterClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 15),
    _SleNetIfElapsedTimeAfterClearStats_Type()
)
sleNetIfElapsedTimeAfterClearStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfElapsedTimeAfterClearStats.setStatus("current")
if mibBuilder.loadTexts:
    sleNetIfElapsedTimeAfterClearStats.setUnits("1 sec")


class _SleNetIfBindingVRFName_Type(OctetString):
    """Custom type sleNetIfBindingVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleNetIfBindingVRFName_Type.__name__ = "OctetString"
_SleNetIfBindingVRFName_Object = MibTableColumn
sleNetIfBindingVRFName = _SleNetIfBindingVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 16),
    _SleNetIfBindingVRFName_Type()
)
sleNetIfBindingVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfBindingVRFName.setStatus("current")


class _SleNetIfOnFailUseVRF_Type(Integer32):
    """Custom type sleNetIfOnFailUseVRF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleNetIfOnFailUseVRF_Type.__name__ = "Integer32"
_SleNetIfOnFailUseVRF_Object = MibTableColumn
sleNetIfOnFailUseVRF = _SleNetIfOnFailUseVRF_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 17),
    _SleNetIfOnFailUseVRF_Type()
)
sleNetIfOnFailUseVRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfOnFailUseVRF.setStatus("current")


class _SleNetIfIpUnreachability_Type(Integer32):
    """Custom type sleNetIfIpUnreachability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleNetIfIpUnreachability_Type.__name__ = "Integer32"
_SleNetIfIpUnreachability_Object = MibTableColumn
sleNetIfIpUnreachability = _SleNetIfIpUnreachability_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 18),
    _SleNetIfIpUnreachability_Type()
)
sleNetIfIpUnreachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpUnreachability.setStatus("current")


class _SleNetIfipRedirects_Type(Integer32):
    """Custom type sleNetIfipRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleNetIfipRedirects_Type.__name__ = "Integer32"
_SleNetIfipRedirects_Object = MibTableColumn
sleNetIfipRedirects = _SleNetIfipRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 19),
    _SleNetIfipRedirects_Type()
)
sleNetIfipRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfipRedirects.setStatus("current")


class _SleNetIfIpForwarding_Type(Integer32):
    """Custom type sleNetIfIpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfIpForwarding_Type.__name__ = "Integer32"
_SleNetIfIpForwarding_Object = MibTableColumn
sleNetIfIpForwarding = _SleNetIfIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 20),
    _SleNetIfIpForwarding_Type()
)
sleNetIfIpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpForwarding.setStatus("current")
_SleNetIfAlias_Type = OctetString
_SleNetIfAlias_Object = MibTableColumn
sleNetIfAlias = _SleNetIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 21),
    _SleNetIfAlias_Type()
)
sleNetIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfAlias.setStatus("current")


class _SleNetIfIpArpAlias_Type(Integer32):
    """Custom type sleNetIfIpArpAlias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfIpArpAlias_Type.__name__ = "Integer32"
_SleNetIfIpArpAlias_Object = MibTableColumn
sleNetIfIpArpAlias = _SleNetIfIpArpAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 22),
    _SleNetIfIpArpAlias_Type()
)
sleNetIfIpArpAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpArpAlias.setStatus("current")
_SleNetIfIpArpAliasMac_Type = MacAddress
_SleNetIfIpArpAliasMac_Object = MibTableColumn
sleNetIfIpArpAliasMac = _SleNetIfIpArpAliasMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 23),
    _SleNetIfIpArpAliasMac_Type()
)
sleNetIfIpArpAliasMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpArpAliasMac.setStatus("current")


class _SleNetIfArpMCProbeCount_Type(Integer32):
    """Custom type sleNetIfArpMCProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleNetIfArpMCProbeCount_Type.__name__ = "Integer32"
_SleNetIfArpMCProbeCount_Object = MibTableColumn
sleNetIfArpMCProbeCount = _SleNetIfArpMCProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 24),
    _SleNetIfArpMCProbeCount_Type()
)
sleNetIfArpMCProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfArpMCProbeCount.setStatus("current")


class _SleNetIfArpUCProbeCount_Type(Integer32):
    """Custom type sleNetIfArpUCProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleNetIfArpUCProbeCount_Type.__name__ = "Integer32"
_SleNetIfArpUCProbeCount_Object = MibTableColumn
sleNetIfArpUCProbeCount = _SleNetIfArpUCProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 25),
    _SleNetIfArpUCProbeCount_Type()
)
sleNetIfArpUCProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfArpUCProbeCount.setStatus("current")


class _SleNetIfArpRetransTime_Type(Integer32):
    """Custom type sleNetIfArpRetransTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_SleNetIfArpRetransTime_Type.__name__ = "Integer32"
_SleNetIfArpRetransTime_Object = MibTableColumn
sleNetIfArpRetransTime = _SleNetIfArpRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 26),
    _SleNetIfArpRetransTime_Type()
)
sleNetIfArpRetransTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfArpRetransTime.setStatus("current")


class _SleNetIfIpProxyArp_Type(Integer32):
    """Custom type sleNetIfIpProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfIpProxyArp_Type.__name__ = "Integer32"
_SleNetIfIpProxyArp_Object = MibTableColumn
sleNetIfIpProxyArp = _SleNetIfIpProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 27),
    _SleNetIfIpProxyArp_Type()
)
sleNetIfIpProxyArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpProxyArp.setStatus("current")


class _SleNetIfIpRPFilter_Type(Integer32):
    """Custom type sleNetIfIpRPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("loose", 1),
          ("strict", 2))
    )


_SleNetIfIpRPFilter_Type.__name__ = "Integer32"
_SleNetIfIpRPFilter_Object = MibTableColumn
sleNetIfIpRPFilter = _SleNetIfIpRPFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 28),
    _SleNetIfIpRPFilter_Type()
)
sleNetIfIpRPFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfIpRPFilter.setStatus("current")


class _SleNetIfRPFilter_Type(Integer32):
    """Custom type sleNetIfRPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("loose", 1),
          ("strict", 2),
          ("looseAllow", 3))
    )


_SleNetIfRPFilter_Type.__name__ = "Integer32"
_SleNetIfRPFilter_Object = MibTableColumn
sleNetIfRPFilter = _SleNetIfRPFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 29),
    _SleNetIfRPFilter_Type()
)
sleNetIfRPFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfRPFilter.setStatus("current")
_SleNetIfRouteMap_Type = OctetString
_SleNetIfRouteMap_Object = MibTableColumn
sleNetIfRouteMap = _SleNetIfRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 1, 1, 30),
    _SleNetIfRouteMap_Type()
)
sleNetIfRouteMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfRouteMap.setStatus("current")
_SleNetIfControl_ObjectIdentity = ObjectIdentity
sleNetIfControl = _SleNetIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2)
)


class _SleNetIfControlRequest_Type(Integer32):
    """Custom type sleNetIfControlRequest based on Integer32"""
    defaultValue = 2

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
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("setNetIfRegState", 1),
          ("setNetIfProfile", 2),
          ("setNetIfIpMartianFilter", 3),
          ("setNetIfBindingVRF", 4),
          ("unsetNetIfBindingVRF", 5),
          ("setNetIfOnFailUseVRF", 6),
          ("setNetIfIpUnreachability", 7),
          ("setNetIfIpRedirects", 8),
          ("setNetIfIpForwarding", 9),
          ("setAlias", 10),
          ("setIpArpAlias", 11),
          ("setArpMCProbeCount", 12),
          ("setArpUCProbeCount", 13),
          ("setArpRetransTime", 14),
          ("setIpProxyArp", 15),
          ("setIpRPFilter", 16),
          ("setRPFilter", 17),
          ("setRouteMap", 18))
    )


_SleNetIfControlRequest_Type.__name__ = "Integer32"
_SleNetIfControlRequest_Object = MibScalar
sleNetIfControlRequest = _SleNetIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 1),
    _SleNetIfControlRequest_Type()
)
sleNetIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlRequest.setStatus("current")
_SleNetIfControlStatus_Type = SleControlStatusType
_SleNetIfControlStatus_Object = MibScalar
sleNetIfControlStatus = _SleNetIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 2),
    _SleNetIfControlStatus_Type()
)
sleNetIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfControlStatus.setStatus("current")


class _SleNetIfControlTimer_Type(Gauge32):
    """Custom type sleNetIfControlTimer based on Gauge32"""
    defaultValue = 0


_SleNetIfControlTimer_Type.__name__ = "Gauge32"
_SleNetIfControlTimer_Object = MibScalar
sleNetIfControlTimer = _SleNetIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 3),
    _SleNetIfControlTimer_Type()
)
sleNetIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlTimer.setStatus("current")
_SleNetIfControlTimeStamp_Type = SleControlRequestResultType
_SleNetIfControlTimeStamp_Object = MibScalar
sleNetIfControlTimeStamp = _SleNetIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 4),
    _SleNetIfControlTimeStamp_Type()
)
sleNetIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfControlTimeStamp.setStatus("current")
_SleNetIfControlReqResult_Type = TimeTicks
_SleNetIfControlReqResult_Object = MibScalar
sleNetIfControlReqResult = _SleNetIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 5),
    _SleNetIfControlReqResult_Type()
)
sleNetIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIfControlReqResult.setStatus("current")


class _SleNetIfControlIndex_Type(Integer32):
    """Custom type sleNetIfControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11023),
    )


_SleNetIfControlIndex_Type.__name__ = "Integer32"
_SleNetIfControlIndex_Object = MibScalar
sleNetIfControlIndex = _SleNetIfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 6),
    _SleNetIfControlIndex_Type()
)
sleNetIfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIndex.setStatus("current")


class _SleNetIfControlDescription_Type(OctetString):
    """Custom type sleNetIfControlDescription based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SleNetIfControlDescription_Type.__name__ = "OctetString"
_SleNetIfControlDescription_Object = MibScalar
sleNetIfControlDescription = _SleNetIfControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 7),
    _SleNetIfControlDescription_Type()
)
sleNetIfControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlDescription.setStatus("current")


class _SleNetIfControlRegState_Type(Integer32):
    """Custom type sleNetIfControlRegState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unregister", 0),
          ("register", 1))
    )


_SleNetIfControlRegState_Type.__name__ = "Integer32"
_SleNetIfControlRegState_Object = MibScalar
sleNetIfControlRegState = _SleNetIfControlRegState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 8),
    _SleNetIfControlRegState_Type()
)
sleNetIfControlRegState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlRegState.setStatus("current")


class _SleNetIfControlAdminState_Type(Integer32):
    """Custom type sleNetIfControlAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_SleNetIfControlAdminState_Type.__name__ = "Integer32"
_SleNetIfControlAdminState_Object = MibScalar
sleNetIfControlAdminState = _SleNetIfControlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 9),
    _SleNetIfControlAdminState_Type()
)
sleNetIfControlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlAdminState.setStatus("current")


class _SleNetIfControlMulticast_Type(Integer32):
    """Custom type sleNetIfControlMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfControlMulticast_Type.__name__ = "Integer32"
_SleNetIfControlMulticast_Object = MibScalar
sleNetIfControlMulticast = _SleNetIfControlMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 10),
    _SleNetIfControlMulticast_Type()
)
sleNetIfControlMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlMulticast.setStatus("current")


class _SleNetIfControlMtu_Type(Integer32):
    """Custom type sleNetIfControlMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 17940),
    )


_SleNetIfControlMtu_Type.__name__ = "Integer32"
_SleNetIfControlMtu_Object = MibScalar
sleNetIfControlMtu = _SleNetIfControlMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 11),
    _SleNetIfControlMtu_Type()
)
sleNetIfControlMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlMtu.setStatus("current")


class _SleNetIfControlIpMartianFilter_Type(Integer32):
    """Custom type sleNetIfControlIpMartianFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfControlIpMartianFilter_Type.__name__ = "Integer32"
_SleNetIfControlIpMartianFilter_Object = MibScalar
sleNetIfControlIpMartianFilter = _SleNetIfControlIpMartianFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 12),
    _SleNetIfControlIpMartianFilter_Type()
)
sleNetIfControlIpMartianFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpMartianFilter.setStatus("current")


class _SleNetIfControlBindingVRFName_Type(OctetString):
    """Custom type sleNetIfControlBindingVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleNetIfControlBindingVRFName_Type.__name__ = "OctetString"
_SleNetIfControlBindingVRFName_Object = MibScalar
sleNetIfControlBindingVRFName = _SleNetIfControlBindingVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 13),
    _SleNetIfControlBindingVRFName_Type()
)
sleNetIfControlBindingVRFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlBindingVRFName.setStatus("current")


class _SleNetIfControlOnFailUseVRF_Type(Integer32):
    """Custom type sleNetIfControlOnFailUseVRF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleNetIfControlOnFailUseVRF_Type.__name__ = "Integer32"
_SleNetIfControlOnFailUseVRF_Object = MibScalar
sleNetIfControlOnFailUseVRF = _SleNetIfControlOnFailUseVRF_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 14),
    _SleNetIfControlOnFailUseVRF_Type()
)
sleNetIfControlOnFailUseVRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlOnFailUseVRF.setStatus("current")


class _SleNetIfControlIpUnreachability_Type(Integer32):
    """Custom type sleNetIfControlIpUnreachability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleNetIfControlIpUnreachability_Type.__name__ = "Integer32"
_SleNetIfControlIpUnreachability_Object = MibScalar
sleNetIfControlIpUnreachability = _SleNetIfControlIpUnreachability_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 15),
    _SleNetIfControlIpUnreachability_Type()
)
sleNetIfControlIpUnreachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpUnreachability.setStatus("current")


class _SleNetIfControlIpRedirects_Type(Integer32):
    """Custom type sleNetIfControlIpRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleNetIfControlIpRedirects_Type.__name__ = "Integer32"
_SleNetIfControlIpRedirects_Object = MibScalar
sleNetIfControlIpRedirects = _SleNetIfControlIpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 16),
    _SleNetIfControlIpRedirects_Type()
)
sleNetIfControlIpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpRedirects.setStatus("current")


class _SleNetIfControlIpForwarding_Type(Integer32):
    """Custom type sleNetIfControlIpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfControlIpForwarding_Type.__name__ = "Integer32"
_SleNetIfControlIpForwarding_Object = MibScalar
sleNetIfControlIpForwarding = _SleNetIfControlIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 17),
    _SleNetIfControlIpForwarding_Type()
)
sleNetIfControlIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpForwarding.setStatus("current")
_SleNetIfControlAlias_Type = OctetString
_SleNetIfControlAlias_Object = MibScalar
sleNetIfControlAlias = _SleNetIfControlAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 18),
    _SleNetIfControlAlias_Type()
)
sleNetIfControlAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlAlias.setStatus("current")


class _SleNetIfControlIpArpAlias_Type(Integer32):
    """Custom type sleNetIfControlIpArpAlias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfControlIpArpAlias_Type.__name__ = "Integer32"
_SleNetIfControlIpArpAlias_Object = MibScalar
sleNetIfControlIpArpAlias = _SleNetIfControlIpArpAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 19),
    _SleNetIfControlIpArpAlias_Type()
)
sleNetIfControlIpArpAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpArpAlias.setStatus("current")
_SleNetIfControlIpArpAliasMac_Type = MacAddress
_SleNetIfControlIpArpAliasMac_Object = MibScalar
sleNetIfControlIpArpAliasMac = _SleNetIfControlIpArpAliasMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 20),
    _SleNetIfControlIpArpAliasMac_Type()
)
sleNetIfControlIpArpAliasMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpArpAliasMac.setStatus("current")


class _SleNetIfControlArpMCProbeCount_Type(Integer32):
    """Custom type sleNetIfControlArpMCProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleNetIfControlArpMCProbeCount_Type.__name__ = "Integer32"
_SleNetIfControlArpMCProbeCount_Object = MibScalar
sleNetIfControlArpMCProbeCount = _SleNetIfControlArpMCProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 21),
    _SleNetIfControlArpMCProbeCount_Type()
)
sleNetIfControlArpMCProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlArpMCProbeCount.setStatus("current")


class _SleNetIfControlArpUCProbeCount_Type(Integer32):
    """Custom type sleNetIfControlArpUCProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleNetIfControlArpUCProbeCount_Type.__name__ = "Integer32"
_SleNetIfControlArpUCProbeCount_Object = MibScalar
sleNetIfControlArpUCProbeCount = _SleNetIfControlArpUCProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 22),
    _SleNetIfControlArpUCProbeCount_Type()
)
sleNetIfControlArpUCProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlArpUCProbeCount.setStatus("current")


class _SleNetIfControlArpRetransTime_Type(Integer32):
    """Custom type sleNetIfControlArpRetransTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_SleNetIfControlArpRetransTime_Type.__name__ = "Integer32"
_SleNetIfControlArpRetransTime_Object = MibScalar
sleNetIfControlArpRetransTime = _SleNetIfControlArpRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 23),
    _SleNetIfControlArpRetransTime_Type()
)
sleNetIfControlArpRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlArpRetransTime.setStatus("current")


class _SleNetIfControlIpProxyArp_Type(Integer32):
    """Custom type sleNetIfControlIpProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNetIfControlIpProxyArp_Type.__name__ = "Integer32"
_SleNetIfControlIpProxyArp_Object = MibScalar
sleNetIfControlIpProxyArp = _SleNetIfControlIpProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 24),
    _SleNetIfControlIpProxyArp_Type()
)
sleNetIfControlIpProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpProxyArp.setStatus("current")


class _SleNetIfControlIpRPFilter_Type(Integer32):
    """Custom type sleNetIfControlIpRPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("loose", 1),
          ("strict", 2))
    )


_SleNetIfControlIpRPFilter_Type.__name__ = "Integer32"
_SleNetIfControlIpRPFilter_Object = MibScalar
sleNetIfControlIpRPFilter = _SleNetIfControlIpRPFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 25),
    _SleNetIfControlIpRPFilter_Type()
)
sleNetIfControlIpRPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlIpRPFilter.setStatus("current")


class _SleNetIfControlRPFilter_Type(Integer32):
    """Custom type sleNetIfControlRPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("loose", 1),
          ("strict", 2),
          ("looseAllow", 3))
    )


_SleNetIfControlRPFilter_Type.__name__ = "Integer32"
_SleNetIfControlRPFilter_Object = MibScalar
sleNetIfControlRPFilter = _SleNetIfControlRPFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 26),
    _SleNetIfControlRPFilter_Type()
)
sleNetIfControlRPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlRPFilter.setStatus("current")
_SleNetIfControlRouteMap_Type = OctetString
_SleNetIfControlRouteMap_Object = MibScalar
sleNetIfControlRouteMap = _SleNetIfControlRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 2, 27),
    _SleNetIfControlRouteMap_Type()
)
sleNetIfControlRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIfControlRouteMap.setStatus("current")
_SleNetIfNotification_ObjectIdentity = ObjectIdentity
sleNetIfNotification = _SleNetIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3)
)
_SleIpAddress_ObjectIdentity = ObjectIdentity
sleIpAddress = _SleIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2)
)
_SleIpAddrTable_Object = MibTable
sleIpAddrTable = _SleIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1)
)
if mibBuilder.loadTexts:
    sleIpAddrTable.setStatus("current")
_SleIpAddrEntry_Object = MibTableRow
sleIpAddrEntry = _SleIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1)
)
sleIpAddrEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleIpAddrValue"),
)
if mibBuilder.loadTexts:
    sleIpAddrEntry.setStatus("current")
_SleIpAddrValue_Type = IpAddress
_SleIpAddrValue_Object = MibTableColumn
sleIpAddrValue = _SleIpAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1, 1),
    _SleIpAddrValue_Type()
)
sleIpAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrValue.setStatus("current")


class _SleIpAddrMask_Type(Integer32):
    """Custom type sleIpAddrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleIpAddrMask_Type.__name__ = "Integer32"
_SleIpAddrMask_Object = MibTableColumn
sleIpAddrMask = _SleIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1, 2),
    _SleIpAddrMask_Type()
)
sleIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrMask.setStatus("current")
_SleIpAddrBcast_Type = IpAddress
_SleIpAddrBcast_Object = MibTableColumn
sleIpAddrBcast = _SleIpAddrBcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1, 3),
    _SleIpAddrBcast_Type()
)
sleIpAddrBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrBcast.setStatus("current")


class _SleIpAddrFlag_Type(Bits):
    """Custom type sleIpAddrFlag based on Bits"""
    namedValues = NamedValues(
        *(("permanent", 0),
          ("tentative", 1),
          ("deprecated", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("secondary", 7))
    )

_SleIpAddrFlag_Type.__name__ = "Bits"
_SleIpAddrFlag_Object = MibTableColumn
sleIpAddrFlag = _SleIpAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1, 4),
    _SleIpAddrFlag_Type()
)
sleIpAddrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrFlag.setStatus("current")


class _SleIpAddrScope_Type(Integer32):
    """Custom type sleIpAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              200,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("site", 200),
          ("link", 253),
          ("host", 254),
          ("nowhere", 255))
    )


_SleIpAddrScope_Type.__name__ = "Integer32"
_SleIpAddrScope_Object = MibTableColumn
sleIpAddrScope = _SleIpAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1, 5),
    _SleIpAddrScope_Type()
)
sleIpAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrScope.setStatus("current")


class _SleIpAddrIpIndex_Type(Integer32):
    """Custom type sleIpAddrIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleIpAddrIpIndex_Type.__name__ = "Integer32"
_SleIpAddrIpIndex_Object = MibTableColumn
sleIpAddrIpIndex = _SleIpAddrIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1, 6),
    _SleIpAddrIpIndex_Type()
)
sleIpAddrIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrIpIndex.setStatus("current")


class _SleIpAddrUnnumUsedIp_Type(Integer32):
    """Custom type sleIpAddrUnnumUsedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("used", 1))
    )


_SleIpAddrUnnumUsedIp_Type.__name__ = "Integer32"
_SleIpAddrUnnumUsedIp_Object = MibTableColumn
sleIpAddrUnnumUsedIp = _SleIpAddrUnnumUsedIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 1, 1, 7),
    _SleIpAddrUnnumUsedIp_Type()
)
sleIpAddrUnnumUsedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrUnnumUsedIp.setStatus("current")
_SleIpAddrControl_ObjectIdentity = ObjectIdentity
sleIpAddrControl = _SleIpAddrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2)
)


class _SleIpAddrControlRequest_Type(Integer32):
    """Custom type sleIpAddrControlRequest based on Integer32"""
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
        *(("createIpAddress", 1),
          ("destroyIpAddress", 2),
          ("addIpIndex", 3),
          ("delIpIndex", 4))
    )


_SleIpAddrControlRequest_Type.__name__ = "Integer32"
_SleIpAddrControlRequest_Object = MibScalar
sleIpAddrControlRequest = _SleIpAddrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 1),
    _SleIpAddrControlRequest_Type()
)
sleIpAddrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlRequest.setStatus("current")
_SleIpAddrControlStatus_Type = SleControlStatusType
_SleIpAddrControlStatus_Object = MibScalar
sleIpAddrControlStatus = _SleIpAddrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 2),
    _SleIpAddrControlStatus_Type()
)
sleIpAddrControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrControlStatus.setStatus("current")


class _SleIpAddrControlTimer_Type(Gauge32):
    """Custom type sleIpAddrControlTimer based on Gauge32"""
    defaultValue = 0


_SleIpAddrControlTimer_Type.__name__ = "Gauge32"
_SleIpAddrControlTimer_Object = MibScalar
sleIpAddrControlTimer = _SleIpAddrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 3),
    _SleIpAddrControlTimer_Type()
)
sleIpAddrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlTimer.setStatus("current")
_SleIpAddrControlTimeStamp_Type = SleControlRequestResultType
_SleIpAddrControlTimeStamp_Object = MibScalar
sleIpAddrControlTimeStamp = _SleIpAddrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 4),
    _SleIpAddrControlTimeStamp_Type()
)
sleIpAddrControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrControlTimeStamp.setStatus("current")
_SleIpAddrControlReqResult_Type = TimeTicks
_SleIpAddrControlReqResult_Object = MibScalar
sleIpAddrControlReqResult = _SleIpAddrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 5),
    _SleIpAddrControlReqResult_Type()
)
sleIpAddrControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddrControlReqResult.setStatus("current")


class _SleIpAddrControlNetIfIndex_Type(Integer32):
    """Custom type sleIpAddrControlNetIfIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(10000, 11023),
    )


_SleIpAddrControlNetIfIndex_Type.__name__ = "Integer32"
_SleIpAddrControlNetIfIndex_Object = MibScalar
sleIpAddrControlNetIfIndex = _SleIpAddrControlNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 6),
    _SleIpAddrControlNetIfIndex_Type()
)
sleIpAddrControlNetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlNetIfIndex.setStatus("current")


class _SleIpAddrControlValue_Type(IpAddress):
    """Custom type sleIpAddrControlValue based on IpAddress"""
    defaultHexValue = "ac106464"


_SleIpAddrControlValue_Type.__name__ = "IpAddress"
_SleIpAddrControlValue_Object = MibScalar
sleIpAddrControlValue = _SleIpAddrControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 7),
    _SleIpAddrControlValue_Type()
)
sleIpAddrControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlValue.setStatus("current")


class _SleIpAddrControlMask_Type(Integer32):
    """Custom type sleIpAddrControlMask based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleIpAddrControlMask_Type.__name__ = "Integer32"
_SleIpAddrControlMask_Object = MibScalar
sleIpAddrControlMask = _SleIpAddrControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 8),
    _SleIpAddrControlMask_Type()
)
sleIpAddrControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlMask.setStatus("current")


class _SleIpAddrControlFlag_Type(Integer32):
    """Custom type sleIpAddrControlFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_SleIpAddrControlFlag_Type.__name__ = "Integer32"
_SleIpAddrControlFlag_Object = MibScalar
sleIpAddrControlFlag = _SleIpAddrControlFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 9),
    _SleIpAddrControlFlag_Type()
)
sleIpAddrControlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlFlag.setStatus("current")


class _SleIpAddrControlScope_Type(Integer32):
    """Custom type sleIpAddrControlScope based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              253,
              254)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("link", 253),
          ("host", 254))
    )


_SleIpAddrControlScope_Type.__name__ = "Integer32"
_SleIpAddrControlScope_Object = MibScalar
sleIpAddrControlScope = _SleIpAddrControlScope_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 10),
    _SleIpAddrControlScope_Type()
)
sleIpAddrControlScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlScope.setStatus("current")


class _SleIpAddrControlIpIndex_Type(Integer32):
    """Custom type sleIpAddrControlIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SleIpAddrControlIpIndex_Type.__name__ = "Integer32"
_SleIpAddrControlIpIndex_Object = MibScalar
sleIpAddrControlIpIndex = _SleIpAddrControlIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 2, 11),
    _SleIpAddrControlIpIndex_Type()
)
sleIpAddrControlIpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddrControlIpIndex.setStatus("current")
_SleIpAddrNotification_ObjectIdentity = ObjectIdentity
sleIpAddrNotification = _SleIpAddrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 3)
)
_SleArp_ObjectIdentity = ObjectIdentity
sleArp = _SleArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3)
)
_SleArpTable_Object = MibTable
sleArpTable = _SleArpTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1)
)
if mibBuilder.loadTexts:
    sleArpTable.setStatus("current")
_SleArpEntry_Object = MibTableRow
sleArpEntry = _SleArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1)
)
sleArpEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleArpIpAddress"),
)
if mibBuilder.loadTexts:
    sleArpEntry.setStatus("current")
_SleArpIpAddress_Type = IpAddress
_SleArpIpAddress_Object = MibTableColumn
sleArpIpAddress = _SleArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1, 1),
    _SleArpIpAddress_Type()
)
sleArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpIpAddress.setStatus("current")
_SleArpPhyAddress_Type = MacAddress
_SleArpPhyAddress_Object = MibTableColumn
sleArpPhyAddress = _SleArpPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1, 2),
    _SleArpPhyAddress_Type()
)
sleArpPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpPhyAddress.setStatus("current")


class _SleArpPortIndex_Type(Integer32):
    """Custom type sleArpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleArpPortIndex_Type.__name__ = "Integer32"
_SleArpPortIndex_Object = MibTableColumn
sleArpPortIndex = _SleArpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1, 3),
    _SleArpPortIndex_Type()
)
sleArpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpPortIndex.setStatus("current")


class _SleArpState_Type(Integer32):
    """Custom type sleArpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_SleArpState_Type.__name__ = "Integer32"
_SleArpState_Object = MibTableColumn
sleArpState = _SleArpState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1, 4),
    _SleArpState_Type()
)
sleArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpState.setStatus("current")


class _SleArpHwType_Type(Integer32):
    """Custom type sleArpHwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethernet", 1)
    )


_SleArpHwType_Type.__name__ = "Integer32"
_SleArpHwType_Object = MibTableColumn
sleArpHwType = _SleArpHwType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1, 5),
    _SleArpHwType_Type()
)
sleArpHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpHwType.setStatus("current")


class _SleArpHwUsed_Type(Integer32):
    """Custom type sleArpHwUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonused", 0),
          ("used", 1))
    )


_SleArpHwUsed_Type.__name__ = "Integer32"
_SleArpHwUsed_Object = MibTableColumn
sleArpHwUsed = _SleArpHwUsed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1, 6),
    _SleArpHwUsed_Type()
)
sleArpHwUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpHwUsed.setStatus("current")


class _SleArpUsedTime_Type(Integer32):
    """Custom type sleArpUsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_SleArpUsedTime_Type.__name__ = "Integer32"
_SleArpUsedTime_Object = MibTableColumn
sleArpUsedTime = _SleArpUsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 1, 1, 7),
    _SleArpUsedTime_Type()
)
sleArpUsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpUsedTime.setStatus("current")
_SleArpControl_ObjectIdentity = ObjectIdentity
sleArpControl = _SleArpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2)
)


class _SleArpControlRequest_Type(Integer32):
    """Custom type sleArpControlRequest based on Integer32"""
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
        *(("createArpEntry", 1),
          ("destroyArpEntry", 2),
          ("clearArpTable", 3),
          ("clearArpTableByAddr", 4))
    )


_SleArpControlRequest_Type.__name__ = "Integer32"
_SleArpControlRequest_Object = MibScalar
sleArpControlRequest = _SleArpControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 1),
    _SleArpControlRequest_Type()
)
sleArpControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpControlRequest.setStatus("current")
_SleArpControlStatus_Type = SleControlStatusType
_SleArpControlStatus_Object = MibScalar
sleArpControlStatus = _SleArpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 2),
    _SleArpControlStatus_Type()
)
sleArpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpControlStatus.setStatus("current")
_SleArpControlTimer_Type = Gauge32
_SleArpControlTimer_Object = MibScalar
sleArpControlTimer = _SleArpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 3),
    _SleArpControlTimer_Type()
)
sleArpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpControlTimer.setStatus("current")
_SleArpControlTimeStamp_Type = SleControlRequestResultType
_SleArpControlTimeStamp_Object = MibScalar
sleArpControlTimeStamp = _SleArpControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 4),
    _SleArpControlTimeStamp_Type()
)
sleArpControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpControlTimeStamp.setStatus("current")
_SleArpControlReqResult_Type = TimeTicks
_SleArpControlReqResult_Object = MibScalar
sleArpControlReqResult = _SleArpControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 5),
    _SleArpControlReqResult_Type()
)
sleArpControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpControlReqResult.setStatus("current")


class _SleArpControlNetIfIndex_Type(Integer32):
    """Custom type sleArpControlNetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_SleArpControlNetIfIndex_Type.__name__ = "Integer32"
_SleArpControlNetIfIndex_Object = MibScalar
sleArpControlNetIfIndex = _SleArpControlNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 6),
    _SleArpControlNetIfIndex_Type()
)
sleArpControlNetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpControlNetIfIndex.setStatus("current")
_SleArpControlIpAddress_Type = IpAddress
_SleArpControlIpAddress_Object = MibScalar
sleArpControlIpAddress = _SleArpControlIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 7),
    _SleArpControlIpAddress_Type()
)
sleArpControlIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpControlIpAddress.setStatus("current")
_SleArpControlPhyAddress_Type = MacAddress
_SleArpControlPhyAddress_Object = MibScalar
sleArpControlPhyAddress = _SleArpControlPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 8),
    _SleArpControlPhyAddress_Type()
)
sleArpControlPhyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpControlPhyAddress.setStatus("current")


class _SleArpControlState_Type(Integer32):
    """Custom type sleArpControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_SleArpControlState_Type.__name__ = "Integer32"
_SleArpControlState_Object = MibScalar
sleArpControlState = _SleArpControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 9),
    _SleArpControlState_Type()
)
sleArpControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpControlState.setStatus("current")


class _SleArpControlMask_Type(Integer32):
    """Custom type sleArpControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleArpControlMask_Type.__name__ = "Integer32"
_SleArpControlMask_Object = MibScalar
sleArpControlMask = _SleArpControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 2, 10),
    _SleArpControlMask_Type()
)
sleArpControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpControlMask.setStatus("current")
_SleArpNotification_ObjectIdentity = ObjectIdentity
sleArpNotification = _SleArpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 3)
)
_SleRoute_ObjectIdentity = ObjectIdentity
sleRoute = _SleRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4)
)
_SleRouteTable_Object = MibTable
sleRouteTable = _SleRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1)
)
if mibBuilder.loadTexts:
    sleRouteTable.setStatus("current")
_SleRouteEntry_Object = MibTableRow
sleRouteEntry = _SleRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1)
)
sleRouteEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleRouteDstAddress"),
    (0, "SLE-NETWORK-MIB", "sleRouteDstMask"),
    (0, "SLE-NETWORK-MIB", "sleRouteGateway"),
    (0, "SLE-NETWORK-MIB", "sleRouteInterface"),
    (0, "SLE-NETWORK-MIB", "sleRouteVRFIndex"),
)
if mibBuilder.loadTexts:
    sleRouteEntry.setStatus("current")
_SleRouteDstAddress_Type = IpAddress
_SleRouteDstAddress_Object = MibTableColumn
sleRouteDstAddress = _SleRouteDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 1),
    _SleRouteDstAddress_Type()
)
sleRouteDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteDstAddress.setStatus("current")


class _SleRouteDstMask_Type(Integer32):
    """Custom type sleRouteDstMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRouteDstMask_Type.__name__ = "Integer32"
_SleRouteDstMask_Object = MibTableColumn
sleRouteDstMask = _SleRouteDstMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 2),
    _SleRouteDstMask_Type()
)
sleRouteDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteDstMask.setStatus("current")
_SleRouteGateway_Type = IpAddress
_SleRouteGateway_Object = MibTableColumn
sleRouteGateway = _SleRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 3),
    _SleRouteGateway_Type()
)
sleRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteGateway.setStatus("current")


class _SleRouteInterface_Type(Integer32):
    """Custom type sleRouteInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11023),
    )


_SleRouteInterface_Type.__name__ = "Integer32"
_SleRouteInterface_Object = MibTableColumn
sleRouteInterface = _SleRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 4),
    _SleRouteInterface_Type()
)
sleRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteInterface.setStatus("current")


class _SleRouteType_Type(Integer32):
    """Custom type sleRouteType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("direct", 3),
          ("indirect", 4))
    )


_SleRouteType_Type.__name__ = "Integer32"
_SleRouteType_Object = MibTableColumn
sleRouteType = _SleRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 5),
    _SleRouteType_Type()
)
sleRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteType.setStatus("current")


class _SleRouteProto_Type(Integer32):
    """Custom type sleRouteProto based on Integer32"""
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("localDirect", 2),
          ("netmgmtStatic", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16),
          ("dhcp", 17))
    )


_SleRouteProto_Type.__name__ = "Integer32"
_SleRouteProto_Object = MibTableColumn
sleRouteProto = _SleRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 6),
    _SleRouteProto_Type()
)
sleRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteProto.setStatus("current")


class _SleRouteMetric_Type(Integer32):
    """Custom type sleRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SleRouteMetric_Type.__name__ = "Integer32"
_SleRouteMetric_Object = MibTableColumn
sleRouteMetric = _SleRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 7),
    _SleRouteMetric_Type()
)
sleRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteMetric.setStatus("current")


class _SleRouteActive_Type(Integer32):
    """Custom type sleRouteActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SleRouteActive_Type.__name__ = "Integer32"
_SleRouteActive_Object = MibTableColumn
sleRouteActive = _SleRouteActive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 8),
    _SleRouteActive_Type()
)
sleRouteActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteActive.setStatus("current")
_SleRouteBindingSrcAddr_Type = IpAddress
_SleRouteBindingSrcAddr_Object = MibTableColumn
sleRouteBindingSrcAddr = _SleRouteBindingSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 9),
    _SleRouteBindingSrcAddr_Type()
)
sleRouteBindingSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteBindingSrcAddr.setStatus("current")


class _SleRouteDistance_Type(Integer32):
    """Custom type sleRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRouteDistance_Type.__name__ = "Integer32"
_SleRouteDistance_Object = MibTableColumn
sleRouteDistance = _SleRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 10),
    _SleRouteDistance_Type()
)
sleRouteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteDistance.setStatus("current")


class _SleRouteSubtype_Type(Integer32):
    """Custom type sleRouteSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ospfIa", 1),
          ("ospfNssa1", 2),
          ("ospfNssa2", 3),
          ("ospfExternal1", 4),
          ("ospfExternal2", 5),
          ("isisL1", 8),
          ("isisL2", 9),
          ("isisIa", 10),
          ("bgpMpls", 11))
    )


_SleRouteSubtype_Type.__name__ = "Integer32"
_SleRouteSubtype_Object = MibTableColumn
sleRouteSubtype = _SleRouteSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 11),
    _SleRouteSubtype_Type()
)
sleRouteSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteSubtype.setStatus("current")


class _SleRouteNexthopStatus_Type(Bits):
    """Custom type sleRouteNexthopStatus based on Bits"""
    namedValues = NamedValues(
        *(("active", 0),
          ("fib", 1),
          ("recursive", 2))
    )

_SleRouteNexthopStatus_Type.__name__ = "Bits"
_SleRouteNexthopStatus_Object = MibTableColumn
sleRouteNexthopStatus = _SleRouteNexthopStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 12),
    _SleRouteNexthopStatus_Type()
)
sleRouteNexthopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteNexthopStatus.setStatus("current")


class _SleRouteRibStatus_Type(Bits):
    """Custom type sleRouteRibStatus based on Bits"""
    namedValues = NamedValues(
        *(("internal", 0),
          ("selfroute", 1),
          ("blackhole", 2),
          ("nonfib", 3),
          ("selected", 4),
          ("changed", 5),
          ("static", 6),
          ("stale", 7))
    )

_SleRouteRibStatus_Type.__name__ = "Bits"
_SleRouteRibStatus_Object = MibTableColumn
sleRouteRibStatus = _SleRouteRibStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 13),
    _SleRouteRibStatus_Type()
)
sleRouteRibStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteRibStatus.setStatus("current")


class _SleRouteVRFIndex_Type(Integer32):
    """Custom type sleRouteVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleRouteVRFIndex_Type.__name__ = "Integer32"
_SleRouteVRFIndex_Object = MibTableColumn
sleRouteVRFIndex = _SleRouteVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 1, 1, 14),
    _SleRouteVRFIndex_Type()
)
sleRouteVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteVRFIndex.setStatus("current")
_SleRouteControl_ObjectIdentity = ObjectIdentity
sleRouteControl = _SleRouteControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2)
)


class _SleRouteControlRequest_Type(Integer32):
    """Custom type sleRouteControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createStaticRoute", 1),
          ("destroyStaticRoute", 2),
          ("setStaticRouteProfile", 3))
    )


_SleRouteControlRequest_Type.__name__ = "Integer32"
_SleRouteControlRequest_Object = MibScalar
sleRouteControlRequest = _SleRouteControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 1),
    _SleRouteControlRequest_Type()
)
sleRouteControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlRequest.setStatus("current")
_SleRouteControlStatus_Type = SleControlStatusType
_SleRouteControlStatus_Object = MibScalar
sleRouteControlStatus = _SleRouteControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 2),
    _SleRouteControlStatus_Type()
)
sleRouteControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteControlStatus.setStatus("current")
_SleRouteControlTimer_Type = Gauge32
_SleRouteControlTimer_Object = MibScalar
sleRouteControlTimer = _SleRouteControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 3),
    _SleRouteControlTimer_Type()
)
sleRouteControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlTimer.setStatus("current")
_SleRouteControlTimeStamp_Type = SleControlRequestResultType
_SleRouteControlTimeStamp_Object = MibScalar
sleRouteControlTimeStamp = _SleRouteControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 4),
    _SleRouteControlTimeStamp_Type()
)
sleRouteControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteControlTimeStamp.setStatus("current")
_SleRouteControlReqResult_Type = TimeTicks
_SleRouteControlReqResult_Object = MibScalar
sleRouteControlReqResult = _SleRouteControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 5),
    _SleRouteControlReqResult_Type()
)
sleRouteControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRouteControlReqResult.setStatus("current")
_SleRouteControlDstAddress_Type = IpAddress
_SleRouteControlDstAddress_Object = MibScalar
sleRouteControlDstAddress = _SleRouteControlDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 6),
    _SleRouteControlDstAddress_Type()
)
sleRouteControlDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlDstAddress.setStatus("current")


class _SleRouteControlDstMask_Type(Integer32):
    """Custom type sleRouteControlDstMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRouteControlDstMask_Type.__name__ = "Integer32"
_SleRouteControlDstMask_Object = MibScalar
sleRouteControlDstMask = _SleRouteControlDstMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 7),
    _SleRouteControlDstMask_Type()
)
sleRouteControlDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlDstMask.setStatus("current")
_SleRouteControlGateway_Type = IpAddress
_SleRouteControlGateway_Object = MibScalar
sleRouteControlGateway = _SleRouteControlGateway_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 8),
    _SleRouteControlGateway_Type()
)
sleRouteControlGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlGateway.setStatus("current")


class _SleRouteControlInterface_Type(Integer32):
    """Custom type sleRouteControlInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11023),
    )


_SleRouteControlInterface_Type.__name__ = "Integer32"
_SleRouteControlInterface_Object = MibScalar
sleRouteControlInterface = _SleRouteControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 9),
    _SleRouteControlInterface_Type()
)
sleRouteControlInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlInterface.setStatus("current")
_SleRouteControlBindingSrcAddr_Type = IpAddress
_SleRouteControlBindingSrcAddr_Object = MibScalar
sleRouteControlBindingSrcAddr = _SleRouteControlBindingSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 10),
    _SleRouteControlBindingSrcAddr_Type()
)
sleRouteControlBindingSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlBindingSrcAddr.setStatus("current")


class _SleRouteControlDistance_Type(Integer32):
    """Custom type sleRouteControlDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRouteControlDistance_Type.__name__ = "Integer32"
_SleRouteControlDistance_Object = MibScalar
sleRouteControlDistance = _SleRouteControlDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 11),
    _SleRouteControlDistance_Type()
)
sleRouteControlDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlDistance.setStatus("current")


class _SleRouteControlVRFIndex_Type(Integer32):
    """Custom type sleRouteControlVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleRouteControlVRFIndex_Type.__name__ = "Integer32"
_SleRouteControlVRFIndex_Object = MibScalar
sleRouteControlVRFIndex = _SleRouteControlVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 2, 12),
    _SleRouteControlVRFIndex_Type()
)
sleRouteControlVRFIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRouteControlVRFIndex.setStatus("current")
_SleRouteNotification_ObjectIdentity = ObjectIdentity
sleRouteNotification = _SleRouteNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 3)
)
_SleDhcpClient_ObjectIdentity = ObjectIdentity
sleDhcpClient = _SleDhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5)
)
_SleDhcpClTable_Object = MibTable
sleDhcpClTable = _SleDhcpClTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1)
)
if mibBuilder.loadTexts:
    sleDhcpClTable.setStatus("current")
_SleDhcpClEntry_Object = MibTableRow
sleDhcpClEntry = _SleDhcpClEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1)
)
sleDhcpClEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
)
if mibBuilder.loadTexts:
    sleDhcpClEntry.setStatus("current")


class _SleDhcpClMode_Type(Integer32):
    """Custom type sleDhcpClMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpClMode_Type.__name__ = "Integer32"
_SleDhcpClMode_Object = MibTableColumn
sleDhcpClMode = _SleDhcpClMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 1),
    _SleDhcpClMode_Type()
)
sleDhcpClMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClMode.setStatus("current")
_SleDhcpClIpAddr_Type = IpAddress
_SleDhcpClIpAddr_Object = MibTableColumn
sleDhcpClIpAddr = _SleDhcpClIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 2),
    _SleDhcpClIpAddr_Type()
)
sleDhcpClIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClIpAddr.setStatus("current")
_SleDhcpClNetmask_Type = IpAddress
_SleDhcpClNetmask_Object = MibTableColumn
sleDhcpClNetmask = _SleDhcpClNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 3),
    _SleDhcpClNetmask_Type()
)
sleDhcpClNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClNetmask.setStatus("current")
_SleDhcpClGateway_Type = IpAddress
_SleDhcpClGateway_Object = MibTableColumn
sleDhcpClGateway = _SleDhcpClGateway_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 4),
    _SleDhcpClGateway_Type()
)
sleDhcpClGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClGateway.setStatus("current")
_SleDhcpClDnsServer_Type = IpAddress
_SleDhcpClDnsServer_Object = MibTableColumn
sleDhcpClDnsServer = _SleDhcpClDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 5),
    _SleDhcpClDnsServer_Type()
)
sleDhcpClDnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClDnsServer.setStatus("current")
_SleDhcpClServer_Type = IpAddress
_SleDhcpClServer_Object = MibTableColumn
sleDhcpClServer = _SleDhcpClServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 6),
    _SleDhcpClServer_Type()
)
sleDhcpClServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClServer.setStatus("current")


class _SleDhcpClClientId_Type(OctetString):
    """Custom type sleDhcpClClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleDhcpClClientId_Type.__name__ = "OctetString"
_SleDhcpClClientId_Object = MibTableColumn
sleDhcpClClientId = _SleDhcpClClientId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 7),
    _SleDhcpClClientId_Type()
)
sleDhcpClClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClClientId.setStatus("current")


class _SleDhcpClClientIdStyle_Type(Integer32):
    """Custom type sleDhcpClClientIdStyle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("hex", 1))
    )


_SleDhcpClClientIdStyle_Type.__name__ = "Integer32"
_SleDhcpClClientIdStyle_Object = MibTableColumn
sleDhcpClClientIdStyle = _SleDhcpClClientIdStyle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 8),
    _SleDhcpClClientIdStyle_Type()
)
sleDhcpClClientIdStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClClientIdStyle.setStatus("current")


class _SleDhcpClClassId_Type(OctetString):
    """Custom type sleDhcpClClassId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SleDhcpClClassId_Type.__name__ = "OctetString"
_SleDhcpClClassId_Object = MibTableColumn
sleDhcpClClassId = _SleDhcpClClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 9),
    _SleDhcpClClassId_Type()
)
sleDhcpClClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClClassId.setStatus("current")


class _SleDhcpClClassIdStyle_Type(Integer32):
    """Custom type sleDhcpClClassIdStyle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("hex", 1))
    )


_SleDhcpClClassIdStyle_Type.__name__ = "Integer32"
_SleDhcpClClassIdStyle_Object = MibTableColumn
sleDhcpClClassIdStyle = _SleDhcpClClassIdStyle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 10),
    _SleDhcpClClassIdStyle_Type()
)
sleDhcpClClassIdStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClClassIdStyle.setStatus("current")


class _SleDhcpClLeasetime_Type(Integer32):
    """Custom type sleDhcpClLeasetime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcpClLeasetime_Type.__name__ = "Integer32"
_SleDhcpClLeasetime_Object = MibTableColumn
sleDhcpClLeasetime = _SleDhcpClLeasetime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 11),
    _SleDhcpClLeasetime_Type()
)
sleDhcpClLeasetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClLeasetime.setStatus("current")


class _SleDhcpClState_Type(Integer32):
    """Custom type sleDhcpClState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("halt", 0),
          ("init", 1),
          ("request", 3),
          ("bound", 4),
          ("renew", 5),
          ("rebind", 6),
          ("nonactive", 255))
    )


_SleDhcpClState_Type.__name__ = "Integer32"
_SleDhcpClState_Object = MibTableColumn
sleDhcpClState = _SleDhcpClState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 1, 1, 12),
    _SleDhcpClState_Type()
)
sleDhcpClState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClState.setStatus("current")
_SleDhcpClControl_ObjectIdentity = ObjectIdentity
sleDhcpClControl = _SleDhcpClControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2)
)


class _SleDhcpClControlRequest_Type(Integer32):
    """Custom type sleDhcpClControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setDhcpClMode", 1),
          ("setDhcpClProfile", 2),
          ("changeDhcpClState", 3))
    )


_SleDhcpClControlRequest_Type.__name__ = "Integer32"
_SleDhcpClControlRequest_Object = MibScalar
sleDhcpClControlRequest = _SleDhcpClControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 1),
    _SleDhcpClControlRequest_Type()
)
sleDhcpClControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlRequest.setStatus("current")
_SleDhcpClControlStatus_Type = SleControlStatusType
_SleDhcpClControlStatus_Object = MibScalar
sleDhcpClControlStatus = _SleDhcpClControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 2),
    _SleDhcpClControlStatus_Type()
)
sleDhcpClControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClControlStatus.setStatus("current")
_SleDhcpClControlTimer_Type = Gauge32
_SleDhcpClControlTimer_Object = MibScalar
sleDhcpClControlTimer = _SleDhcpClControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 3),
    _SleDhcpClControlTimer_Type()
)
sleDhcpClControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlTimer.setStatus("current")
_SleDhcpClControlTimeStamp_Type = SleControlRequestResultType
_SleDhcpClControlTimeStamp_Object = MibScalar
sleDhcpClControlTimeStamp = _SleDhcpClControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 4),
    _SleDhcpClControlTimeStamp_Type()
)
sleDhcpClControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClControlTimeStamp.setStatus("current")
_SleDhcpClControlReqResult_Type = TimeTicks
_SleDhcpClControlReqResult_Object = MibScalar
sleDhcpClControlReqResult = _SleDhcpClControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 5),
    _SleDhcpClControlReqResult_Type()
)
sleDhcpClControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClControlReqResult.setStatus("current")


class _SleDhcpClControlNetIfIndex_Type(Integer32):
    """Custom type sleDhcpClControlNetIfIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleDhcpClControlNetIfIndex_Type.__name__ = "Integer32"
_SleDhcpClControlNetIfIndex_Object = MibScalar
sleDhcpClControlNetIfIndex = _SleDhcpClControlNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 6),
    _SleDhcpClControlNetIfIndex_Type()
)
sleDhcpClControlNetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlNetIfIndex.setStatus("current")


class _SleDhcpClControlMode_Type(Integer32):
    """Custom type sleDhcpClControlMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpClControlMode_Type.__name__ = "Integer32"
_SleDhcpClControlMode_Object = MibScalar
sleDhcpClControlMode = _SleDhcpClControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 7),
    _SleDhcpClControlMode_Type()
)
sleDhcpClControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlMode.setStatus("current")


class _SleDhcpClControlClientId_Type(OctetString):
    """Custom type sleDhcpClControlClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleDhcpClControlClientId_Type.__name__ = "OctetString"
_SleDhcpClControlClientId_Object = MibScalar
sleDhcpClControlClientId = _SleDhcpClControlClientId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 8),
    _SleDhcpClControlClientId_Type()
)
sleDhcpClControlClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlClientId.setStatus("current")


class _SleDhcpClControlClientIdStyle_Type(Integer32):
    """Custom type sleDhcpClControlClientIdStyle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("hex", 1))
    )


_SleDhcpClControlClientIdStyle_Type.__name__ = "Integer32"
_SleDhcpClControlClientIdStyle_Object = MibScalar
sleDhcpClControlClientIdStyle = _SleDhcpClControlClientIdStyle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 9),
    _SleDhcpClControlClientIdStyle_Type()
)
sleDhcpClControlClientIdStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlClientIdStyle.setStatus("current")


class _SleDhcpClControlClassId_Type(OctetString):
    """Custom type sleDhcpClControlClassId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleDhcpClControlClassId_Type.__name__ = "OctetString"
_SleDhcpClControlClassId_Object = MibScalar
sleDhcpClControlClassId = _SleDhcpClControlClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 10),
    _SleDhcpClControlClassId_Type()
)
sleDhcpClControlClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlClassId.setStatus("current")


class _SleDhcpClControlClassIdStyle_Type(Integer32):
    """Custom type sleDhcpClControlClassIdStyle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("hex", 1))
    )


_SleDhcpClControlClassIdStyle_Type.__name__ = "Integer32"
_SleDhcpClControlClassIdStyle_Object = MibScalar
sleDhcpClControlClassIdStyle = _SleDhcpClControlClassIdStyle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 11),
    _SleDhcpClControlClassIdStyle_Type()
)
sleDhcpClControlClassIdStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlClassIdStyle.setStatus("current")


class _SleDhcpClControlLeasetime_Type(Integer32):
    """Custom type sleDhcpClControlLeasetime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcpClControlLeasetime_Type.__name__ = "Integer32"
_SleDhcpClControlLeasetime_Object = MibScalar
sleDhcpClControlLeasetime = _SleDhcpClControlLeasetime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 12),
    _SleDhcpClControlLeasetime_Type()
)
sleDhcpClControlLeasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlLeasetime.setStatus("current")


class _SleDhcpClControlUpdateIP_Type(Integer32):
    """Custom type sleDhcpClControlUpdateIP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remain", 0),
          ("renew", 1),
          ("release", 2))
    )


_SleDhcpClControlUpdateIP_Type.__name__ = "Integer32"
_SleDhcpClControlUpdateIP_Object = MibScalar
sleDhcpClControlUpdateIP = _SleDhcpClControlUpdateIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 2, 13),
    _SleDhcpClControlUpdateIP_Type()
)
sleDhcpClControlUpdateIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpClControlUpdateIP.setStatus("current")
_SleDhcpClNotification_ObjectIdentity = ObjectIdentity
sleDhcpClNotification = _SleDhcpClNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 3)
)
_SleV2DhcpClient_ObjectIdentity = ObjectIdentity
sleV2DhcpClient = _SleV2DhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 6)
)
_SleNetworkBase_ObjectIdentity = ObjectIdentity
sleNetworkBase = _SleNetworkBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7)
)
_SleNetworkBaseInfo_ObjectIdentity = ObjectIdentity
sleNetworkBaseInfo = _SleNetworkBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 1)
)


class _SleNetworkArpAgingTime_Type(Integer32):
    """Custom type sleNetworkArpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483637),
    )


_SleNetworkArpAgingTime_Type.__name__ = "Integer32"
_SleNetworkArpAgingTime_Object = MibScalar
sleNetworkArpAgingTime = _SleNetworkArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 1, 1),
    _SleNetworkArpAgingTime_Type()
)
sleNetworkArpAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkArpAgingTime.setStatus("current")


class _SleNetworkBaseVrfDynamicForwardBinding_Type(Integer32):
    """Custom type sleNetworkBaseVrfDynamicForwardBinding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("vrrp", 1))
    )


_SleNetworkBaseVrfDynamicForwardBinding_Type.__name__ = "Integer32"
_SleNetworkBaseVrfDynamicForwardBinding_Object = MibScalar
sleNetworkBaseVrfDynamicForwardBinding = _SleNetworkBaseVrfDynamicForwardBinding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 1, 2),
    _SleNetworkBaseVrfDynamicForwardBinding_Type()
)
sleNetworkBaseVrfDynamicForwardBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkBaseVrfDynamicForwardBinding.setStatus("current")
_SleNetworkBaseControl_ObjectIdentity = ObjectIdentity
sleNetworkBaseControl = _SleNetworkBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2)
)


class _SleNetworkControlRequest_Type(Integer32):
    """Custom type sleNetworkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setArpProfile", 1),
          ("setVrfForwdDynamicStatus", 2))
    )


_SleNetworkControlRequest_Type.__name__ = "Integer32"
_SleNetworkControlRequest_Object = MibScalar
sleNetworkControlRequest = _SleNetworkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2, 1),
    _SleNetworkControlRequest_Type()
)
sleNetworkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkControlRequest.setStatus("current")
_SleNetworkControlStatus_Type = SleControlStatusType
_SleNetworkControlStatus_Object = MibScalar
sleNetworkControlStatus = _SleNetworkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2, 2),
    _SleNetworkControlStatus_Type()
)
sleNetworkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkControlStatus.setStatus("current")
_SleNetworkControlTimer_Type = Gauge32
_SleNetworkControlTimer_Object = MibScalar
sleNetworkControlTimer = _SleNetworkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2, 3),
    _SleNetworkControlTimer_Type()
)
sleNetworkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkControlTimer.setStatus("current")
_SleNetworkControlTimeStamp_Type = TimeTicks
_SleNetworkControlTimeStamp_Object = MibScalar
sleNetworkControlTimeStamp = _SleNetworkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2, 4),
    _SleNetworkControlTimeStamp_Type()
)
sleNetworkControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkControlTimeStamp.setStatus("current")
_SleNetworkControlReqResult_Type = SleControlRequestResultType
_SleNetworkControlReqResult_Object = MibScalar
sleNetworkControlReqResult = _SleNetworkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2, 5),
    _SleNetworkControlReqResult_Type()
)
sleNetworkControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkControlReqResult.setStatus("current")


class _SleNetworkControlArpAgingTime_Type(Integer32):
    """Custom type sleNetworkControlArpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483637),
    )


_SleNetworkControlArpAgingTime_Type.__name__ = "Integer32"
_SleNetworkControlArpAgingTime_Object = MibScalar
sleNetworkControlArpAgingTime = _SleNetworkControlArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2, 6),
    _SleNetworkControlArpAgingTime_Type()
)
sleNetworkControlArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkControlArpAgingTime.setStatus("current")


class _SleNetworkControlVrfDynamicForwardBinding_Type(Integer32):
    """Custom type sleNetworkControlVrfDynamicForwardBinding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("vrrp", 1))
    )


_SleNetworkControlVrfDynamicForwardBinding_Type.__name__ = "Integer32"
_SleNetworkControlVrfDynamicForwardBinding_Object = MibScalar
sleNetworkControlVrfDynamicForwardBinding = _SleNetworkControlVrfDynamicForwardBinding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 2, 7),
    _SleNetworkControlVrfDynamicForwardBinding_Type()
)
sleNetworkControlVrfDynamicForwardBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkControlVrfDynamicForwardBinding.setStatus("current")
_SleNetworkBaseNotification_ObjectIdentity = ObjectIdentity
sleNetworkBaseNotification = _SleNetworkBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 3)
)
_SleTunnel_ObjectIdentity = ObjectIdentity
sleTunnel = _SleTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8)
)
_SleTunnelIfTable_Object = MibTable
sleTunnelIfTable = _SleTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1)
)
if mibBuilder.loadTexts:
    sleTunnelIfTable.setStatus("current")
_SleTunnelIfEntry_Object = MibTableRow
sleTunnelIfEntry = _SleTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1)
)
sleTunnelIfEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    sleTunnelIfEntry.setStatus("current")


class _SleTunnelIfIndex_Type(Integer32):
    """Custom type sleTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 11023),
    )


_SleTunnelIfIndex_Type.__name__ = "Integer32"
_SleTunnelIfIndex_Object = MibTableColumn
sleTunnelIfIndex = _SleTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 1),
    _SleTunnelIfIndex_Type()
)
sleTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfIndex.setStatus("current")
_SleTunnelIfLocalAddress_Type = IpAddress
_SleTunnelIfLocalAddress_Object = MibTableColumn
sleTunnelIfLocalAddress = _SleTunnelIfLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 2),
    _SleTunnelIfLocalAddress_Type()
)
sleTunnelIfLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfLocalAddress.setStatus("current")
_SleTunnelIfRemoteAddress_Type = IpAddress
_SleTunnelIfRemoteAddress_Object = MibTableColumn
sleTunnelIfRemoteAddress = _SleTunnelIfRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 3),
    _SleTunnelIfRemoteAddress_Type()
)
sleTunnelIfRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfRemoteAddress.setStatus("current")
_SleTunnelIfMode_Type = IANAtunnelType
_SleTunnelIfMode_Object = MibTableColumn
sleTunnelIfMode = _SleTunnelIfMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 4),
    _SleTunnelIfMode_Type()
)
sleTunnelIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfMode.setStatus("current")


class _SleTunnelIfTTL_Type(Integer32):
    """Custom type sleTunnelIfTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleTunnelIfTTL_Type.__name__ = "Integer32"
_SleTunnelIfTTL_Object = MibTableColumn
sleTunnelIfTTL = _SleTunnelIfTTL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 5),
    _SleTunnelIfTTL_Type()
)
sleTunnelIfTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfTTL.setStatus("current")


class _SleTunnelIfDscpMode_Type(Integer32):
    """Custom type sleTunnelIfDscpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscpAssign", 1),
          ("dscpCopyFromPacket", 2),
          ("dscpMapFromPacket", 3))
    )


_SleTunnelIfDscpMode_Type.__name__ = "Integer32"
_SleTunnelIfDscpMode_Object = MibTableColumn
sleTunnelIfDscpMode = _SleTunnelIfDscpMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 6),
    _SleTunnelIfDscpMode_Type()
)
sleTunnelIfDscpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfDscpMode.setStatus("current")


class _SleTunnelIfDscp_Type(Integer32):
    """Custom type sleTunnelIfDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleTunnelIfDscp_Type.__name__ = "Integer32"
_SleTunnelIfDscp_Object = MibTableColumn
sleTunnelIfDscp = _SleTunnelIfDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 7),
    _SleTunnelIfDscp_Type()
)
sleTunnelIfDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfDscp.setStatus("current")


class _SleTunnelIfKeepaliveInterval_Type(Integer32):
    """Custom type sleTunnelIfKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SleTunnelIfKeepaliveInterval_Type.__name__ = "Integer32"
_SleTunnelIfKeepaliveInterval_Object = MibTableColumn
sleTunnelIfKeepaliveInterval = _SleTunnelIfKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 8),
    _SleTunnelIfKeepaliveInterval_Type()
)
sleTunnelIfKeepaliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfKeepaliveInterval.setStatus("current")


class _SleTunnelIfKeepaliveRetry_Type(Integer32):
    """Custom type sleTunnelIfKeepaliveRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleTunnelIfKeepaliveRetry_Type.__name__ = "Integer32"
_SleTunnelIfKeepaliveRetry_Object = MibTableColumn
sleTunnelIfKeepaliveRetry = _SleTunnelIfKeepaliveRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 9),
    _SleTunnelIfKeepaliveRetry_Type()
)
sleTunnelIfKeepaliveRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfKeepaliveRetry.setStatus("current")


class _SleTunnelIfPathMtuDiscovery_Type(Integer32):
    """Custom type sleTunnelIfPathMtuDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleTunnelIfPathMtuDiscovery_Type.__name__ = "Integer32"
_SleTunnelIfPathMtuDiscovery_Object = MibTableColumn
sleTunnelIfPathMtuDiscovery = _SleTunnelIfPathMtuDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 10),
    _SleTunnelIfPathMtuDiscovery_Type()
)
sleTunnelIfPathMtuDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfPathMtuDiscovery.setStatus("current")


class _SleTunnelIfVRFName_Type(OctetString):
    """Custom type sleTunnelIfVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleTunnelIfVRFName_Type.__name__ = "OctetString"
_SleTunnelIfVRFName_Object = MibTableColumn
sleTunnelIfVRFName = _SleTunnelIfVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 11),
    _SleTunnelIfVRFName_Type()
)
sleTunnelIfVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfVRFName.setStatus("current")
_SleTunnelIfBindingPorts_Type = OctetString
_SleTunnelIfBindingPorts_Object = MibTableColumn
sleTunnelIfBindingPorts = _SleTunnelIfBindingPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 12),
    _SleTunnelIfBindingPorts_Type()
)
sleTunnelIfBindingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfBindingPorts.setStatus("current")
_SleTunnelIfLocalAddress6_Type = InetAddress
_SleTunnelIfLocalAddress6_Object = MibTableColumn
sleTunnelIfLocalAddress6 = _SleTunnelIfLocalAddress6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 13),
    _SleTunnelIfLocalAddress6_Type()
)
sleTunnelIfLocalAddress6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfLocalAddress6.setStatus("current")
_SleTunnelIfRemoteAddress6_Type = InetAddress
_SleTunnelIfRemoteAddress6_Object = MibTableColumn
sleTunnelIfRemoteAddress6 = _SleTunnelIfRemoteAddress6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 14),
    _SleTunnelIfRemoteAddress6_Type()
)
sleTunnelIfRemoteAddress6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfRemoteAddress6.setStatus("current")


class _SleTunnelIfChecksum_Type(Integer32):
    """Custom type sleTunnelIfChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleTunnelIfChecksum_Type.__name__ = "Integer32"
_SleTunnelIfChecksum_Object = MibTableColumn
sleTunnelIfChecksum = _SleTunnelIfChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 15),
    _SleTunnelIfChecksum_Type()
)
sleTunnelIfChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfChecksum.setStatus("current")
_SleTunnelIfDmac_Type = MacAddress
_SleTunnelIfDmac_Object = MibTableColumn
sleTunnelIfDmac = _SleTunnelIfDmac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 16),
    _SleTunnelIfDmac_Type()
)
sleTunnelIfDmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfDmac.setStatus("current")


class _SleTunnelIfTos_Type(Integer32):
    """Custom type sleTunnelIfTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleTunnelIfTos_Type.__name__ = "Integer32"
_SleTunnelIfTos_Object = MibTableColumn
sleTunnelIfTos = _SleTunnelIfTos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 1, 1, 17),
    _SleTunnelIfTos_Type()
)
sleTunnelIfTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfTos.setStatus("current")
_SleTunnelIfControl_ObjectIdentity = ObjectIdentity
sleTunnelIfControl = _SleTunnelIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2)
)


class _SleTunnelIfControlRequest_Type(Integer32):
    """Custom type sleTunnelIfControlRequest based on Integer32"""
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
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("createTunnelInterface", 1),
          ("deleteTunnelInterface", 2),
          ("setTunnelIfLocalAddress", 3),
          ("setTunnelIfRemoteAddress", 4),
          ("setTunnelIfMode", 5),
          ("setTunnelIfTTL", 6),
          ("setTunnelIfDscp", 7),
          ("setTunnelIfKeepalive", 8),
          ("setTunnelIfPathMtuDiscovery", 9),
          ("setTunnelIfVRFName", 10),
          ("unsetTunnelIfVRFName", 11),
          ("setTunnelLocalAddr6", 12),
          ("setTunnelRemoteAddr6", 13),
          ("setTunnelChecksum", 14),
          ("setTunnelDmac", 15),
          ("setTunnelTos", 16))
    )


_SleTunnelIfControlRequest_Type.__name__ = "Integer32"
_SleTunnelIfControlRequest_Object = MibScalar
sleTunnelIfControlRequest = _SleTunnelIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 1),
    _SleTunnelIfControlRequest_Type()
)
sleTunnelIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlRequest.setStatus("current")
_SleTunnelIfControlStatus_Type = SleControlStatusType
_SleTunnelIfControlStatus_Object = MibScalar
sleTunnelIfControlStatus = _SleTunnelIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 2),
    _SleTunnelIfControlStatus_Type()
)
sleTunnelIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfControlStatus.setStatus("current")
_SleTunnelIfControlTimer_Type = Gauge32
_SleTunnelIfControlTimer_Object = MibScalar
sleTunnelIfControlTimer = _SleTunnelIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 3),
    _SleTunnelIfControlTimer_Type()
)
sleTunnelIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlTimer.setStatus("current")
_SleTunnelIfControlTimeStamp_Type = SleControlRequestResultType
_SleTunnelIfControlTimeStamp_Object = MibScalar
sleTunnelIfControlTimeStamp = _SleTunnelIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 4),
    _SleTunnelIfControlTimeStamp_Type()
)
sleTunnelIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfControlTimeStamp.setStatus("current")
_SleTunnelIfControlReqResult_Type = TimeTicks
_SleTunnelIfControlReqResult_Object = MibScalar
sleTunnelIfControlReqResult = _SleTunnelIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 5),
    _SleTunnelIfControlReqResult_Type()
)
sleTunnelIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIfControlReqResult.setStatus("current")


class _SleTunnelIfControlIndex_Type(Integer32):
    """Custom type sleTunnelIfControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 11023),
    )


_SleTunnelIfControlIndex_Type.__name__ = "Integer32"
_SleTunnelIfControlIndex_Object = MibScalar
sleTunnelIfControlIndex = _SleTunnelIfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 6),
    _SleTunnelIfControlIndex_Type()
)
sleTunnelIfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlIndex.setStatus("current")
_SleTunnelIfControlLocalAddress_Type = IpAddress
_SleTunnelIfControlLocalAddress_Object = MibScalar
sleTunnelIfControlLocalAddress = _SleTunnelIfControlLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 7),
    _SleTunnelIfControlLocalAddress_Type()
)
sleTunnelIfControlLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlLocalAddress.setStatus("current")
_SleTunnelIfControlRemoteAddress_Type = IpAddress
_SleTunnelIfControlRemoteAddress_Object = MibScalar
sleTunnelIfControlRemoteAddress = _SleTunnelIfControlRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 8),
    _SleTunnelIfControlRemoteAddress_Type()
)
sleTunnelIfControlRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlRemoteAddress.setStatus("current")
_SleTunnelIfControlMode_Type = IANAtunnelType
_SleTunnelIfControlMode_Object = MibScalar
sleTunnelIfControlMode = _SleTunnelIfControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 9),
    _SleTunnelIfControlMode_Type()
)
sleTunnelIfControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlMode.setStatus("current")


class _SleTunnelIfControlTTL_Type(Integer32):
    """Custom type sleTunnelIfControlTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleTunnelIfControlTTL_Type.__name__ = "Integer32"
_SleTunnelIfControlTTL_Object = MibScalar
sleTunnelIfControlTTL = _SleTunnelIfControlTTL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 10),
    _SleTunnelIfControlTTL_Type()
)
sleTunnelIfControlTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlTTL.setStatus("current")


class _SleTunneIflControlDscpMode_Type(Integer32):
    """Custom type sleTunneIflControlDscpMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscpAssign", 1),
          ("dscpCopyFromPacket", 2),
          ("dscpMapFromPacket", 3))
    )


_SleTunneIflControlDscpMode_Type.__name__ = "Integer32"
_SleTunneIflControlDscpMode_Object = MibScalar
sleTunneIflControlDscpMode = _SleTunneIflControlDscpMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 11),
    _SleTunneIflControlDscpMode_Type()
)
sleTunneIflControlDscpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunneIflControlDscpMode.setStatus("current")


class _SleTunneIflControlDscp_Type(Integer32):
    """Custom type sleTunneIflControlDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleTunneIflControlDscp_Type.__name__ = "Integer32"
_SleTunneIflControlDscp_Object = MibScalar
sleTunneIflControlDscp = _SleTunneIflControlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 12),
    _SleTunneIflControlDscp_Type()
)
sleTunneIflControlDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunneIflControlDscp.setStatus("current")


class _SleTunnelIfControlKeepaliveInterval_Type(Integer32):
    """Custom type sleTunnelIfControlKeepaliveInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SleTunnelIfControlKeepaliveInterval_Type.__name__ = "Integer32"
_SleTunnelIfControlKeepaliveInterval_Object = MibScalar
sleTunnelIfControlKeepaliveInterval = _SleTunnelIfControlKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 13),
    _SleTunnelIfControlKeepaliveInterval_Type()
)
sleTunnelIfControlKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlKeepaliveInterval.setStatus("current")


class _SleTunneIflControlKeepaliveRetry_Type(Integer32):
    """Custom type sleTunneIflControlKeepaliveRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleTunneIflControlKeepaliveRetry_Type.__name__ = "Integer32"
_SleTunneIflControlKeepaliveRetry_Object = MibScalar
sleTunneIflControlKeepaliveRetry = _SleTunneIflControlKeepaliveRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 14),
    _SleTunneIflControlKeepaliveRetry_Type()
)
sleTunneIflControlKeepaliveRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunneIflControlKeepaliveRetry.setStatus("current")


class _SleTunnelIfControlPathMtuDiscovery_Type(Integer32):
    """Custom type sleTunnelIfControlPathMtuDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleTunnelIfControlPathMtuDiscovery_Type.__name__ = "Integer32"
_SleTunnelIfControlPathMtuDiscovery_Object = MibScalar
sleTunnelIfControlPathMtuDiscovery = _SleTunnelIfControlPathMtuDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 15),
    _SleTunnelIfControlPathMtuDiscovery_Type()
)
sleTunnelIfControlPathMtuDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlPathMtuDiscovery.setStatus("current")


class _SleTunnelIfControlVRFName_Type(OctetString):
    """Custom type sleTunnelIfControlVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleTunnelIfControlVRFName_Type.__name__ = "OctetString"
_SleTunnelIfControlVRFName_Object = MibScalar
sleTunnelIfControlVRFName = _SleTunnelIfControlVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 16),
    _SleTunnelIfControlVRFName_Type()
)
sleTunnelIfControlVRFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlVRFName.setStatus("current")
_SleTunnelIfControlLocalAddress6_Type = InetAddress
_SleTunnelIfControlLocalAddress6_Object = MibScalar
sleTunnelIfControlLocalAddress6 = _SleTunnelIfControlLocalAddress6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 17),
    _SleTunnelIfControlLocalAddress6_Type()
)
sleTunnelIfControlLocalAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlLocalAddress6.setStatus("current")
_SleTunnelIfControlRemoteAddress6_Type = InetAddress
_SleTunnelIfControlRemoteAddress6_Object = MibScalar
sleTunnelIfControlRemoteAddress6 = _SleTunnelIfControlRemoteAddress6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 18),
    _SleTunnelIfControlRemoteAddress6_Type()
)
sleTunnelIfControlRemoteAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlRemoteAddress6.setStatus("current")


class _SleTunnelIfControlChecksum_Type(Integer32):
    """Custom type sleTunnelIfControlChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleTunnelIfControlChecksum_Type.__name__ = "Integer32"
_SleTunnelIfControlChecksum_Object = MibScalar
sleTunnelIfControlChecksum = _SleTunnelIfControlChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 19),
    _SleTunnelIfControlChecksum_Type()
)
sleTunnelIfControlChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlChecksum.setStatus("current")
_SleTunnelIfControlDmac_Type = MacAddress
_SleTunnelIfControlDmac_Object = MibScalar
sleTunnelIfControlDmac = _SleTunnelIfControlDmac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 20),
    _SleTunnelIfControlDmac_Type()
)
sleTunnelIfControlDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlDmac.setStatus("current")


class _SleTunnelIfControlTos_Type(Integer32):
    """Custom type sleTunnelIfControlTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleTunnelIfControlTos_Type.__name__ = "Integer32"
_SleTunnelIfControlTos_Object = MibScalar
sleTunnelIfControlTos = _SleTunnelIfControlTos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 2, 21),
    _SleTunnelIfControlTos_Type()
)
sleTunnelIfControlTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelIfControlTos.setStatus("current")
_SleTunnelIfNotification_ObjectIdentity = ObjectIdentity
sleTunnelIfNotification = _SleTunnelIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3)
)
_SleTunnelAddressTable_Object = MibTable
sleTunnelAddressTable = _SleTunnelAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4)
)
if mibBuilder.loadTexts:
    sleTunnelAddressTable.setStatus("current")
_SleTunnelAddressEntry_Object = MibTableRow
sleTunnelAddressEntry = _SleTunnelAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1)
)
sleTunnelAddressEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleTunnelIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleTunnelAddressValue"),
)
if mibBuilder.loadTexts:
    sleTunnelAddressEntry.setStatus("current")
_SleTunnelAddressValue_Type = IpAddress
_SleTunnelAddressValue_Object = MibTableColumn
sleTunnelAddressValue = _SleTunnelAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1, 1),
    _SleTunnelAddressValue_Type()
)
sleTunnelAddressValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressValue.setStatus("current")


class _SleTunnelAddressMask_Type(Integer32):
    """Custom type sleTunnelAddressMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleTunnelAddressMask_Type.__name__ = "Integer32"
_SleTunnelAddressMask_Object = MibTableColumn
sleTunnelAddressMask = _SleTunnelAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1, 2),
    _SleTunnelAddressMask_Type()
)
sleTunnelAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressMask.setStatus("current")
_SleTunnelIpAddrBcast_Type = IpAddress
_SleTunnelIpAddrBcast_Object = MibTableColumn
sleTunnelIpAddrBcast = _SleTunnelIpAddrBcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1, 3),
    _SleTunnelIpAddrBcast_Type()
)
sleTunnelIpAddrBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelIpAddrBcast.setStatus("current")


class _SleTunnelAddressFlag_Type(Bits):
    """Custom type sleTunnelAddressFlag based on Bits"""
    namedValues = NamedValues(
        *(("permanent", 0),
          ("tentative", 1),
          ("deprecated", 2),
          ("anycast", 3),
          ("reserved1", 4),
          ("reserved2", 5),
          ("reserved3", 6),
          ("secondary", 7))
    )

_SleTunnelAddressFlag_Type.__name__ = "Bits"
_SleTunnelAddressFlag_Object = MibTableColumn
sleTunnelAddressFlag = _SleTunnelAddressFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1, 4),
    _SleTunnelAddressFlag_Type()
)
sleTunnelAddressFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressFlag.setStatus("current")


class _SleTunnelAddressScope_Type(Integer32):
    """Custom type sleTunnelAddressScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleTunnelAddressScope_Type.__name__ = "Integer32"
_SleTunnelAddressScope_Object = MibTableColumn
sleTunnelAddressScope = _SleTunnelAddressScope_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1, 5),
    _SleTunnelAddressScope_Type()
)
sleTunnelAddressScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressScope.setStatus("current")


class _SleTunnelAddressUnnumIfIndex_Type(Integer32):
    """Custom type sleTunnelAddressUnnumIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleTunnelAddressUnnumIfIndex_Type.__name__ = "Integer32"
_SleTunnelAddressUnnumIfIndex_Object = MibTableColumn
sleTunnelAddressUnnumIfIndex = _SleTunnelAddressUnnumIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1, 6),
    _SleTunnelAddressUnnumIfIndex_Type()
)
sleTunnelAddressUnnumIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressUnnumIfIndex.setStatus("current")


class _SleTunnelAddressUnnumIpIndex_Type(Integer32):
    """Custom type sleTunnelAddressUnnumIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 1024),
    )


_SleTunnelAddressUnnumIpIndex_Type.__name__ = "Integer32"
_SleTunnelAddressUnnumIpIndex_Object = MibTableColumn
sleTunnelAddressUnnumIpIndex = _SleTunnelAddressUnnumIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 4, 1, 7),
    _SleTunnelAddressUnnumIpIndex_Type()
)
sleTunnelAddressUnnumIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressUnnumIpIndex.setStatus("current")
_SleTunnelAddressControl_ObjectIdentity = ObjectIdentity
sleTunnelAddressControl = _SleTunnelAddressControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5)
)


class _SleTunnelAddressControlRequest_Type(Integer32):
    """Custom type sleTunnelAddressControlRequest based on Integer32"""
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
        *(("createTunnelIpAddress", 1),
          ("destroyTunnelIpAddress", 2),
          ("setIfUnnumbered", 3),
          ("delIfUnnumbered", 4))
    )


_SleTunnelAddressControlRequest_Type.__name__ = "Integer32"
_SleTunnelAddressControlRequest_Object = MibScalar
sleTunnelAddressControlRequest = _SleTunnelAddressControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 1),
    _SleTunnelAddressControlRequest_Type()
)
sleTunnelAddressControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlRequest.setStatus("current")
_SleTunnelAddressControlStatus_Type = SleControlStatusType
_SleTunnelAddressControlStatus_Object = MibScalar
sleTunnelAddressControlStatus = _SleTunnelAddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 2),
    _SleTunnelAddressControlStatus_Type()
)
sleTunnelAddressControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressControlStatus.setStatus("current")
_SleTunnelAddressControlTimer_Type = Gauge32
_SleTunnelAddressControlTimer_Object = MibScalar
sleTunnelAddressControlTimer = _SleTunnelAddressControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 3),
    _SleTunnelAddressControlTimer_Type()
)
sleTunnelAddressControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlTimer.setStatus("current")
_SleTunnelAddressControlTimeStamp_Type = SleControlRequestResultType
_SleTunnelAddressControlTimeStamp_Object = MibScalar
sleTunnelAddressControlTimeStamp = _SleTunnelAddressControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 4),
    _SleTunnelAddressControlTimeStamp_Type()
)
sleTunnelAddressControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressControlTimeStamp.setStatus("current")
_SleTunnelAddressControlReqResult_Type = TimeTicks
_SleTunnelAddressControlReqResult_Object = MibScalar
sleTunnelAddressControlReqResult = _SleTunnelAddressControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 5),
    _SleTunnelAddressControlReqResult_Type()
)
sleTunnelAddressControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTunnelAddressControlReqResult.setStatus("current")


class _SleTunnelAddressControlTunnelIfIndex_Type(Integer32):
    """Custom type sleTunnelAddressControlTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 11023),
    )


_SleTunnelAddressControlTunnelIfIndex_Type.__name__ = "Integer32"
_SleTunnelAddressControlTunnelIfIndex_Object = MibScalar
sleTunnelAddressControlTunnelIfIndex = _SleTunnelAddressControlTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 6),
    _SleTunnelAddressControlTunnelIfIndex_Type()
)
sleTunnelAddressControlTunnelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlTunnelIfIndex.setStatus("current")
_SleTunnelAddressControlValue_Type = IpAddress
_SleTunnelAddressControlValue_Object = MibScalar
sleTunnelAddressControlValue = _SleTunnelAddressControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 7),
    _SleTunnelAddressControlValue_Type()
)
sleTunnelAddressControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlValue.setStatus("current")


class _SleTunnelAddressControlMask_Type(Integer32):
    """Custom type sleTunnelAddressControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleTunnelAddressControlMask_Type.__name__ = "Integer32"
_SleTunnelAddressControlMask_Object = MibScalar
sleTunnelAddressControlMask = _SleTunnelAddressControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 8),
    _SleTunnelAddressControlMask_Type()
)
sleTunnelAddressControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlMask.setStatus("current")


class _SleTunnelAddressControlFlag_Type(Integer32):
    """Custom type sleTunnelAddressControlFlag based on Integer32"""
    defaultValue = 1

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
        *(("primary", 1),
          ("secondary", 2),
          ("anycast", 3),
          ("unicast", 4))
    )


_SleTunnelAddressControlFlag_Type.__name__ = "Integer32"
_SleTunnelAddressControlFlag_Object = MibScalar
sleTunnelAddressControlFlag = _SleTunnelAddressControlFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 9),
    _SleTunnelAddressControlFlag_Type()
)
sleTunnelAddressControlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlFlag.setStatus("current")


class _SleTunnelAddressControlScope_Type(Integer32):
    """Custom type sleTunnelAddressControlScope based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              253,
              254)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("link", 253),
          ("host", 254))
    )


_SleTunnelAddressControlScope_Type.__name__ = "Integer32"
_SleTunnelAddressControlScope_Object = MibScalar
sleTunnelAddressControlScope = _SleTunnelAddressControlScope_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 10),
    _SleTunnelAddressControlScope_Type()
)
sleTunnelAddressControlScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlScope.setStatus("current")


class _SleTunnelAddressControlUnnumIfIndex_Type(Integer32):
    """Custom type sleTunnelAddressControlUnnumIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleTunnelAddressControlUnnumIfIndex_Type.__name__ = "Integer32"
_SleTunnelAddressControlUnnumIfIndex_Object = MibScalar
sleTunnelAddressControlUnnumIfIndex = _SleTunnelAddressControlUnnumIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 11),
    _SleTunnelAddressControlUnnumIfIndex_Type()
)
sleTunnelAddressControlUnnumIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlUnnumIfIndex.setStatus("current")


class _SleTunnelAddressControlUnnumIpIndex_Type(Integer32):
    """Custom type sleTunnelAddressControlUnnumIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 1024),
    )


_SleTunnelAddressControlUnnumIpIndex_Type.__name__ = "Integer32"
_SleTunnelAddressControlUnnumIpIndex_Object = MibScalar
sleTunnelAddressControlUnnumIpIndex = _SleTunnelAddressControlUnnumIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 5, 12),
    _SleTunnelAddressControlUnnumIpIndex_Type()
)
sleTunnelAddressControlUnnumIpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTunnelAddressControlUnnumIpIndex.setStatus("current")
_SleTunnelAddressNotification_ObjectIdentity = ObjectIdentity
sleTunnelAddressNotification = _SleTunnelAddressNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 6)
)
_SleIpVRF_ObjectIdentity = ObjectIdentity
sleIpVRF = _SleIpVRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9)
)
_SleIpVRFTable_Object = MibTable
sleIpVRFTable = _SleIpVRFTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 1)
)
if mibBuilder.loadTexts:
    sleIpVRFTable.setStatus("current")
_SleIpVRFEntry_Object = MibTableRow
sleIpVRFEntry = _SleIpVRFEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 1, 1)
)
sleIpVRFEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleIpVRFIndex"),
)
if mibBuilder.loadTexts:
    sleIpVRFEntry.setStatus("current")


class _SleIpVRFIndex_Type(Integer32):
    """Custom type sleIpVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleIpVRFIndex_Type.__name__ = "Integer32"
_SleIpVRFIndex_Object = MibTableColumn
sleIpVRFIndex = _SleIpVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 1, 1, 1),
    _SleIpVRFIndex_Type()
)
sleIpVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFIndex.setStatus("current")


class _SleIpVRFName_Type(OctetString):
    """Custom type sleIpVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleIpVRFName_Type.__name__ = "OctetString"
_SleIpVRFName_Object = MibTableColumn
sleIpVRFName = _SleIpVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 1, 1, 2),
    _SleIpVRFName_Type()
)
sleIpVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFName.setStatus("current")
_SleIpVRFDesignatedPorts_Type = OctetString
_SleIpVRFDesignatedPorts_Object = MibTableColumn
sleIpVRFDesignatedPorts = _SleIpVRFDesignatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 1, 1, 3),
    _SleIpVRFDesignatedPorts_Type()
)
sleIpVRFDesignatedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFDesignatedPorts.setStatus("current")
_SleIpVRFRouterId_Type = IpAddress
_SleIpVRFRouterId_Object = MibTableColumn
sleIpVRFRouterId = _SleIpVRFRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 1, 1, 4),
    _SleIpVRFRouterId_Type()
)
sleIpVRFRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFRouterId.setStatus("current")


class _SleIpVRFDescription_Type(OctetString):
    """Custom type sleIpVRFDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SleIpVRFDescription_Type.__name__ = "OctetString"
_SleIpVRFDescription_Object = MibTableColumn
sleIpVRFDescription = _SleIpVRFDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 1, 1, 5),
    _SleIpVRFDescription_Type()
)
sleIpVRFDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFDescription.setStatus("current")
_SleIpVRFControl_ObjectIdentity = ObjectIdentity
sleIpVRFControl = _SleIpVRFControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2)
)


class _SleIpVRFControlRequest_Type(Integer32):
    """Custom type sleIpVRFControlRequest based on Integer32"""
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
        *(("createIpVRF", 1),
          ("deleteIpVRF", 2),
          ("setIpVRFDesignatedPorts", 3),
          ("unsetIpVRFDesignatedPorts", 4),
          ("setVRFRouterId", 5),
          ("setVRFDescription", 6))
    )


_SleIpVRFControlRequest_Type.__name__ = "Integer32"
_SleIpVRFControlRequest_Object = MibScalar
sleIpVRFControlRequest = _SleIpVRFControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 1),
    _SleIpVRFControlRequest_Type()
)
sleIpVRFControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFControlRequest.setStatus("current")
_SleIpVRFControlStatus_Type = SleControlStatusType
_SleIpVRFControlStatus_Object = MibScalar
sleIpVRFControlStatus = _SleIpVRFControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 2),
    _SleIpVRFControlStatus_Type()
)
sleIpVRFControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFControlStatus.setStatus("current")
_SleIpVRFControlTimer_Type = Gauge32
_SleIpVRFControlTimer_Object = MibScalar
sleIpVRFControlTimer = _SleIpVRFControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 3),
    _SleIpVRFControlTimer_Type()
)
sleIpVRFControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFControlTimer.setStatus("current")
_SleIpVRFControlTimeStamp_Type = SleControlRequestResultType
_SleIpVRFControlTimeStamp_Object = MibScalar
sleIpVRFControlTimeStamp = _SleIpVRFControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 4),
    _SleIpVRFControlTimeStamp_Type()
)
sleIpVRFControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFControlTimeStamp.setStatus("current")
_SleIpVRFControlReqResult_Type = TimeTicks
_SleIpVRFControlReqResult_Object = MibScalar
sleIpVRFControlReqResult = _SleIpVRFControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 5),
    _SleIpVRFControlReqResult_Type()
)
sleIpVRFControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFControlReqResult.setStatus("current")


class _SleIpVRFControlName_Type(OctetString):
    """Custom type sleIpVRFControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleIpVRFControlName_Type.__name__ = "OctetString"
_SleIpVRFControlName_Object = MibScalar
sleIpVRFControlName = _SleIpVRFControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 6),
    _SleIpVRFControlName_Type()
)
sleIpVRFControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFControlName.setStatus("current")
_SleIpVRFControlDesignatedPorts_Type = OctetString
_SleIpVRFControlDesignatedPorts_Object = MibScalar
sleIpVRFControlDesignatedPorts = _SleIpVRFControlDesignatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 7),
    _SleIpVRFControlDesignatedPorts_Type()
)
sleIpVRFControlDesignatedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFControlDesignatedPorts.setStatus("current")
_SleIpVRFControlRouterId_Type = IpAddress
_SleIpVRFControlRouterId_Object = MibScalar
sleIpVRFControlRouterId = _SleIpVRFControlRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 8),
    _SleIpVRFControlRouterId_Type()
)
sleIpVRFControlRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFControlRouterId.setStatus("current")


class _SleIpVRFControlDescription_Type(OctetString):
    """Custom type sleIpVRFControlDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SleIpVRFControlDescription_Type.__name__ = "OctetString"
_SleIpVRFControlDescription_Object = MibScalar
sleIpVRFControlDescription = _SleIpVRFControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 2, 9),
    _SleIpVRFControlDescription_Type()
)
sleIpVRFControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFControlDescription.setStatus("current")
_SleIpVRFNotification_ObjectIdentity = ObjectIdentity
sleIpVRFNotification = _SleIpVRFNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 3)
)
_SleIpVRFSelectionSourceTable_Object = MibTable
sleIpVRFSelectionSourceTable = _SleIpVRFSelectionSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 4)
)
if mibBuilder.loadTexts:
    sleIpVRFSelectionSourceTable.setStatus("current")
_SleIpVRFSelectionSourceEntry_Object = MibTableRow
sleIpVRFSelectionSourceEntry = _SleIpVRFSelectionSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 4, 1)
)
sleIpVRFSelectionSourceEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleIpVRFSelectionSrcIndex"),
)
if mibBuilder.loadTexts:
    sleIpVRFSelectionSourceEntry.setStatus("current")


class _SleIpVRFSelectionSrcIndex_Type(Integer32):
    """Custom type sleIpVRFSelectionSrcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SleIpVRFSelectionSrcIndex_Type.__name__ = "Integer32"
_SleIpVRFSelectionSrcIndex_Object = MibTableColumn
sleIpVRFSelectionSrcIndex = _SleIpVRFSelectionSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 4, 1, 1),
    _SleIpVRFSelectionSrcIndex_Type()
)
sleIpVRFSelectionSrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcIndex.setStatus("current")
_SleIpVRFSelectionSrcAddr_Type = IpAddress
_SleIpVRFSelectionSrcAddr_Object = MibTableColumn
sleIpVRFSelectionSrcAddr = _SleIpVRFSelectionSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 4, 1, 2),
    _SleIpVRFSelectionSrcAddr_Type()
)
sleIpVRFSelectionSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcAddr.setStatus("current")


class _SleIpVRFSelectionSrcMask_Type(Integer32):
    """Custom type sleIpVRFSelectionSrcMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleIpVRFSelectionSrcMask_Type.__name__ = "Integer32"
_SleIpVRFSelectionSrcMask_Object = MibTableColumn
sleIpVRFSelectionSrcMask = _SleIpVRFSelectionSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 4, 1, 3),
    _SleIpVRFSelectionSrcMask_Type()
)
sleIpVRFSelectionSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcMask.setStatus("current")


class _SleIpVRFSelectionSrcVRFName_Type(OctetString):
    """Custom type sleIpVRFSelectionSrcVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleIpVRFSelectionSrcVRFName_Type.__name__ = "OctetString"
_SleIpVRFSelectionSrcVRFName_Object = MibTableColumn
sleIpVRFSelectionSrcVRFName = _SleIpVRFSelectionSrcVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 4, 1, 4),
    _SleIpVRFSelectionSrcVRFName_Type()
)
sleIpVRFSelectionSrcVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcVRFName.setStatus("current")
_SleIpVRFSelectionSourceControl_ObjectIdentity = ObjectIdentity
sleIpVRFSelectionSourceControl = _SleIpVRFSelectionSourceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5)
)


class _SleIpVRFSelectionSrcControlRequest_Type(Integer32):
    """Custom type sleIpVRFSelectionSrcControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setVRFSelectionSource", 1),
          ("unsetVRFSelectionSource", 2))
    )


_SleIpVRFSelectionSrcControlRequest_Type.__name__ = "Integer32"
_SleIpVRFSelectionSrcControlRequest_Object = MibScalar
sleIpVRFSelectionSrcControlRequest = _SleIpVRFSelectionSrcControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 1),
    _SleIpVRFSelectionSrcControlRequest_Type()
)
sleIpVRFSelectionSrcControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlRequest.setStatus("current")
_SleIpVRFSelectionSrcControlStatus_Type = SleControlStatusType
_SleIpVRFSelectionSrcControlStatus_Object = MibScalar
sleIpVRFSelectionSrcControlStatus = _SleIpVRFSelectionSrcControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 2),
    _SleIpVRFSelectionSrcControlStatus_Type()
)
sleIpVRFSelectionSrcControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlStatus.setStatus("current")
_SleIpVRFSelectionSrcControlTimer_Type = Gauge32
_SleIpVRFSelectionSrcControlTimer_Object = MibScalar
sleIpVRFSelectionSrcControlTimer = _SleIpVRFSelectionSrcControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 3),
    _SleIpVRFSelectionSrcControlTimer_Type()
)
sleIpVRFSelectionSrcControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlTimer.setStatus("current")
_SleIpVRFSelectionSrcControlTimeStamp_Type = SleControlRequestResultType
_SleIpVRFSelectionSrcControlTimeStamp_Object = MibScalar
sleIpVRFSelectionSrcControlTimeStamp = _SleIpVRFSelectionSrcControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 4),
    _SleIpVRFSelectionSrcControlTimeStamp_Type()
)
sleIpVRFSelectionSrcControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlTimeStamp.setStatus("current")
_SleIpVRFSelectionSrcControlReqResult_Type = TimeTicks
_SleIpVRFSelectionSrcControlReqResult_Object = MibScalar
sleIpVRFSelectionSrcControlReqResult = _SleIpVRFSelectionSrcControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 5),
    _SleIpVRFSelectionSrcControlReqResult_Type()
)
sleIpVRFSelectionSrcControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlReqResult.setStatus("current")
_SleIpVRFSelectionSrcControlAddr_Type = IpAddress
_SleIpVRFSelectionSrcControlAddr_Object = MibScalar
sleIpVRFSelectionSrcControlAddr = _SleIpVRFSelectionSrcControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 6),
    _SleIpVRFSelectionSrcControlAddr_Type()
)
sleIpVRFSelectionSrcControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlAddr.setStatus("current")


class _SleIpVRFSelectionSrcControlMask_Type(Integer32):
    """Custom type sleIpVRFSelectionSrcControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleIpVRFSelectionSrcControlMask_Type.__name__ = "Integer32"
_SleIpVRFSelectionSrcControlMask_Object = MibScalar
sleIpVRFSelectionSrcControlMask = _SleIpVRFSelectionSrcControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 7),
    _SleIpVRFSelectionSrcControlMask_Type()
)
sleIpVRFSelectionSrcControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlMask.setStatus("current")


class _SleIpVRFSelectionSrcControlVRFName_Type(OctetString):
    """Custom type sleIpVRFSelectionSrcControlVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleIpVRFSelectionSrcControlVRFName_Type.__name__ = "OctetString"
_SleIpVRFSelectionSrcControlVRFName_Object = MibScalar
sleIpVRFSelectionSrcControlVRFName = _SleIpVRFSelectionSrcControlVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 5, 8),
    _SleIpVRFSelectionSrcControlVRFName_Type()
)
sleIpVRFSelectionSrcControlVRFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcControlVRFName.setStatus("current")
_SleIpVRFSelectionSourceNotification_ObjectIdentity = ObjectIdentity
sleIpVRFSelectionSourceNotification = _SleIpVRFSelectionSourceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 6)
)
_SleBFD_ObjectIdentity = ObjectIdentity
sleBFD = _SleBFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10)
)
_SleBFDBase_ObjectIdentity = ObjectIdentity
sleBFDBase = _SleBFDBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1)
)
_SleBFDBaseInfo_ObjectIdentity = ObjectIdentity
sleBFDBaseInfo = _SleBFDBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 1)
)


class _SleBFDEnable_Type(Integer32):
    """Custom type sleBFDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleBFDEnable_Type.__name__ = "Integer32"
_SleBFDEnable_Object = MibScalar
sleBFDEnable = _SleBFDEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 1, 1),
    _SleBFDEnable_Type()
)
sleBFDEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDEnable.setStatus("current")


class _SleBFDEchoEnable_Type(Integer32):
    """Custom type sleBFDEchoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleBFDEchoEnable_Type.__name__ = "Integer32"
_SleBFDEchoEnable_Object = MibScalar
sleBFDEchoEnable = _SleBFDEchoEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 1, 2),
    _SleBFDEchoEnable_Type()
)
sleBFDEchoEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDEchoEnable.setStatus("current")


class _SleBFDSlowTimer_Type(Integer32):
    """Custom type sleBFDSlowTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_SleBFDSlowTimer_Type.__name__ = "Integer32"
_SleBFDSlowTimer_Object = MibScalar
sleBFDSlowTimer = _SleBFDSlowTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 1, 3),
    _SleBFDSlowTimer_Type()
)
sleBFDSlowTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSlowTimer.setStatus("current")
_SleBFDBaseControl_ObjectIdentity = ObjectIdentity
sleBFDBaseControl = _SleBFDBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2)
)


class _SleBFDControlRequest_Type(Integer32):
    """Custom type sleBFDControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setBFDBaseProfile", 1)
    )


_SleBFDControlRequest_Type.__name__ = "Integer32"
_SleBFDControlRequest_Object = MibScalar
sleBFDControlRequest = _SleBFDControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 1),
    _SleBFDControlRequest_Type()
)
sleBFDControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDControlRequest.setStatus("current")
_SleBFDControlStatus_Type = SleControlStatusType
_SleBFDControlStatus_Object = MibScalar
sleBFDControlStatus = _SleBFDControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 2),
    _SleBFDControlStatus_Type()
)
sleBFDControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDControlStatus.setStatus("current")
_SleBFDControlTimer_Type = Gauge32
_SleBFDControlTimer_Object = MibScalar
sleBFDControlTimer = _SleBFDControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 3),
    _SleBFDControlTimer_Type()
)
sleBFDControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDControlTimer.setStatus("current")
_SleBFDControlTimeStamp_Type = TimeTicks
_SleBFDControlTimeStamp_Object = MibScalar
sleBFDControlTimeStamp = _SleBFDControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 4),
    _SleBFDControlTimeStamp_Type()
)
sleBFDControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDControlTimeStamp.setStatus("current")
_SleBFDControlReqResult_Type = SleControlRequestResultType
_SleBFDControlReqResult_Object = MibScalar
sleBFDControlReqResult = _SleBFDControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 5),
    _SleBFDControlReqResult_Type()
)
sleBFDControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDControlReqResult.setStatus("current")


class _SleBFDControlEnable_Type(Integer32):
    """Custom type sleBFDControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleBFDControlEnable_Type.__name__ = "Integer32"
_SleBFDControlEnable_Object = MibScalar
sleBFDControlEnable = _SleBFDControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 6),
    _SleBFDControlEnable_Type()
)
sleBFDControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDControlEnable.setStatus("current")


class _SleBFDControlEchoEnable_Type(Integer32):
    """Custom type sleBFDControlEchoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleBFDControlEchoEnable_Type.__name__ = "Integer32"
_SleBFDControlEchoEnable_Object = MibScalar
sleBFDControlEchoEnable = _SleBFDControlEchoEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 7),
    _SleBFDControlEchoEnable_Type()
)
sleBFDControlEchoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDControlEchoEnable.setStatus("current")


class _SleBFDControlSlowTimer_Type(Integer32):
    """Custom type sleBFDControlSlowTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_SleBFDControlSlowTimer_Type.__name__ = "Integer32"
_SleBFDControlSlowTimer_Object = MibScalar
sleBFDControlSlowTimer = _SleBFDControlSlowTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 2, 8),
    _SleBFDControlSlowTimer_Type()
)
sleBFDControlSlowTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDControlSlowTimer.setStatus("current")
_SleBFDBaseNotification_ObjectIdentity = ObjectIdentity
sleBFDBaseNotification = _SleBFDBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 3)
)
_SleBFDInterface_ObjectIdentity = ObjectIdentity
sleBFDInterface = _SleBFDInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2)
)
_SleBFDInterfaceTable_Object = MibTable
sleBFDInterfaceTable = _SleBFDInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1)
)
if mibBuilder.loadTexts:
    sleBFDInterfaceTable.setStatus("current")
_SleBFDInterfaceEntry_Object = MibTableRow
sleBFDInterfaceEntry = _SleBFDInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1, 1)
)
sleBFDInterfaceEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
)
if mibBuilder.loadTexts:
    sleBFDInterfaceEntry.setStatus("current")


class _SleBFDIfRxInterval_Type(Integer32):
    """Custom type sleBFDIfRxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_SleBFDIfRxInterval_Type.__name__ = "Integer32"
_SleBFDIfRxInterval_Object = MibTableColumn
sleBFDIfRxInterval = _SleBFDIfRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1, 1, 1),
    _SleBFDIfRxInterval_Type()
)
sleBFDIfRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfRxInterval.setStatus("current")


class _SleBFDIfTxInterval_Type(Integer32):
    """Custom type sleBFDIfTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_SleBFDIfTxInterval_Type.__name__ = "Integer32"
_SleBFDIfTxInterval_Object = MibTableColumn
sleBFDIfTxInterval = _SleBFDIfTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1, 1, 2),
    _SleBFDIfTxInterval_Type()
)
sleBFDIfTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfTxInterval.setStatus("current")


class _SleBFDIfDetectMulti_Type(Integer32):
    """Custom type sleBFDIfDetectMulti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_SleBFDIfDetectMulti_Type.__name__ = "Integer32"
_SleBFDIfDetectMulti_Object = MibTableColumn
sleBFDIfDetectMulti = _SleBFDIfDetectMulti_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1, 1, 3),
    _SleBFDIfDetectMulti_Type()
)
sleBFDIfDetectMulti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfDetectMulti.setStatus("current")


class _SleBFDIfRxIntervalIPv6_Type(Integer32):
    """Custom type sleBFDIfRxIntervalIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_SleBFDIfRxIntervalIPv6_Type.__name__ = "Integer32"
_SleBFDIfRxIntervalIPv6_Object = MibTableColumn
sleBFDIfRxIntervalIPv6 = _SleBFDIfRxIntervalIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1, 1, 4),
    _SleBFDIfRxIntervalIPv6_Type()
)
sleBFDIfRxIntervalIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfRxIntervalIPv6.setStatus("current")


class _SleBFDIfTxIntervalIJPv6_Type(Integer32):
    """Custom type sleBFDIfTxIntervalIJPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_SleBFDIfTxIntervalIJPv6_Type.__name__ = "Integer32"
_SleBFDIfTxIntervalIJPv6_Object = MibTableColumn
sleBFDIfTxIntervalIJPv6 = _SleBFDIfTxIntervalIJPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1, 1, 5),
    _SleBFDIfTxIntervalIJPv6_Type()
)
sleBFDIfTxIntervalIJPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfTxIntervalIJPv6.setStatus("current")


class _SleBFDIfDetectMultiIPv6_Type(Integer32):
    """Custom type sleBFDIfDetectMultiIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_SleBFDIfDetectMultiIPv6_Type.__name__ = "Integer32"
_SleBFDIfDetectMultiIPv6_Object = MibTableColumn
sleBFDIfDetectMultiIPv6 = _SleBFDIfDetectMultiIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 1, 1, 6),
    _SleBFDIfDetectMultiIPv6_Type()
)
sleBFDIfDetectMultiIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfDetectMultiIPv6.setStatus("current")
_SleBFDInterfaceControl_ObjectIdentity = ObjectIdentity
sleBFDInterfaceControl = _SleBFDInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2)
)


class _SleBFDIfControlRequest_Type(Integer32):
    """Custom type sleBFDIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setBFDIfProfile", 1)
    )


_SleBFDIfControlRequest_Type.__name__ = "Integer32"
_SleBFDIfControlRequest_Object = MibScalar
sleBFDIfControlRequest = _SleBFDIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 1),
    _SleBFDIfControlRequest_Type()
)
sleBFDIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlRequest.setStatus("current")
_SleBFDIfControlStatus_Type = SleControlStatusType
_SleBFDIfControlStatus_Object = MibScalar
sleBFDIfControlStatus = _SleBFDIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 2),
    _SleBFDIfControlStatus_Type()
)
sleBFDIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfControlStatus.setStatus("current")
_SleBFDIfControlTimer_Type = Gauge32
_SleBFDIfControlTimer_Object = MibScalar
sleBFDIfControlTimer = _SleBFDIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 3),
    _SleBFDIfControlTimer_Type()
)
sleBFDIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlTimer.setStatus("current")
_SleBFDIfControlTimeStamp_Type = TimeTicks
_SleBFDIfControlTimeStamp_Object = MibScalar
sleBFDIfControlTimeStamp = _SleBFDIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 4),
    _SleBFDIfControlTimeStamp_Type()
)
sleBFDIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfControlTimeStamp.setStatus("current")
_SleBFDIfControlReqResult_Type = SleControlRequestResultType
_SleBFDIfControlReqResult_Object = MibScalar
sleBFDIfControlReqResult = _SleBFDIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 5),
    _SleBFDIfControlReqResult_Type()
)
sleBFDIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDIfControlReqResult.setStatus("current")


class _SleBFDIfControlNetIfIndex_Type(Integer32):
    """Custom type sleBFDIfControlNetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleBFDIfControlNetIfIndex_Type.__name__ = "Integer32"
_SleBFDIfControlNetIfIndex_Object = MibScalar
sleBFDIfControlNetIfIndex = _SleBFDIfControlNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 6),
    _SleBFDIfControlNetIfIndex_Type()
)
sleBFDIfControlNetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlNetIfIndex.setStatus("current")


class _SleBFDIfControlRxInterval_Type(Integer32):
    """Custom type sleBFDIfControlRxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_SleBFDIfControlRxInterval_Type.__name__ = "Integer32"
_SleBFDIfControlRxInterval_Object = MibScalar
sleBFDIfControlRxInterval = _SleBFDIfControlRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 7),
    _SleBFDIfControlRxInterval_Type()
)
sleBFDIfControlRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlRxInterval.setStatus("current")


class _SleBFDIfControlTxInterval_Type(Integer32):
    """Custom type sleBFDIfControlTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_SleBFDIfControlTxInterval_Type.__name__ = "Integer32"
_SleBFDIfControlTxInterval_Object = MibScalar
sleBFDIfControlTxInterval = _SleBFDIfControlTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 8),
    _SleBFDIfControlTxInterval_Type()
)
sleBFDIfControlTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlTxInterval.setStatus("current")


class _SleBFDIfControlDetectMulti_Type(Integer32):
    """Custom type sleBFDIfControlDetectMulti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_SleBFDIfControlDetectMulti_Type.__name__ = "Integer32"
_SleBFDIfControlDetectMulti_Object = MibScalar
sleBFDIfControlDetectMulti = _SleBFDIfControlDetectMulti_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 9),
    _SleBFDIfControlDetectMulti_Type()
)
sleBFDIfControlDetectMulti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlDetectMulti.setStatus("current")


class _SleBFDIfControlRxIntervalIPv6_Type(Integer32):
    """Custom type sleBFDIfControlRxIntervalIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_SleBFDIfControlRxIntervalIPv6_Type.__name__ = "Integer32"
_SleBFDIfControlRxIntervalIPv6_Object = MibScalar
sleBFDIfControlRxIntervalIPv6 = _SleBFDIfControlRxIntervalIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 10),
    _SleBFDIfControlRxIntervalIPv6_Type()
)
sleBFDIfControlRxIntervalIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlRxIntervalIPv6.setStatus("current")


class _SleBFDIfControlTxIntervalIPv6_Type(Integer32):
    """Custom type sleBFDIfControlTxIntervalIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_SleBFDIfControlTxIntervalIPv6_Type.__name__ = "Integer32"
_SleBFDIfControlTxIntervalIPv6_Object = MibScalar
sleBFDIfControlTxIntervalIPv6 = _SleBFDIfControlTxIntervalIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 11),
    _SleBFDIfControlTxIntervalIPv6_Type()
)
sleBFDIfControlTxIntervalIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlTxIntervalIPv6.setStatus("current")


class _SleBFDIfControlDetectMultiIPv6_Type(Integer32):
    """Custom type sleBFDIfControlDetectMultiIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_SleBFDIfControlDetectMultiIPv6_Type.__name__ = "Integer32"
_SleBFDIfControlDetectMultiIPv6_Object = MibScalar
sleBFDIfControlDetectMultiIPv6 = _SleBFDIfControlDetectMultiIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 2, 12),
    _SleBFDIfControlDetectMultiIPv6_Type()
)
sleBFDIfControlDetectMultiIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDIfControlDetectMultiIPv6.setStatus("current")
_SleBFDInterfaceNotification_ObjectIdentity = ObjectIdentity
sleBFDInterfaceNotification = _SleBFDInterfaceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 3)
)
_SleBFDSession_ObjectIdentity = ObjectIdentity
sleBFDSession = _SleBFDSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3)
)
_SleBFDSessionInfo_ObjectIdentity = ObjectIdentity
sleBFDSessionInfo = _SleBFDSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1)
)
_SleBFDSessionInfoTable_Object = MibTable
sleBFDSessionInfoTable = _SleBFDSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleBFDSessionInfoTable.setStatus("current")
_SleBFDSessionInfoEntry_Object = MibTableRow
sleBFDSessionInfoEntry = _SleBFDSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1)
)
sleBFDSessionInfoEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrType"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrValue"),
)
if mibBuilder.loadTexts:
    sleBFDSessionInfoEntry.setStatus("current")
_SleBFDSessionNeighAddrType_Type = InetAddressType
_SleBFDSessionNeighAddrType_Object = MibTableColumn
sleBFDSessionNeighAddrType = _SleBFDSessionNeighAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 1),
    _SleBFDSessionNeighAddrType_Type()
)
sleBFDSessionNeighAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionNeighAddrType.setStatus("current")
_SleBFDSessionNeighAddrValue_Type = InetAddress
_SleBFDSessionNeighAddrValue_Object = MibTableColumn
sleBFDSessionNeighAddrValue = _SleBFDSessionNeighAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 2),
    _SleBFDSessionNeighAddrValue_Type()
)
sleBFDSessionNeighAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionNeighAddrValue.setStatus("current")


class _SleBFDSessionRegProtocols_Type(Bits):
    """Custom type sleBFDSessionRegProtocols based on Bits"""
    namedValues = NamedValues(
        *(("ospfv2", 0),
          ("ospfv3", 1),
          ("vrrp4", 2),
          ("vrrp6", 3),
          ("staticroute4", 4),
          ("staticroute6", 5),
          ("bgp", 6))
    )

_SleBFDSessionRegProtocols_Type.__name__ = "Bits"
_SleBFDSessionRegProtocols_Object = MibTableColumn
sleBFDSessionRegProtocols = _SleBFDSessionRegProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 3),
    _SleBFDSessionRegProtocols_Type()
)
sleBFDSessionRegProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRegProtocols.setStatus("current")
_SleBFDSessionLocalDiscr_Type = Unsigned32
_SleBFDSessionLocalDiscr_Object = MibTableColumn
sleBFDSessionLocalDiscr = _SleBFDSessionLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 4),
    _SleBFDSessionLocalDiscr_Type()
)
sleBFDSessionLocalDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalDiscr.setStatus("current")
_SleBFDSessionRemoteDiscr_Type = Unsigned32
_SleBFDSessionRemoteDiscr_Object = MibTableColumn
sleBFDSessionRemoteDiscr = _SleBFDSessionRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 5),
    _SleBFDSessionRemoteDiscr_Type()
)
sleBFDSessionRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRemoteDiscr.setStatus("current")


class _SleBFDSessionDetecMultiplier_Type(Integer32):
    """Custom type sleBFDSessionDetecMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleBFDSessionDetecMultiplier_Type.__name__ = "Integer32"
_SleBFDSessionDetecMultiplier_Object = MibTableColumn
sleBFDSessionDetecMultiplier = _SleBFDSessionDetecMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 6),
    _SleBFDSessionDetecMultiplier_Type()
)
sleBFDSessionDetecMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionDetecMultiplier.setStatus("current")


class _SleBFDSessionStatus_Type(Integer32):
    """Custom type sleBFDSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3),
          ("disabled", 4))
    )


_SleBFDSessionStatus_Type.__name__ = "Integer32"
_SleBFDSessionStatus_Object = MibTableColumn
sleBFDSessionStatus = _SleBFDSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 7),
    _SleBFDSessionStatus_Type()
)
sleBFDSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatus.setStatus("current")


class _SleBFDSessionEchoUsage_Type(Integer32):
    """Custom type sleBFDSessionEchoUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsing", 0),
          ("using", 1))
    )


_SleBFDSessionEchoUsage_Type.__name__ = "Integer32"
_SleBFDSessionEchoUsage_Object = MibTableColumn
sleBFDSessionEchoUsage = _SleBFDSessionEchoUsage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 8),
    _SleBFDSessionEchoUsage_Type()
)
sleBFDSessionEchoUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionEchoUsage.setStatus("current")
_SleBFDSessionUptime_Type = TimeTicks
_SleBFDSessionUptime_Object = MibTableColumn
sleBFDSessionUptime = _SleBFDSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 1, 1, 1, 9),
    _SleBFDSessionUptime_Type()
)
sleBFDSessionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionUptime.setStatus("current")
_SleBFDSessionStats_ObjectIdentity = ObjectIdentity
sleBFDSessionStats = _SleBFDSessionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2)
)
_SleBFDSessionStatsTable_Object = MibTable
sleBFDSessionStatsTable = _SleBFDSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleBFDSessionStatsTable.setStatus("current")
_SleBFDSessionStatsEntry_Object = MibTableRow
sleBFDSessionStatsEntry = _SleBFDSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1)
)
sleBFDSessionStatsEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrType"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrValue"),
)
if mibBuilder.loadTexts:
    sleBFDSessionStatsEntry.setStatus("current")
_SleBFDSessionStatsHolddownTime_Type = Unsigned32
_SleBFDSessionStatsHolddownTime_Object = MibTableColumn
sleBFDSessionStatsHolddownTime = _SleBFDSessionStatsHolddownTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 1),
    _SleBFDSessionStatsHolddownTime_Type()
)
sleBFDSessionStatsHolddownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsHolddownTime.setStatus("current")
_SleBFDSessionStatsHolddownExpires_Type = Unsigned32
_SleBFDSessionStatsHolddownExpires_Object = MibTableColumn
sleBFDSessionStatsHolddownExpires = _SleBFDSessionStatsHolddownExpires_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 2),
    _SleBFDSessionStatsHolddownExpires_Type()
)
sleBFDSessionStatsHolddownExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsHolddownExpires.setStatus("current")
_SleBFDSessionStatsHolddownHitCount_Type = Unsigned32
_SleBFDSessionStatsHolddownHitCount_Object = MibTableColumn
sleBFDSessionStatsHolddownHitCount = _SleBFDSessionStatsHolddownHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 3),
    _SleBFDSessionStatsHolddownHitCount_Type()
)
sleBFDSessionStatsHolddownHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsHolddownHitCount.setStatus("current")
_SleBFDSessionStatsHelloTime_Type = Unsigned32
_SleBFDSessionStatsHelloTime_Object = MibTableColumn
sleBFDSessionStatsHelloTime = _SleBFDSessionStatsHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 4),
    _SleBFDSessionStatsHelloTime_Type()
)
sleBFDSessionStatsHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsHelloTime.setStatus("current")
_SleBFDSessionStatsHelloHitCount_Type = Unsigned32
_SleBFDSessionStatsHelloHitCount_Object = MibTableColumn
sleBFDSessionStatsHelloHitCount = _SleBFDSessionStatsHelloHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 5),
    _SleBFDSessionStatsHelloHitCount_Type()
)
sleBFDSessionStatsHelloHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsHelloHitCount.setStatus("current")
_SleBFDSessionStatsRxCount_Type = Unsigned32
_SleBFDSessionStatsRxCount_Object = MibTableColumn
sleBFDSessionStatsRxCount = _SleBFDSessionStatsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 6),
    _SleBFDSessionStatsRxCount_Type()
)
sleBFDSessionStatsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsRxCount.setStatus("current")
_SleBFDSessionStatsRxAvgInterval_Type = Unsigned32
_SleBFDSessionStatsRxAvgInterval_Object = MibTableColumn
sleBFDSessionStatsRxAvgInterval = _SleBFDSessionStatsRxAvgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 7),
    _SleBFDSessionStatsRxAvgInterval_Type()
)
sleBFDSessionStatsRxAvgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsRxAvgInterval.setStatus("current")
_SleBFDSessionStatsRxMinInterval_Type = Unsigned32
_SleBFDSessionStatsRxMinInterval_Object = MibTableColumn
sleBFDSessionStatsRxMinInterval = _SleBFDSessionStatsRxMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 8),
    _SleBFDSessionStatsRxMinInterval_Type()
)
sleBFDSessionStatsRxMinInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsRxMinInterval.setStatus("current")
_SleBFDSessionStatsRxMaxInterval_Type = Unsigned32
_SleBFDSessionStatsRxMaxInterval_Object = MibTableColumn
sleBFDSessionStatsRxMaxInterval = _SleBFDSessionStatsRxMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 9),
    _SleBFDSessionStatsRxMaxInterval_Type()
)
sleBFDSessionStatsRxMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsRxMaxInterval.setStatus("current")
_SleBFDSessionStatsTxCount_Type = Unsigned32
_SleBFDSessionStatsTxCount_Object = MibTableColumn
sleBFDSessionStatsTxCount = _SleBFDSessionStatsTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 10),
    _SleBFDSessionStatsTxCount_Type()
)
sleBFDSessionStatsTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsTxCount.setStatus("current")
_SleBFDSessionStatsTxAvgInterval_Type = Unsigned32
_SleBFDSessionStatsTxAvgInterval_Object = MibTableColumn
sleBFDSessionStatsTxAvgInterval = _SleBFDSessionStatsTxAvgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 11),
    _SleBFDSessionStatsTxAvgInterval_Type()
)
sleBFDSessionStatsTxAvgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsTxAvgInterval.setStatus("current")
_SleBFDSessionStatsTxMinInterval_Type = Unsigned32
_SleBFDSessionStatsTxMinInterval_Object = MibTableColumn
sleBFDSessionStatsTxMinInterval = _SleBFDSessionStatsTxMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 12),
    _SleBFDSessionStatsTxMinInterval_Type()
)
sleBFDSessionStatsTxMinInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsTxMinInterval.setStatus("current")
_SleBFDSessionStatsTxMaxInterval_Type = Unsigned32
_SleBFDSessionStatsTxMaxInterval_Object = MibTableColumn
sleBFDSessionStatsTxMaxInterval = _SleBFDSessionStatsTxMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 13),
    _SleBFDSessionStatsTxMaxInterval_Type()
)
sleBFDSessionStatsTxMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsTxMaxInterval.setStatus("current")
_SleBFDSessionStatsEchoRxCount_Type = Unsigned32
_SleBFDSessionStatsEchoRxCount_Object = MibTableColumn
sleBFDSessionStatsEchoRxCount = _SleBFDSessionStatsEchoRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 14),
    _SleBFDSessionStatsEchoRxCount_Type()
)
sleBFDSessionStatsEchoRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoRxCount.setStatus("current")
_SleBFDSessionStatsEchoRxAvgInterval_Type = Unsigned32
_SleBFDSessionStatsEchoRxAvgInterval_Object = MibTableColumn
sleBFDSessionStatsEchoRxAvgInterval = _SleBFDSessionStatsEchoRxAvgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 15),
    _SleBFDSessionStatsEchoRxAvgInterval_Type()
)
sleBFDSessionStatsEchoRxAvgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoRxAvgInterval.setStatus("current")
_SleBFDSessionStatsEchoRxMinInterval_Type = Unsigned32
_SleBFDSessionStatsEchoRxMinInterval_Object = MibTableColumn
sleBFDSessionStatsEchoRxMinInterval = _SleBFDSessionStatsEchoRxMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 16),
    _SleBFDSessionStatsEchoRxMinInterval_Type()
)
sleBFDSessionStatsEchoRxMinInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoRxMinInterval.setStatus("current")
_SleBFDSessionStatsEchoRxMaxInterval_Type = Unsigned32
_SleBFDSessionStatsEchoRxMaxInterval_Object = MibTableColumn
sleBFDSessionStatsEchoRxMaxInterval = _SleBFDSessionStatsEchoRxMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 17),
    _SleBFDSessionStatsEchoRxMaxInterval_Type()
)
sleBFDSessionStatsEchoRxMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoRxMaxInterval.setStatus("current")
_SleBFDSessionStatsEchoTxCount_Type = Unsigned32
_SleBFDSessionStatsEchoTxCount_Object = MibTableColumn
sleBFDSessionStatsEchoTxCount = _SleBFDSessionStatsEchoTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 18),
    _SleBFDSessionStatsEchoTxCount_Type()
)
sleBFDSessionStatsEchoTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoTxCount.setStatus("current")
_SleBFDSessionStatsEchoTxAvgInterval_Type = Unsigned32
_SleBFDSessionStatsEchoTxAvgInterval_Object = MibTableColumn
sleBFDSessionStatsEchoTxAvgInterval = _SleBFDSessionStatsEchoTxAvgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 19),
    _SleBFDSessionStatsEchoTxAvgInterval_Type()
)
sleBFDSessionStatsEchoTxAvgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoTxAvgInterval.setStatus("current")
_SleBFDSessionStatsEchoTxMinInterva_Type = Unsigned32
_SleBFDSessionStatsEchoTxMinInterva_Object = MibTableColumn
sleBFDSessionStatsEchoTxMinInterva = _SleBFDSessionStatsEchoTxMinInterva_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 20),
    _SleBFDSessionStatsEchoTxMinInterva_Type()
)
sleBFDSessionStatsEchoTxMinInterva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoTxMinInterva.setStatus("current")
_SleBFDSessionStatsEchoTxMaxInterval_Type = Unsigned32
_SleBFDSessionStatsEchoTxMaxInterval_Object = MibTableColumn
sleBFDSessionStatsEchoTxMaxInterval = _SleBFDSessionStatsEchoTxMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 2, 1, 1, 21),
    _SleBFDSessionStatsEchoTxMaxInterval_Type()
)
sleBFDSessionStatsEchoTxMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionStatsEchoTxMaxInterval.setStatus("current")
_SleBFDSessionLocal_ObjectIdentity = ObjectIdentity
sleBFDSessionLocal = _SleBFDSessionLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3)
)
_SleBFDSessionLocalTable_Object = MibTable
sleBFDSessionLocalTable = _SleBFDSessionLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sleBFDSessionLocalTable.setStatus("current")
_SleBFDSessionLocalEntry_Object = MibTableRow
sleBFDSessionLocalEntry = _SleBFDSessionLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1)
)
sleBFDSessionLocalEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrType"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrValue"),
)
if mibBuilder.loadTexts:
    sleBFDSessionLocalEntry.setStatus("current")


class _SleBFDSessionLocalDiag_Type(Integer32):
    """Custom type sleBFDSessionLocalDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("noDiag", 0),
          ("detectExpired", 1),
          ("echoFailed", 2),
          ("neighDownAlarm", 3),
          ("fwdPlaneReset", 4),
          ("pathDown", 5),
          ("concatPathDown", 6),
          ("adminDown", 7),
          ("reverseConcatDown", 8),
          ("reserved", 9))
    )


_SleBFDSessionLocalDiag_Type.__name__ = "Integer32"
_SleBFDSessionLocalDiag_Object = MibTableColumn
sleBFDSessionLocalDiag = _SleBFDSessionLocalDiag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1, 1),
    _SleBFDSessionLocalDiag_Type()
)
sleBFDSessionLocalDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalDiag.setStatus("current")


class _SleBFDSessionLocalState_Type(Integer32):
    """Custom type sleBFDSessionLocalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("donw", 1),
          ("init", 2),
          ("up", 3))
    )


_SleBFDSessionLocalState_Type.__name__ = "Integer32"
_SleBFDSessionLocalState_Object = MibTableColumn
sleBFDSessionLocalState = _SleBFDSessionLocalState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1, 2),
    _SleBFDSessionLocalState_Type()
)
sleBFDSessionLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalState.setStatus("current")


class _SleBFDSessionLocalFlags_Type(Bits):
    """Custom type sleBFDSessionLocalFlags based on Bits"""
    namedValues = NamedValues(
        *(("poll", 0),
          ("final", 1),
          ("controlIndependent", 2),
          ("authPresent", 3),
          ("demand", 4),
          ("multipoint", 5))
    )

_SleBFDSessionLocalFlags_Type.__name__ = "Bits"
_SleBFDSessionLocalFlags_Object = MibTableColumn
sleBFDSessionLocalFlags = _SleBFDSessionLocalFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1, 3),
    _SleBFDSessionLocalFlags_Type()
)
sleBFDSessionLocalFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalFlags.setStatus("current")


class _SleBFDSessionLocalMultiplier_Type(Integer32):
    """Custom type sleBFDSessionLocalMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleBFDSessionLocalMultiplier_Type.__name__ = "Integer32"
_SleBFDSessionLocalMultiplier_Object = MibTableColumn
sleBFDSessionLocalMultiplier = _SleBFDSessionLocalMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1, 4),
    _SleBFDSessionLocalMultiplier_Type()
)
sleBFDSessionLocalMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalMultiplier.setStatus("current")
_SleBFDSessionLocalMinTxInterval_Type = Unsigned32
_SleBFDSessionLocalMinTxInterval_Object = MibTableColumn
sleBFDSessionLocalMinTxInterval = _SleBFDSessionLocalMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1, 5),
    _SleBFDSessionLocalMinTxInterval_Type()
)
sleBFDSessionLocalMinTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalMinTxInterval.setStatus("current")
_SleBFDSessionLocalMinRxInterval_Type = Unsigned32
_SleBFDSessionLocalMinRxInterval_Object = MibTableColumn
sleBFDSessionLocalMinRxInterval = _SleBFDSessionLocalMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1, 6),
    _SleBFDSessionLocalMinRxInterval_Type()
)
sleBFDSessionLocalMinRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalMinRxInterval.setStatus("current")
_SleBFDSessionLocalMinEchoInterval_Type = Unsigned32
_SleBFDSessionLocalMinEchoInterval_Object = MibTableColumn
sleBFDSessionLocalMinEchoInterval = _SleBFDSessionLocalMinEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 3, 1, 1, 7),
    _SleBFDSessionLocalMinEchoInterval_Type()
)
sleBFDSessionLocalMinEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionLocalMinEchoInterval.setStatus("current")
_SleBFDSessionRemote_ObjectIdentity = ObjectIdentity
sleBFDSessionRemote = _SleBFDSessionRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4)
)
_SleBFDSessionRemoteTable_Object = MibTable
sleBFDSessionRemoteTable = _SleBFDSessionRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1)
)
if mibBuilder.loadTexts:
    sleBFDSessionRemoteTable.setStatus("current")
_SleBFDSessionRemoteEntry_Object = MibTableRow
sleBFDSessionRemoteEntry = _SleBFDSessionRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1)
)
sleBFDSessionRemoteEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrType"),
    (0, "SLE-NETWORK-MIB", "sleBFDSessionNeighAddrValue"),
)
if mibBuilder.loadTexts:
    sleBFDSessionRemoteEntry.setStatus("current")


class _SleBFDSessionRemoteDiag_Type(Integer32):
    """Custom type sleBFDSessionRemoteDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("noDiag", 0),
          ("detectExpired", 1),
          ("echoFailed", 2),
          ("neighDownAlarm", 3),
          ("fwdPlaneReset", 4),
          ("pathDown", 5),
          ("concatPathDown", 6),
          ("adminDown", 7),
          ("reverseConcatDown", 8),
          ("reserved", 9))
    )


_SleBFDSessionRemoteDiag_Type.__name__ = "Integer32"
_SleBFDSessionRemoteDiag_Object = MibTableColumn
sleBFDSessionRemoteDiag = _SleBFDSessionRemoteDiag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1, 1),
    _SleBFDSessionRemoteDiag_Type()
)
sleBFDSessionRemoteDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRemoteDiag.setStatus("current")


class _SleBFDSessionRemoteState_Type(Integer32):
    """Custom type sleBFDSessionRemoteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("donw", 1),
          ("init", 2),
          ("up", 3))
    )


_SleBFDSessionRemoteState_Type.__name__ = "Integer32"
_SleBFDSessionRemoteState_Object = MibTableColumn
sleBFDSessionRemoteState = _SleBFDSessionRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1, 2),
    _SleBFDSessionRemoteState_Type()
)
sleBFDSessionRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRemoteState.setStatus("current")


class _SleBFDSessionremoteFlags_Type(Bits):
    """Custom type sleBFDSessionremoteFlags based on Bits"""
    namedValues = NamedValues(
        *(("poll", 0),
          ("final", 1),
          ("controlIndependent", 2),
          ("authPresent", 3),
          ("demand", 4),
          ("multipoint", 5))
    )

_SleBFDSessionremoteFlags_Type.__name__ = "Bits"
_SleBFDSessionremoteFlags_Object = MibTableColumn
sleBFDSessionremoteFlags = _SleBFDSessionremoteFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1, 3),
    _SleBFDSessionremoteFlags_Type()
)
sleBFDSessionremoteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionremoteFlags.setStatus("current")


class _SleBFDSessionRemoteMultiplier_Type(Integer32):
    """Custom type sleBFDSessionRemoteMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleBFDSessionRemoteMultiplier_Type.__name__ = "Integer32"
_SleBFDSessionRemoteMultiplier_Object = MibTableColumn
sleBFDSessionRemoteMultiplier = _SleBFDSessionRemoteMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1, 4),
    _SleBFDSessionRemoteMultiplier_Type()
)
sleBFDSessionRemoteMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRemoteMultiplier.setStatus("current")
_SleBFDSessionRemoteMinTxInterval_Type = Unsigned32
_SleBFDSessionRemoteMinTxInterval_Object = MibTableColumn
sleBFDSessionRemoteMinTxInterval = _SleBFDSessionRemoteMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1, 5),
    _SleBFDSessionRemoteMinTxInterval_Type()
)
sleBFDSessionRemoteMinTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRemoteMinTxInterval.setStatus("current")
_SleBFDSessionRemoteMinRxInterval_Type = Unsigned32
_SleBFDSessionRemoteMinRxInterval_Object = MibTableColumn
sleBFDSessionRemoteMinRxInterval = _SleBFDSessionRemoteMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1, 6),
    _SleBFDSessionRemoteMinRxInterval_Type()
)
sleBFDSessionRemoteMinRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRemoteMinRxInterval.setStatus("current")
_SleBFDSessionRemoteMinEchoInterval_Type = Unsigned32
_SleBFDSessionRemoteMinEchoInterval_Object = MibTableColumn
sleBFDSessionRemoteMinEchoInterval = _SleBFDSessionRemoteMinEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 3, 4, 1, 1, 7),
    _SleBFDSessionRemoteMinEchoInterval_Type()
)
sleBFDSessionRemoteMinEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDSessionRemoteMinEchoInterval.setStatus("current")
_SleBFDStaticGw_ObjectIdentity = ObjectIdentity
sleBFDStaticGw = _SleBFDStaticGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4)
)
_SleBFDStaticGwTable_Object = MibTable
sleBFDStaticGwTable = _SleBFDStaticGwTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 1)
)
if mibBuilder.loadTexts:
    sleBFDStaticGwTable.setStatus("current")
_SleBFDStaticGwEntry_Object = MibTableRow
sleBFDStaticGwEntry = _SleBFDStaticGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 1, 1)
)
sleBFDStaticGwEntry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleNetIfIndex"),
    (0, "SLE-NETWORK-MIB", "sleBFDStaticGwAddrType"),
    (0, "SLE-NETWORK-MIB", "sleBFDStaticGwAddr"),
)
if mibBuilder.loadTexts:
    sleBFDStaticGwEntry.setStatus("current")
_SleBFDStaticGwAddrType_Type = InetAddressType
_SleBFDStaticGwAddrType_Object = MibTableColumn
sleBFDStaticGwAddrType = _SleBFDStaticGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 1, 1, 1),
    _SleBFDStaticGwAddrType_Type()
)
sleBFDStaticGwAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDStaticGwAddrType.setStatus("current")
_SleBFDStaticGwAddr_Type = InetAddress
_SleBFDStaticGwAddr_Object = MibTableColumn
sleBFDStaticGwAddr = _SleBFDStaticGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 1, 1, 2),
    _SleBFDStaticGwAddr_Type()
)
sleBFDStaticGwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDStaticGwAddr.setStatus("current")
_SleBFDStaticGwControl_ObjectIdentity = ObjectIdentity
sleBFDStaticGwControl = _SleBFDStaticGwControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2)
)


class _SleBFDStaticGwControlRequest_Type(Integer32):
    """Custom type sleBFDStaticGwControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addBfdStaticGw", 1),
          ("delBfdStaticGw", 2))
    )


_SleBFDStaticGwControlRequest_Type.__name__ = "Integer32"
_SleBFDStaticGwControlRequest_Object = MibScalar
sleBFDStaticGwControlRequest = _SleBFDStaticGwControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 1),
    _SleBFDStaticGwControlRequest_Type()
)
sleBFDStaticGwControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlRequest.setStatus("current")
_SleBFDStaticGwControlStatus_Type = SleControlStatusType
_SleBFDStaticGwControlStatus_Object = MibScalar
sleBFDStaticGwControlStatus = _SleBFDStaticGwControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 2),
    _SleBFDStaticGwControlStatus_Type()
)
sleBFDStaticGwControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlStatus.setStatus("current")
_SleBFDStaticGwControlTimer_Type = Gauge32
_SleBFDStaticGwControlTimer_Object = MibScalar
sleBFDStaticGwControlTimer = _SleBFDStaticGwControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 3),
    _SleBFDStaticGwControlTimer_Type()
)
sleBFDStaticGwControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlTimer.setStatus("current")
_SleBFDStaticGwControlTimeStamp_Type = TimeTicks
_SleBFDStaticGwControlTimeStamp_Object = MibScalar
sleBFDStaticGwControlTimeStamp = _SleBFDStaticGwControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 4),
    _SleBFDStaticGwControlTimeStamp_Type()
)
sleBFDStaticGwControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlTimeStamp.setStatus("current")
_SleBFDStaticGwControlReqResult_Type = SleControlRequestResultType
_SleBFDStaticGwControlReqResult_Object = MibScalar
sleBFDStaticGwControlReqResult = _SleBFDStaticGwControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 5),
    _SleBFDStaticGwControlReqResult_Type()
)
sleBFDStaticGwControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlReqResult.setStatus("current")
_SleBFDStaticGwControlNetIfIndex_Type = Integer32
_SleBFDStaticGwControlNetIfIndex_Object = MibScalar
sleBFDStaticGwControlNetIfIndex = _SleBFDStaticGwControlNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 6),
    _SleBFDStaticGwControlNetIfIndex_Type()
)
sleBFDStaticGwControlNetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlNetIfIndex.setStatus("current")
_SleBFDStaticGwControlGwAddrType_Type = InetAddressType
_SleBFDStaticGwControlGwAddrType_Object = MibScalar
sleBFDStaticGwControlGwAddrType = _SleBFDStaticGwControlGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 7),
    _SleBFDStaticGwControlGwAddrType_Type()
)
sleBFDStaticGwControlGwAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlGwAddrType.setStatus("current")
_SleBFDStaticGwControlGwAddr_Type = InetAddress
_SleBFDStaticGwControlGwAddr_Object = MibScalar
sleBFDStaticGwControlGwAddr = _SleBFDStaticGwControlGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 2, 8),
    _SleBFDStaticGwControlGwAddr_Type()
)
sleBFDStaticGwControlGwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBFDStaticGwControlGwAddr.setStatus("current")
_SleBFDStaticGwNotification_ObjectIdentity = ObjectIdentity
sleBFDStaticGwNotification = _SleBFDStaticGwNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 3)
)

# Managed Objects groups

sleNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 14)
)
sleNetworkGroup.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfName"),
        ("SLE-NETWORK-MIB", "sleNetIfDescription"),
        ("SLE-NETWORK-MIB", "sleNetIfTableIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfAdminState"),
        ("SLE-NETWORK-MIB", "sleNetIfOperState"),
        ("SLE-NETWORK-MIB", "sleNetIfMulticast"),
        ("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlStatus"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimer"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlDescription"),
        ("SLE-NETWORK-MIB", "sleNetIfControlAdminState"),
        ("SLE-NETWORK-MIB", "sleNetIfControlMulticast"),
        ("SLE-NETWORK-MIB", "sleIpAddrValue"),
        ("SLE-NETWORK-MIB", "sleIpAddrMask"),
        ("SLE-NETWORK-MIB", "sleIpAddrBcast"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlStatus"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlTimer"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlValue"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlMask"),
        ("SLE-NETWORK-MIB", "sleArpIpAddress"),
        ("SLE-NETWORK-MIB", "sleArpPhyAddress"),
        ("SLE-NETWORK-MIB", "sleArpPortIndex"),
        ("SLE-NETWORK-MIB", "sleArpHwType"),
        ("SLE-NETWORK-MIB", "sleArpControlRequest"),
        ("SLE-NETWORK-MIB", "sleArpControlStatus"),
        ("SLE-NETWORK-MIB", "sleArpControlTimer"),
        ("SLE-NETWORK-MIB", "sleArpControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleArpControlReqResult"),
        ("SLE-NETWORK-MIB", "sleArpControlIpAddress"),
        ("SLE-NETWORK-MIB", "sleArpControlPhyAddress"),
        ("SLE-NETWORK-MIB", "sleRouteDstAddress"),
        ("SLE-NETWORK-MIB", "sleRouteDstMask"),
        ("SLE-NETWORK-MIB", "sleRouteGateway"),
        ("SLE-NETWORK-MIB", "sleRouteInterface"),
        ("SLE-NETWORK-MIB", "sleRouteType"),
        ("SLE-NETWORK-MIB", "sleRouteProto"),
        ("SLE-NETWORK-MIB", "sleRouteMetric"),
        ("SLE-NETWORK-MIB", "sleRouteActive"),
        ("SLE-NETWORK-MIB", "sleRouteBindingSrcAddr"),
        ("SLE-NETWORK-MIB", "sleRouteDistance"),
        ("SLE-NETWORK-MIB", "sleRouteControlRequest"),
        ("SLE-NETWORK-MIB", "sleRouteControlStatus"),
        ("SLE-NETWORK-MIB", "sleRouteControlTimer"),
        ("SLE-NETWORK-MIB", "sleRouteControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleRouteControlReqResult"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstAddress"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstMask"),
        ("SLE-NETWORK-MIB", "sleRouteControlGateway"),
        ("SLE-NETWORK-MIB", "sleRouteControlInterface"),
        ("SLE-NETWORK-MIB", "sleRouteControlBindingSrcAddr"),
        ("SLE-NETWORK-MIB", "sleRouteControlDistance"),
        ("SLE-NETWORK-MIB", "sleDhcpClIpAddr"),
        ("SLE-NETWORK-MIB", "sleDhcpClState"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlRequest"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlStatus"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlTimer"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlReqResult"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlUpdateIP"),
        ("SLE-NETWORK-MIB", "sleNetIfRegState"),
        ("SLE-NETWORK-MIB", "sleNetIfMtu"),
        ("SLE-NETWORK-MIB", "sleNetIfIpSetMode"),
        ("SLE-NETWORK-MIB", "sleNetIfIpMartianFilter"),
        ("SLE-NETWORK-MIB", "sleNetIfControlRegState"),
        ("SLE-NETWORK-MIB", "sleNetIfControlMtu"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpMartianFilter"),
        ("SLE-NETWORK-MIB", "sleIpAddrFlag"),
        ("SLE-NETWORK-MIB", "sleIpAddrScope"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlFlag"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlScope"),
        ("SLE-NETWORK-MIB", "sleArpState"),
        ("SLE-NETWORK-MIB", "sleArpHwUsed"),
        ("SLE-NETWORK-MIB", "sleArpUsedTime"),
        ("SLE-NETWORK-MIB", "sleArpControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleArpControlState"),
        ("SLE-NETWORK-MIB", "sleArpControlMask"),
        ("SLE-NETWORK-MIB", "sleRouteSubtype"),
        ("SLE-NETWORK-MIB", "sleRouteNexthopStatus"),
        ("SLE-NETWORK-MIB", "sleRouteRibStatus"),
        ("SLE-NETWORK-MIB", "sleNetworkArpAgingTime"),
        ("SLE-NETWORK-MIB", "sleNetworkControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetworkControlStatus"),
        ("SLE-NETWORK-MIB", "sleNetworkControlTimer"),
        ("SLE-NETWORK-MIB", "sleNetworkControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetworkControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetworkControlArpAgingTime"),
        ("SLE-NETWORK-MIB", "sleNetIfUpCnt"),
        ("SLE-NETWORK-MIB", "sleNetIfDownCnt"),
        ("SLE-NETWORK-MIB", "sleNetIfLinkUpTime"),
        ("SLE-NETWORK-MIB", "sleNetIfElapsedTimeAfterClearStats"),
        ("SLE-NETWORK-MIB", "sleNetIfBindingVRFName"),
        ("SLE-NETWORK-MIB", "sleNetIfControlBindingVRFName"),
        ("SLE-NETWORK-MIB", "sleRouteVRFIndex"),
        ("SLE-NETWORK-MIB", "sleRouteControlVRFIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfLocalAddress"),
        ("SLE-NETWORK-MIB", "sleTunnelIfRemoteAddress"),
        ("SLE-NETWORK-MIB", "sleTunnelIfMode"),
        ("SLE-NETWORK-MIB", "sleTunnelIfTTL"),
        ("SLE-NETWORK-MIB", "sleTunnelIfDscpMode"),
        ("SLE-NETWORK-MIB", "sleTunnelIfDscp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfKeepaliveInterval"),
        ("SLE-NETWORK-MIB", "sleTunnelIfKeepaliveRetry"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlStatus"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimer"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlLocalAddress"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlRemoteAddress"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlMode"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTTL"),
        ("SLE-NETWORK-MIB", "sleTunneIflControlDscpMode"),
        ("SLE-NETWORK-MIB", "sleTunneIflControlDscp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlKeepaliveInterval"),
        ("SLE-NETWORK-MIB", "sleTunneIflControlKeepaliveRetry"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressValue"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressMask"),
        ("SLE-NETWORK-MIB", "sleTunnelIpAddrBcast"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressFlag"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressScope"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlStatus"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTimer"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTunnelIfIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlValue"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlMask"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlFlag"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlScope"),
        ("SLE-NETWORK-MIB", "sleIpVRFIndex"),
        ("SLE-NETWORK-MIB", "sleIpVRFName"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlStatus"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimer"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlName"),
        ("SLE-NETWORK-MIB", "sleNetIfOnFailUseVRF"),
        ("SLE-NETWORK-MIB", "sleNetIfControlOnFailUseVRF"),
        ("SLE-NETWORK-MIB", "sleTunnelIfPathMtuDiscovery"),
        ("SLE-NETWORK-MIB", "sleTunnelIfVRFName"),
        ("SLE-NETWORK-MIB", "sleTunnelIfBindingPorts"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlPathMtuDiscovery"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlVRFName"),
        ("SLE-NETWORK-MIB", "sleIpVRFDesignatedPorts"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlDesignatedPorts"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcIndex"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcAddr"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcMask"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcVRFName"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlStatus"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlTimer"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlAddr"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlMask"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlVRFName"),
        ("SLE-NETWORK-MIB", "sleNetIfIpUnreachability"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpUnreachability"),
        ("SLE-NETWORK-MIB", "sleIpVRFRouterId"),
        ("SLE-NETWORK-MIB", "sleIpVRFDescription"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlRouterId"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlDescription"),
        ("SLE-NETWORK-MIB", "sleBFDEnable"),
        ("SLE-NETWORK-MIB", "sleBFDEchoEnable"),
        ("SLE-NETWORK-MIB", "sleBFDSlowTimer"),
        ("SLE-NETWORK-MIB", "sleBFDControlRequest"),
        ("SLE-NETWORK-MIB", "sleBFDControlStatus"),
        ("SLE-NETWORK-MIB", "sleBFDControlTimer"),
        ("SLE-NETWORK-MIB", "sleBFDControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleBFDControlReqResult"),
        ("SLE-NETWORK-MIB", "sleBFDControlEnable"),
        ("SLE-NETWORK-MIB", "sleBFDControlEchoEnable"),
        ("SLE-NETWORK-MIB", "sleBFDControlSlowTimer"),
        ("SLE-NETWORK-MIB", "sleBFDIfRxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDIfTxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDIfDetectMulti"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlStatus"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlTimer"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlRxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlTxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlDetectMulti"),
        ("SLE-NETWORK-MIB", "sleBFDSessionNeighAddrType"),
        ("SLE-NETWORK-MIB", "sleBFDSessionNeighAddrValue"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRegProtocols"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalDiscr"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRemoteDiscr"),
        ("SLE-NETWORK-MIB", "sleBFDSessionDetecMultiplier"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatus"),
        ("SLE-NETWORK-MIB", "sleBFDSessionEchoUsage"),
        ("SLE-NETWORK-MIB", "sleBFDSessionUptime"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsHolddownTime"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsHolddownExpires"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsHolddownHitCount"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsHelloTime"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsHelloHitCount"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsRxCount"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsRxAvgInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsRxMinInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsRxMaxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsTxCount"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsTxAvgInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsTxMinInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsTxMaxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalDiag"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalState"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalFlags"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalMultiplier"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalMinTxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalMinRxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionLocalMinEchoInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRemoteDiag"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRemoteState"),
        ("SLE-NETWORK-MIB", "sleBFDSessionremoteFlags"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRemoteMultiplier"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRemoteMinTxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRemoteMinRxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionRemoteMinEchoInterval"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwAddrType"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwAddr"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlRequest"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlStatus"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlTimer"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlReqResult"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlGwAddrType"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlGwAddr"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoRxCount"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoRxAvgInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoRxMinInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoRxMaxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoTxCount"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoTxAvgInterval"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoTxMinInterva"),
        ("SLE-NETWORK-MIB", "sleBFDSessionStatsEchoTxMaxInterval"),
        ("SLE-NETWORK-MIB", "sleNetIfipRedirects"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpRedirects"),
        ("SLE-NETWORK-MIB", "sleIpAddrIpIndex"),
        ("SLE-NETWORK-MIB", "sleIpAddrUnnumUsedIp"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlIpIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressUnnumIpIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlUnnumIpIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfIpForwarding"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpForwarding"),
        ("SLE-NETWORK-MIB", "sleTunnelIfLocalAddress6"),
        ("SLE-NETWORK-MIB", "sleTunnelIfRemoteAddress6"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlLocalAddress6"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlRemoteAddress6"),
        ("SLE-NETWORK-MIB", "sleNetIfAlias"),
        ("SLE-NETWORK-MIB", "sleNetIfIpArpAlias"),
        ("SLE-NETWORK-MIB", "sleNetIfIpArpAliasMac"),
        ("SLE-NETWORK-MIB", "sleNetIfArpMCProbeCount"),
        ("SLE-NETWORK-MIB", "sleNetIfArpUCProbeCount"),
        ("SLE-NETWORK-MIB", "sleNetIfArpRetransTime"),
        ("SLE-NETWORK-MIB", "sleNetIfIpProxyArp"),
        ("SLE-NETWORK-MIB", "sleNetIfIpRPFilter"),
        ("SLE-NETWORK-MIB", "sleNetIfRPFilter"),
        ("SLE-NETWORK-MIB", "sleNetIfRouteMap"),
        ("SLE-NETWORK-MIB", "sleNetIfControlAlias"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpArpAlias"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpArpAliasMac"),
        ("SLE-NETWORK-MIB", "sleNetIfControlArpMCProbeCount"),
        ("SLE-NETWORK-MIB", "sleNetIfControlArpUCProbeCount"),
        ("SLE-NETWORK-MIB", "sleNetIfControlArpRetransTime"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpProxyArp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpRPFilter"),
        ("SLE-NETWORK-MIB", "sleNetIfControlRPFilter"),
        ("SLE-NETWORK-MIB", "sleNetIfControlRouteMap"),
        ("SLE-NETWORK-MIB", "sleBFDIfRxIntervalIPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfTxIntervalIJPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfDetectMultiIPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlRxIntervalIPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlTxIntervalIPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlDetectMultiIPv6"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTos"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlDmac"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlChecksum"),
        ("SLE-NETWORK-MIB", "sleTunnelIfTos"),
        ("SLE-NETWORK-MIB", "sleTunnelIfDmac"),
        ("SLE-NETWORK-MIB", "sleTunnelIfChecksum"),
        ("SLE-NETWORK-MIB", "sleNetworkBaseVrfDynamicForwardBinding"),
        ("SLE-NETWORK-MIB", "sleNetworkControlVrfDynamicForwardBinding"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleDhcpClMode"),
        ("SLE-NETWORK-MIB", "sleDhcpClNetmask"),
        ("SLE-NETWORK-MIB", "sleDhcpClGateway"),
        ("SLE-NETWORK-MIB", "sleDhcpClDnsServer"),
        ("SLE-NETWORK-MIB", "sleDhcpClServer"),
        ("SLE-NETWORK-MIB", "sleDhcpClClientId"),
        ("SLE-NETWORK-MIB", "sleDhcpClClientIdStyle"),
        ("SLE-NETWORK-MIB", "sleDhcpClClassId"),
        ("SLE-NETWORK-MIB", "sleDhcpClClassIdStyle"),
        ("SLE-NETWORK-MIB", "sleDhcpClLeasetime"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlMode"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlClientId"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlClientIdStyle"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlClassId"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlClassIdStyle"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlLeasetime"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressUnnumIfIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlUnnumIfIndex"))
)
if mibBuilder.loadTexts:
    sleNetworkGroup.setStatus("current")


# Notification objects

sleNetIfRegStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 1)
)
sleNetIfRegStateChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfRegState"))
)
if mibBuilder.loadTexts:
    sleNetIfRegStateChanged.setStatus(
        "current"
    )

sleNetIfProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 2)
)
sleNetIfProfileChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfDescription"),
        ("SLE-NETWORK-MIB", "sleNetIfAdminState"),
        ("SLE-NETWORK-MIB", "sleNetIfMulticast"),
        ("SLE-NETWORK-MIB", "sleNetIfMtu"))
)
if mibBuilder.loadTexts:
    sleNetIfProfileChanged.setStatus(
        "current"
    )

sleNetIfIpMartianFilterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 3)
)
sleNetIfIpMartianFilterChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpMartianFilter"))
)
if mibBuilder.loadTexts:
    sleNetIfIpMartianFilterChanged.setStatus(
        "current"
    )

sleNetIfBindingVRFSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 4)
)
sleNetIfBindingVRFSet.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlBindingVRFName"))
)
if mibBuilder.loadTexts:
    sleNetIfBindingVRFSet.setStatus(
        "current"
    )

sleNetIfBindingVRFUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 5)
)
sleNetIfBindingVRFUnset.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlBindingVRFName"))
)
if mibBuilder.loadTexts:
    sleNetIfBindingVRFUnset.setStatus(
        "current"
    )

sleNetIfIpOnFailUseVRFChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 6)
)
sleNetIfIpOnFailUseVRFChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlOnFailUseVRF"))
)
if mibBuilder.loadTexts:
    sleNetIfIpOnFailUseVRFChanged.setStatus(
        "current"
    )

sleNetIfIpUnreachabilityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 7)
)
sleNetIfIpUnreachabilityChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpUnreachability"))
)
if mibBuilder.loadTexts:
    sleNetIfIpUnreachabilityChanged.setStatus(
        "current"
    )

sleNetIfIpRedirectsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 8)
)
sleNetIfIpRedirectsChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpRedirects"))
)
if mibBuilder.loadTexts:
    sleNetIfIpRedirectsChanged.setStatus(
        "current"
    )

sleNetIfIpForwardingChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 9)
)
sleNetIfIpForwardingChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpForwarding"))
)
if mibBuilder.loadTexts:
    sleNetIfIpForwardingChanged.setStatus(
        "current"
    )

sleNetIfAliasChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 10)
)
sleNetIfAliasChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlAlias"))
)
if mibBuilder.loadTexts:
    sleNetIfAliasChanged.setStatus(
        "current"
    )

sleNetIfIpArpAliasChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 11)
)
sleNetIfIpArpAliasChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpArpAlias"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpArpAliasMac"))
)
if mibBuilder.loadTexts:
    sleNetIfIpArpAliasChanged.setStatus(
        "current"
    )

sleNetIfArpMCProbeCountChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 12)
)
sleNetIfArpMCProbeCountChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlArpMCProbeCount"))
)
if mibBuilder.loadTexts:
    sleNetIfArpMCProbeCountChanged.setStatus(
        "current"
    )

sleNetIfArpUCProbeCountChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 13)
)
sleNetIfArpUCProbeCountChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlArpUCProbeCount"))
)
if mibBuilder.loadTexts:
    sleNetIfArpUCProbeCountChanged.setStatus(
        "current"
    )

sleNetIfArpRetransTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 14)
)
sleNetIfArpRetransTimeChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlArpRetransTime"))
)
if mibBuilder.loadTexts:
    sleNetIfArpRetransTimeChanged.setStatus(
        "current"
    )

sleNetIfIpProxyArpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 15)
)
sleNetIfIpProxyArpChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpProxyArp"))
)
if mibBuilder.loadTexts:
    sleNetIfIpProxyArpChanged.setStatus(
        "current"
    )

sleNetIfIpRPFilterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 16)
)
sleNetIfIpRPFilterChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIpRPFilter"))
)
if mibBuilder.loadTexts:
    sleNetIfIpRPFilterChanged.setStatus(
        "current"
    )

sleNetIfRPFilterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 17)
)
sleNetIfRPFilterChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlRPFilter"))
)
if mibBuilder.loadTexts:
    sleNetIfRPFilterChanged.setStatus(
        "current"
    )

sleNetIfRouteMapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 1, 3, 18)
)
sleNetIfRouteMapChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleNetIfControlRouteMap"))
)
if mibBuilder.loadTexts:
    sleNetIfRouteMapChanged.setStatus(
        "current"
    )

sleIpAddressCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 3, 1)
)
sleIpAddressCreated.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpAddrControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpAddrMask"),
        ("SLE-NETWORK-MIB", "sleIpAddrFlag"),
        ("SLE-NETWORK-MIB", "sleIpAddrScope"))
)
if mibBuilder.loadTexts:
    sleIpAddressCreated.setStatus(
        "current"
    )

sleIpAddressDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 3, 2)
)
sleIpAddressDestroyed.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpAddrControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpAddrMask"))
)
if mibBuilder.loadTexts:
    sleIpAddressDestroyed.setStatus(
        "current"
    )

sleIpAddressIpIndexAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 3, 3)
)
sleIpAddressIpIndexAdded.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpAddrControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlValue"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlMask"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlIpIndex"))
)
if mibBuilder.loadTexts:
    sleIpAddressIpIndexAdded.setStatus(
        "current"
    )

sleIpAddressIpIndexDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 2, 3, 4)
)
sleIpAddressIpIndexDeleted.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpAddrControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleIpAddrControlIpIndex"))
)
if mibBuilder.loadTexts:
    sleIpAddressIpIndexDeleted.setStatus(
        "current"
    )

sleArpEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 3, 1)
)
sleArpEntryCreated.setObjects(
      *(("SLE-NETWORK-MIB", "sleArpControlRequest"),
        ("SLE-NETWORK-MIB", "sleArpControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleArpControlReqResult"),
        ("SLE-NETWORK-MIB", "sleArpPhyAddress"))
)
if mibBuilder.loadTexts:
    sleArpEntryCreated.setStatus(
        "current"
    )

sleArpEntryDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 3, 2)
)
sleArpEntryDestroyed.setObjects(
      *(("SLE-NETWORK-MIB", "sleArpControlRequest"),
        ("SLE-NETWORK-MIB", "sleArpControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleArpControlReqResult"),
        ("SLE-NETWORK-MIB", "sleArpPhyAddress"))
)
if mibBuilder.loadTexts:
    sleArpEntryDestroyed.setStatus(
        "current"
    )

sleArpTableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 3, 3)
)
sleArpTableCleared.setObjects(
      *(("SLE-NETWORK-MIB", "sleArpControlRequest"),
        ("SLE-NETWORK-MIB", "sleArpControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleArpControlReqResult"),
        ("SLE-NETWORK-MIB", "sleArpState"))
)
if mibBuilder.loadTexts:
    sleArpTableCleared.setStatus(
        "current"
    )

sleArpTableClearedByAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 3, 3, 4)
)
sleArpTableClearedByAddr.setObjects(
      *(("SLE-NETWORK-MIB", "sleArpControlRequest"),
        ("SLE-NETWORK-MIB", "sleArpControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleArpControlReqResult"),
        ("SLE-NETWORK-MIB", "sleArpControlIpAddress"),
        ("SLE-NETWORK-MIB", "sleArpControlMask"),
        ("SLE-NETWORK-MIB", "sleArpControlState"))
)
if mibBuilder.loadTexts:
    sleArpTableClearedByAddr.setStatus(
        "current"
    )

sleRouteStaticCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 3, 1)
)
sleRouteStaticCreated.setObjects(
      *(("SLE-NETWORK-MIB", "sleRouteControlRequest"),
        ("SLE-NETWORK-MIB", "sleRouteControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleRouteControlReqResult"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstAddress"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstMask"),
        ("SLE-NETWORK-MIB", "sleRouteControlGateway"),
        ("SLE-NETWORK-MIB", "sleRouteControlInterface"),
        ("SLE-NETWORK-MIB", "sleRouteControlBindingSrcAddr"),
        ("SLE-NETWORK-MIB", "sleRouteControlDistance"),
        ("SLE-NETWORK-MIB", "sleRouteControlVRFIndex"))
)
if mibBuilder.loadTexts:
    sleRouteStaticCreated.setStatus(
        "current"
    )

sleRouteStaticDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 3, 2)
)
sleRouteStaticDestroyed.setObjects(
      *(("SLE-NETWORK-MIB", "sleRouteControlRequest"),
        ("SLE-NETWORK-MIB", "sleRouteControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleRouteControlReqResult"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstAddress"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstMask"),
        ("SLE-NETWORK-MIB", "sleRouteControlGateway"),
        ("SLE-NETWORK-MIB", "sleRouteControlInterface"),
        ("SLE-NETWORK-MIB", "sleRouteControlVRFIndex"))
)
if mibBuilder.loadTexts:
    sleRouteStaticDestroyed.setStatus(
        "current"
    )

sleRouteStaticProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 4, 3, 3)
)
sleRouteStaticProfileChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleRouteControlRequest"),
        ("SLE-NETWORK-MIB", "sleRouteControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleRouteControlReqResult"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstAddress"),
        ("SLE-NETWORK-MIB", "sleRouteControlDstMask"),
        ("SLE-NETWORK-MIB", "sleRouteControlGateway"),
        ("SLE-NETWORK-MIB", "sleRouteControlInterface"),
        ("SLE-NETWORK-MIB", "sleRouteControlBindingSrcAddr"),
        ("SLE-NETWORK-MIB", "sleRouteControlDistance"),
        ("SLE-NETWORK-MIB", "sleRouteControlVRFIndex"))
)
if mibBuilder.loadTexts:
    sleRouteStaticProfileChanged.setStatus(
        "current"
    )

sleDhcpClModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 3, 1)
)
sleDhcpClModeChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleDhcpClControlRequest"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlReqResult"),
        ("SLE-NETWORK-MIB", "sleDhcpClMode"))
)
if mibBuilder.loadTexts:
    sleDhcpClModeChanged.setStatus(
        "current"
    )

sleDhcpClProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 3, 2)
)
sleDhcpClProfileChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleDhcpClControlRequest"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlReqResult"),
        ("SLE-NETWORK-MIB", "sleDhcpClClientId"),
        ("SLE-NETWORK-MIB", "sleDhcpClClientIdStyle"),
        ("SLE-NETWORK-MIB", "sleDhcpClClassId"),
        ("SLE-NETWORK-MIB", "sleDhcpClClassIdStyle"),
        ("SLE-NETWORK-MIB", "sleDhcpClLeasetime"))
)
if mibBuilder.loadTexts:
    sleDhcpClProfileChanged.setStatus(
        "current"
    )

sleDhcpClStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 5, 3, 3)
)
sleDhcpClStateChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleDhcpClControlRequest"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleDhcpClControlReqResult"),
        ("SLE-NETWORK-MIB", "sleDhcpClState"))
)
if mibBuilder.loadTexts:
    sleDhcpClStateChanged.setStatus(
        "current"
    )

sleNetworkArpProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 7, 3, 1)
)
sleNetworkArpProfileChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetworkControlRequest"),
        ("SLE-NETWORK-MIB", "sleNetworkControlReqResult"),
        ("SLE-NETWORK-MIB", "sleNetworkControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleNetworkArpAgingTime"))
)
if mibBuilder.loadTexts:
    sleNetworkArpProfileChanged.setStatus(
        "current"
    )

sleTunnelIfCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 1)
)
sleTunnelIfCreated.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"))
)
if mibBuilder.loadTexts:
    sleTunnelIfCreated.setStatus(
        "current"
    )

sleTunnelIfDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 2)
)
sleTunnelIfDeleted.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"))
)
if mibBuilder.loadTexts:
    sleTunnelIfDeleted.setStatus(
        "current"
    )

sleTunnelIfLocalAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 3)
)
sleTunnelIfLocalAddressChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlLocalAddress"))
)
if mibBuilder.loadTexts:
    sleTunnelIfLocalAddressChanged.setStatus(
        "current"
    )

sleTunnelIfRemoteAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 4)
)
sleTunnelIfRemoteAddressChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlRemoteAddress"))
)
if mibBuilder.loadTexts:
    sleTunnelIfRemoteAddressChanged.setStatus(
        "current"
    )

sleTunnelIfModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 5)
)
sleTunnelIfModeChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlMode"))
)
if mibBuilder.loadTexts:
    sleTunnelIfModeChanged.setStatus(
        "current"
    )

sleTunnelIfTTLChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 6)
)
sleTunnelIfTTLChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTTL"))
)
if mibBuilder.loadTexts:
    sleTunnelIfTTLChanged.setStatus(
        "current"
    )

sleTunnelIfDscpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 7)
)
sleTunnelIfDscpChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunneIflControlDscpMode"),
        ("SLE-NETWORK-MIB", "sleTunneIflControlDscp"))
)
if mibBuilder.loadTexts:
    sleTunnelIfDscpChanged.setStatus(
        "current"
    )

sleTunnelIfKeepaliveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 8)
)
sleTunnelIfKeepaliveChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlKeepaliveInterval"),
        ("SLE-NETWORK-MIB", "sleTunneIflControlKeepaliveRetry"))
)
if mibBuilder.loadTexts:
    sleTunnelIfKeepaliveChanged.setStatus(
        "current"
    )

sleTunnelIfPathMtuDiscoveryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 9)
)
sleTunnelIfPathMtuDiscoveryChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlPathMtuDiscovery"))
)
if mibBuilder.loadTexts:
    sleTunnelIfPathMtuDiscoveryChanged.setStatus(
        "current"
    )

sleTunnelIfVRFNameSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 10)
)
sleTunnelIfVRFNameSet.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlVRFName"))
)
if mibBuilder.loadTexts:
    sleTunnelIfVRFNameSet.setStatus(
        "current"
    )

sleTunnelIfVRFNameUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 11)
)
sleTunnelIfVRFNameUnset.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"))
)
if mibBuilder.loadTexts:
    sleTunnelIfVRFNameUnset.setStatus(
        "current"
    )

sleTunnelIfLocalAddress6Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 12)
)
sleTunnelIfLocalAddress6Changed.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlLocalAddress6"))
)
if mibBuilder.loadTexts:
    sleTunnelIfLocalAddress6Changed.setStatus(
        "current"
    )

sleTunnelIfRemoteAddress6Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 3, 13)
)
sleTunnelIfRemoteAddress6Changed.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelIfControlRemoteAddress6"))
)
if mibBuilder.loadTexts:
    sleTunnelIfRemoteAddress6Changed.setStatus(
        "current"
    )

sleTunnelAddressCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 6, 1)
)
sleTunnelAddressCreated.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelAddressControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTunnelIfIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlValue"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlMask"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlFlag"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlScope"))
)
if mibBuilder.loadTexts:
    sleTunnelAddressCreated.setStatus(
        "current"
    )

sleTunnelAddressDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 6, 2)
)
sleTunnelAddressDeleted.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelAddressControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTunnelIfIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlValue"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlMask"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlFlag"))
)
if mibBuilder.loadTexts:
    sleTunnelAddressDeleted.setStatus(
        "current"
    )

sleTunnelAddressUnnumChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 6, 3)
)
sleTunnelAddressUnnumChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelAddressControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlUnnumIfIndex"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlUnnumIpIndex"))
)
if mibBuilder.loadTexts:
    sleTunnelAddressUnnumChanged.setStatus(
        "current"
    )

sleTunnelAddressUnnumDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 8, 6, 4)
)
sleTunnelAddressUnnumDeleted.setObjects(
      *(("SLE-NETWORK-MIB", "sleTunnelAddressControlRequest"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlReqResult"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressControlTunnelIfIndex"))
)
if mibBuilder.loadTexts:
    sleTunnelAddressUnnumDeleted.setStatus(
        "current"
    )

sleIpVRFCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 3, 1)
)
sleIpVRFCreated.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlName"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlReqResult"))
)
if mibBuilder.loadTexts:
    sleIpVRFCreated.setStatus(
        "current"
    )

sleIpVRFDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 3, 2)
)
sleIpVRFDeleted.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlName"))
)
if mibBuilder.loadTexts:
    sleIpVRFDeleted.setStatus(
        "current"
    )

sleIpVRFDesignatedPortsSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 3, 3)
)
sleIpVRFDesignatedPortsSet.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlName"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlDesignatedPorts"))
)
if mibBuilder.loadTexts:
    sleIpVRFDesignatedPortsSet.setStatus(
        "current"
    )

sleIpVRFDesignatedPortsUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 3, 4)
)
sleIpVRFDesignatedPortsUnset.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlName"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlDesignatedPorts"))
)
if mibBuilder.loadTexts:
    sleIpVRFDesignatedPortsUnset.setStatus(
        "current"
    )

sleIpVRFRouterIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 3, 5)
)
sleIpVRFRouterIdChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlName"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlRouterId"))
)
if mibBuilder.loadTexts:
    sleIpVRFRouterIdChanged.setStatus(
        "current"
    )

sleIpVRFDescriptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 3, 6)
)
sleIpVRFDescriptionChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlName"),
        ("SLE-NETWORK-MIB", "sleIpVRFControlDescription"))
)
if mibBuilder.loadTexts:
    sleIpVRFDescriptionChanged.setStatus(
        "current"
    )

sleIpVRFSelectionSrcSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 6, 1)
)
sleIpVRFSelectionSrcSet.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlAddr"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlMask"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlVRFName"))
)
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcSet.setStatus(
        "current"
    )

sleIpVRFSelectionSrcUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 9, 6, 2)
)
sleIpVRFSelectionSrcUnset.setObjects(
      *(("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlRequest"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlReqResult"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlAddr"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlMask"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcControlVRFName"))
)
if mibBuilder.loadTexts:
    sleIpVRFSelectionSrcUnset.setStatus(
        "current"
    )

sleBFDBaseProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 1, 3, 1)
)
sleBFDBaseProfileChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleBFDControlRequest"),
        ("SLE-NETWORK-MIB", "sleBFDControlReqResult"),
        ("SLE-NETWORK-MIB", "sleBFDControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleBFDEnable"),
        ("SLE-NETWORK-MIB", "sleBFDEchoEnable"),
        ("SLE-NETWORK-MIB", "sleBFDSlowTimer"))
)
if mibBuilder.loadTexts:
    sleBFDBaseProfileChanged.setStatus(
        "current"
    )

sleBFDIfProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 2, 3, 1)
)
sleBFDIfProfileChanged.setObjects(
      *(("SLE-NETWORK-MIB", "sleBFDIfControlRequest"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlRxIntervalIPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlTxIntervalIPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlDetectMultiIPv6"),
        ("SLE-NETWORK-MIB", "sleBFDIfControlReqResult"),
        ("SLE-NETWORK-MIB", "sleBFDIfRxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDIfTxInterval"),
        ("SLE-NETWORK-MIB", "sleBFDIfDetectMulti"))
)
if mibBuilder.loadTexts:
    sleBFDIfProfileChanged.setStatus(
        "current"
    )

sleBFDStaticGwAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 3, 1)
)
sleBFDStaticGwAdded.setObjects(
      *(("SLE-NETWORK-MIB", "sleBFDStaticGwControlRequest"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlTimer"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlReqResult"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlGwAddr"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlGwAddrType"))
)
if mibBuilder.loadTexts:
    sleBFDStaticGwAdded.setStatus(
        "current"
    )

sleBFDStaticGwDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 10, 4, 3, 2)
)
sleBFDStaticGwDeleted.setObjects(
      *(("SLE-NETWORK-MIB", "sleBFDStaticGwControlRequest"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlTimeStamp"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlReqResult"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlNetIfIndex"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlGwAddr"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwControlGwAddrType"))
)
if mibBuilder.loadTexts:
    sleBFDStaticGwDeleted.setStatus(
        "current"
    )


# Notifications groups

sleNetworkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 11, 15)
)
sleNetworkNotificationGroup.setObjects(
      *(("SLE-NETWORK-MIB", "sleNetIfProfileChanged"),
        ("SLE-NETWORK-MIB", "sleIpAddressCreated"),
        ("SLE-NETWORK-MIB", "sleIpAddressDestroyed"),
        ("SLE-NETWORK-MIB", "sleArpEntryCreated"),
        ("SLE-NETWORK-MIB", "sleArpEntryDestroyed"),
        ("SLE-NETWORK-MIB", "sleArpTableCleared"),
        ("SLE-NETWORK-MIB", "sleRouteStaticCreated"),
        ("SLE-NETWORK-MIB", "sleRouteStaticDestroyed"),
        ("SLE-NETWORK-MIB", "sleRouteStaticProfileChanged"),
        ("SLE-NETWORK-MIB", "sleDhcpClModeChanged"),
        ("SLE-NETWORK-MIB", "sleDhcpClProfileChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfCreated"),
        ("SLE-NETWORK-MIB", "sleTunnelIfDeleted"),
        ("SLE-NETWORK-MIB", "sleTunnelIfLocalAddressChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfRemoteAddressChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfModeChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfTTLChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfDscpChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfKeepaliveChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressCreated"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressDeleted"),
        ("SLE-NETWORK-MIB", "sleIpVRFCreated"),
        ("SLE-NETWORK-MIB", "sleIpVRFDeleted"),
        ("SLE-NETWORK-MIB", "sleDhcpClStateChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfRegStateChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfIpMartianFilterChanged"),
        ("SLE-NETWORK-MIB", "sleArpTableClearedByAddr"),
        ("SLE-NETWORK-MIB", "sleNetworkArpProfileChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfBindingVRFSet"),
        ("SLE-NETWORK-MIB", "sleNetIfBindingVRFUnset"),
        ("SLE-NETWORK-MIB", "sleNetIfIpOnFailUseVRFChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfPathMtuDiscoveryChanged"),
        ("SLE-NETWORK-MIB", "sleIpVRFDesignatedPortsSet"),
        ("SLE-NETWORK-MIB", "sleIpVRFDesignatedPortsUnset"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcSet"),
        ("SLE-NETWORK-MIB", "sleNetIfIpUnreachabilityChanged"),
        ("SLE-NETWORK-MIB", "sleIpVRFRouterIdChanged"),
        ("SLE-NETWORK-MIB", "sleIpVRFDescriptionChanged"),
        ("SLE-NETWORK-MIB", "sleBFDBaseProfileChanged"),
        ("SLE-NETWORK-MIB", "sleBFDIfProfileChanged"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwAdded"),
        ("SLE-NETWORK-MIB", "sleBFDStaticGwDeleted"),
        ("SLE-NETWORK-MIB", "sleNetIfIpRedirectsChanged"),
        ("SLE-NETWORK-MIB", "sleIpAddressIpIndexAdded"),
        ("SLE-NETWORK-MIB", "sleIpAddressIpIndexDeleted"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressUnnumChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelAddressUnnumDeleted"),
        ("SLE-NETWORK-MIB", "sleNetIfIpForwardingChanged"),
        ("SLE-NETWORK-MIB", "sleTunnelIfLocalAddress6Changed"),
        ("SLE-NETWORK-MIB", "sleTunnelIfRemoteAddress6Changed"),
        ("SLE-NETWORK-MIB", "sleNetIfAliasChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfIpArpAliasChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfArpMCProbeCountChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfArpUCProbeCountChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfArpRetransTimeChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfIpProxyArpChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfIpRPFilterChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfRPFilterChanged"),
        ("SLE-NETWORK-MIB", "sleNetIfRouteMapChanged"),
        ("SLE-NETWORK-MIB", "sleIpVRFSelectionSrcUnset"),
        ("SLE-NETWORK-MIB", "sleTunnelIfVRFNameSet"),
        ("SLE-NETWORK-MIB", "sleTunnelIfVRFNameUnset"))
)
if mibBuilder.loadTexts:
    sleNetworkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-NETWORK-MIB",
    **{"sleNetwork": sleNetwork,
       "sleNetInterface": sleNetInterface,
       "sleNetIfTable": sleNetIfTable,
       "sleNetIfEntry": sleNetIfEntry,
       "sleNetIfIndex": sleNetIfIndex,
       "sleNetIfName": sleNetIfName,
       "sleNetIfDescription": sleNetIfDescription,
       "sleNetIfTableIndex": sleNetIfTableIndex,
       "sleNetIfRegState": sleNetIfRegState,
       "sleNetIfAdminState": sleNetIfAdminState,
       "sleNetIfOperState": sleNetIfOperState,
       "sleNetIfMulticast": sleNetIfMulticast,
       "sleNetIfMtu": sleNetIfMtu,
       "sleNetIfIpSetMode": sleNetIfIpSetMode,
       "sleNetIfIpMartianFilter": sleNetIfIpMartianFilter,
       "sleNetIfUpCnt": sleNetIfUpCnt,
       "sleNetIfDownCnt": sleNetIfDownCnt,
       "sleNetIfLinkUpTime": sleNetIfLinkUpTime,
       "sleNetIfElapsedTimeAfterClearStats": sleNetIfElapsedTimeAfterClearStats,
       "sleNetIfBindingVRFName": sleNetIfBindingVRFName,
       "sleNetIfOnFailUseVRF": sleNetIfOnFailUseVRF,
       "sleNetIfIpUnreachability": sleNetIfIpUnreachability,
       "sleNetIfipRedirects": sleNetIfipRedirects,
       "sleNetIfIpForwarding": sleNetIfIpForwarding,
       "sleNetIfAlias": sleNetIfAlias,
       "sleNetIfIpArpAlias": sleNetIfIpArpAlias,
       "sleNetIfIpArpAliasMac": sleNetIfIpArpAliasMac,
       "sleNetIfArpMCProbeCount": sleNetIfArpMCProbeCount,
       "sleNetIfArpUCProbeCount": sleNetIfArpUCProbeCount,
       "sleNetIfArpRetransTime": sleNetIfArpRetransTime,
       "sleNetIfIpProxyArp": sleNetIfIpProxyArp,
       "sleNetIfIpRPFilter": sleNetIfIpRPFilter,
       "sleNetIfRPFilter": sleNetIfRPFilter,
       "sleNetIfRouteMap": sleNetIfRouteMap,
       "sleNetIfControl": sleNetIfControl,
       "sleNetIfControlRequest": sleNetIfControlRequest,
       "sleNetIfControlStatus": sleNetIfControlStatus,
       "sleNetIfControlTimer": sleNetIfControlTimer,
       "sleNetIfControlTimeStamp": sleNetIfControlTimeStamp,
       "sleNetIfControlReqResult": sleNetIfControlReqResult,
       "sleNetIfControlIndex": sleNetIfControlIndex,
       "sleNetIfControlDescription": sleNetIfControlDescription,
       "sleNetIfControlRegState": sleNetIfControlRegState,
       "sleNetIfControlAdminState": sleNetIfControlAdminState,
       "sleNetIfControlMulticast": sleNetIfControlMulticast,
       "sleNetIfControlMtu": sleNetIfControlMtu,
       "sleNetIfControlIpMartianFilter": sleNetIfControlIpMartianFilter,
       "sleNetIfControlBindingVRFName": sleNetIfControlBindingVRFName,
       "sleNetIfControlOnFailUseVRF": sleNetIfControlOnFailUseVRF,
       "sleNetIfControlIpUnreachability": sleNetIfControlIpUnreachability,
       "sleNetIfControlIpRedirects": sleNetIfControlIpRedirects,
       "sleNetIfControlIpForwarding": sleNetIfControlIpForwarding,
       "sleNetIfControlAlias": sleNetIfControlAlias,
       "sleNetIfControlIpArpAlias": sleNetIfControlIpArpAlias,
       "sleNetIfControlIpArpAliasMac": sleNetIfControlIpArpAliasMac,
       "sleNetIfControlArpMCProbeCount": sleNetIfControlArpMCProbeCount,
       "sleNetIfControlArpUCProbeCount": sleNetIfControlArpUCProbeCount,
       "sleNetIfControlArpRetransTime": sleNetIfControlArpRetransTime,
       "sleNetIfControlIpProxyArp": sleNetIfControlIpProxyArp,
       "sleNetIfControlIpRPFilter": sleNetIfControlIpRPFilter,
       "sleNetIfControlRPFilter": sleNetIfControlRPFilter,
       "sleNetIfControlRouteMap": sleNetIfControlRouteMap,
       "sleNetIfNotification": sleNetIfNotification,
       "sleNetIfRegStateChanged": sleNetIfRegStateChanged,
       "sleNetIfProfileChanged": sleNetIfProfileChanged,
       "sleNetIfIpMartianFilterChanged": sleNetIfIpMartianFilterChanged,
       "sleNetIfBindingVRFSet": sleNetIfBindingVRFSet,
       "sleNetIfBindingVRFUnset": sleNetIfBindingVRFUnset,
       "sleNetIfIpOnFailUseVRFChanged": sleNetIfIpOnFailUseVRFChanged,
       "sleNetIfIpUnreachabilityChanged": sleNetIfIpUnreachabilityChanged,
       "sleNetIfIpRedirectsChanged": sleNetIfIpRedirectsChanged,
       "sleNetIfIpForwardingChanged": sleNetIfIpForwardingChanged,
       "sleNetIfAliasChanged": sleNetIfAliasChanged,
       "sleNetIfIpArpAliasChanged": sleNetIfIpArpAliasChanged,
       "sleNetIfArpMCProbeCountChanged": sleNetIfArpMCProbeCountChanged,
       "sleNetIfArpUCProbeCountChanged": sleNetIfArpUCProbeCountChanged,
       "sleNetIfArpRetransTimeChanged": sleNetIfArpRetransTimeChanged,
       "sleNetIfIpProxyArpChanged": sleNetIfIpProxyArpChanged,
       "sleNetIfIpRPFilterChanged": sleNetIfIpRPFilterChanged,
       "sleNetIfRPFilterChanged": sleNetIfRPFilterChanged,
       "sleNetIfRouteMapChanged": sleNetIfRouteMapChanged,
       "sleIpAddress": sleIpAddress,
       "sleIpAddrTable": sleIpAddrTable,
       "sleIpAddrEntry": sleIpAddrEntry,
       "sleIpAddrValue": sleIpAddrValue,
       "sleIpAddrMask": sleIpAddrMask,
       "sleIpAddrBcast": sleIpAddrBcast,
       "sleIpAddrFlag": sleIpAddrFlag,
       "sleIpAddrScope": sleIpAddrScope,
       "sleIpAddrIpIndex": sleIpAddrIpIndex,
       "sleIpAddrUnnumUsedIp": sleIpAddrUnnumUsedIp,
       "sleIpAddrControl": sleIpAddrControl,
       "sleIpAddrControlRequest": sleIpAddrControlRequest,
       "sleIpAddrControlStatus": sleIpAddrControlStatus,
       "sleIpAddrControlTimer": sleIpAddrControlTimer,
       "sleIpAddrControlTimeStamp": sleIpAddrControlTimeStamp,
       "sleIpAddrControlReqResult": sleIpAddrControlReqResult,
       "sleIpAddrControlNetIfIndex": sleIpAddrControlNetIfIndex,
       "sleIpAddrControlValue": sleIpAddrControlValue,
       "sleIpAddrControlMask": sleIpAddrControlMask,
       "sleIpAddrControlFlag": sleIpAddrControlFlag,
       "sleIpAddrControlScope": sleIpAddrControlScope,
       "sleIpAddrControlIpIndex": sleIpAddrControlIpIndex,
       "sleIpAddrNotification": sleIpAddrNotification,
       "sleIpAddressCreated": sleIpAddressCreated,
       "sleIpAddressDestroyed": sleIpAddressDestroyed,
       "sleIpAddressIpIndexAdded": sleIpAddressIpIndexAdded,
       "sleIpAddressIpIndexDeleted": sleIpAddressIpIndexDeleted,
       "sleArp": sleArp,
       "sleArpTable": sleArpTable,
       "sleArpEntry": sleArpEntry,
       "sleArpIpAddress": sleArpIpAddress,
       "sleArpPhyAddress": sleArpPhyAddress,
       "sleArpPortIndex": sleArpPortIndex,
       "sleArpState": sleArpState,
       "sleArpHwType": sleArpHwType,
       "sleArpHwUsed": sleArpHwUsed,
       "sleArpUsedTime": sleArpUsedTime,
       "sleArpControl": sleArpControl,
       "sleArpControlRequest": sleArpControlRequest,
       "sleArpControlStatus": sleArpControlStatus,
       "sleArpControlTimer": sleArpControlTimer,
       "sleArpControlTimeStamp": sleArpControlTimeStamp,
       "sleArpControlReqResult": sleArpControlReqResult,
       "sleArpControlNetIfIndex": sleArpControlNetIfIndex,
       "sleArpControlIpAddress": sleArpControlIpAddress,
       "sleArpControlPhyAddress": sleArpControlPhyAddress,
       "sleArpControlState": sleArpControlState,
       "sleArpControlMask": sleArpControlMask,
       "sleArpNotification": sleArpNotification,
       "sleArpEntryCreated": sleArpEntryCreated,
       "sleArpEntryDestroyed": sleArpEntryDestroyed,
       "sleArpTableCleared": sleArpTableCleared,
       "sleArpTableClearedByAddr": sleArpTableClearedByAddr,
       "sleRoute": sleRoute,
       "sleRouteTable": sleRouteTable,
       "sleRouteEntry": sleRouteEntry,
       "sleRouteDstAddress": sleRouteDstAddress,
       "sleRouteDstMask": sleRouteDstMask,
       "sleRouteGateway": sleRouteGateway,
       "sleRouteInterface": sleRouteInterface,
       "sleRouteType": sleRouteType,
       "sleRouteProto": sleRouteProto,
       "sleRouteMetric": sleRouteMetric,
       "sleRouteActive": sleRouteActive,
       "sleRouteBindingSrcAddr": sleRouteBindingSrcAddr,
       "sleRouteDistance": sleRouteDistance,
       "sleRouteSubtype": sleRouteSubtype,
       "sleRouteNexthopStatus": sleRouteNexthopStatus,
       "sleRouteRibStatus": sleRouteRibStatus,
       "sleRouteVRFIndex": sleRouteVRFIndex,
       "sleRouteControl": sleRouteControl,
       "sleRouteControlRequest": sleRouteControlRequest,
       "sleRouteControlStatus": sleRouteControlStatus,
       "sleRouteControlTimer": sleRouteControlTimer,
       "sleRouteControlTimeStamp": sleRouteControlTimeStamp,
       "sleRouteControlReqResult": sleRouteControlReqResult,
       "sleRouteControlDstAddress": sleRouteControlDstAddress,
       "sleRouteControlDstMask": sleRouteControlDstMask,
       "sleRouteControlGateway": sleRouteControlGateway,
       "sleRouteControlInterface": sleRouteControlInterface,
       "sleRouteControlBindingSrcAddr": sleRouteControlBindingSrcAddr,
       "sleRouteControlDistance": sleRouteControlDistance,
       "sleRouteControlVRFIndex": sleRouteControlVRFIndex,
       "sleRouteNotification": sleRouteNotification,
       "sleRouteStaticCreated": sleRouteStaticCreated,
       "sleRouteStaticDestroyed": sleRouteStaticDestroyed,
       "sleRouteStaticProfileChanged": sleRouteStaticProfileChanged,
       "sleDhcpClient": sleDhcpClient,
       "sleDhcpClTable": sleDhcpClTable,
       "sleDhcpClEntry": sleDhcpClEntry,
       "sleDhcpClMode": sleDhcpClMode,
       "sleDhcpClIpAddr": sleDhcpClIpAddr,
       "sleDhcpClNetmask": sleDhcpClNetmask,
       "sleDhcpClGateway": sleDhcpClGateway,
       "sleDhcpClDnsServer": sleDhcpClDnsServer,
       "sleDhcpClServer": sleDhcpClServer,
       "sleDhcpClClientId": sleDhcpClClientId,
       "sleDhcpClClientIdStyle": sleDhcpClClientIdStyle,
       "sleDhcpClClassId": sleDhcpClClassId,
       "sleDhcpClClassIdStyle": sleDhcpClClassIdStyle,
       "sleDhcpClLeasetime": sleDhcpClLeasetime,
       "sleDhcpClState": sleDhcpClState,
       "sleDhcpClControl": sleDhcpClControl,
       "sleDhcpClControlRequest": sleDhcpClControlRequest,
       "sleDhcpClControlStatus": sleDhcpClControlStatus,
       "sleDhcpClControlTimer": sleDhcpClControlTimer,
       "sleDhcpClControlTimeStamp": sleDhcpClControlTimeStamp,
       "sleDhcpClControlReqResult": sleDhcpClControlReqResult,
       "sleDhcpClControlNetIfIndex": sleDhcpClControlNetIfIndex,
       "sleDhcpClControlMode": sleDhcpClControlMode,
       "sleDhcpClControlClientId": sleDhcpClControlClientId,
       "sleDhcpClControlClientIdStyle": sleDhcpClControlClientIdStyle,
       "sleDhcpClControlClassId": sleDhcpClControlClassId,
       "sleDhcpClControlClassIdStyle": sleDhcpClControlClassIdStyle,
       "sleDhcpClControlLeasetime": sleDhcpClControlLeasetime,
       "sleDhcpClControlUpdateIP": sleDhcpClControlUpdateIP,
       "sleDhcpClNotification": sleDhcpClNotification,
       "sleDhcpClModeChanged": sleDhcpClModeChanged,
       "sleDhcpClProfileChanged": sleDhcpClProfileChanged,
       "sleDhcpClStateChanged": sleDhcpClStateChanged,
       "sleV2DhcpClient": sleV2DhcpClient,
       "sleNetworkBase": sleNetworkBase,
       "sleNetworkBaseInfo": sleNetworkBaseInfo,
       "sleNetworkArpAgingTime": sleNetworkArpAgingTime,
       "sleNetworkBaseVrfDynamicForwardBinding": sleNetworkBaseVrfDynamicForwardBinding,
       "sleNetworkBaseControl": sleNetworkBaseControl,
       "sleNetworkControlRequest": sleNetworkControlRequest,
       "sleNetworkControlStatus": sleNetworkControlStatus,
       "sleNetworkControlTimer": sleNetworkControlTimer,
       "sleNetworkControlTimeStamp": sleNetworkControlTimeStamp,
       "sleNetworkControlReqResult": sleNetworkControlReqResult,
       "sleNetworkControlArpAgingTime": sleNetworkControlArpAgingTime,
       "sleNetworkControlVrfDynamicForwardBinding": sleNetworkControlVrfDynamicForwardBinding,
       "sleNetworkBaseNotification": sleNetworkBaseNotification,
       "sleNetworkArpProfileChanged": sleNetworkArpProfileChanged,
       "sleTunnel": sleTunnel,
       "sleTunnelIfTable": sleTunnelIfTable,
       "sleTunnelIfEntry": sleTunnelIfEntry,
       "sleTunnelIfIndex": sleTunnelIfIndex,
       "sleTunnelIfLocalAddress": sleTunnelIfLocalAddress,
       "sleTunnelIfRemoteAddress": sleTunnelIfRemoteAddress,
       "sleTunnelIfMode": sleTunnelIfMode,
       "sleTunnelIfTTL": sleTunnelIfTTL,
       "sleTunnelIfDscpMode": sleTunnelIfDscpMode,
       "sleTunnelIfDscp": sleTunnelIfDscp,
       "sleTunnelIfKeepaliveInterval": sleTunnelIfKeepaliveInterval,
       "sleTunnelIfKeepaliveRetry": sleTunnelIfKeepaliveRetry,
       "sleTunnelIfPathMtuDiscovery": sleTunnelIfPathMtuDiscovery,
       "sleTunnelIfVRFName": sleTunnelIfVRFName,
       "sleTunnelIfBindingPorts": sleTunnelIfBindingPorts,
       "sleTunnelIfLocalAddress6": sleTunnelIfLocalAddress6,
       "sleTunnelIfRemoteAddress6": sleTunnelIfRemoteAddress6,
       "sleTunnelIfChecksum": sleTunnelIfChecksum,
       "sleTunnelIfDmac": sleTunnelIfDmac,
       "sleTunnelIfTos": sleTunnelIfTos,
       "sleTunnelIfControl": sleTunnelIfControl,
       "sleTunnelIfControlRequest": sleTunnelIfControlRequest,
       "sleTunnelIfControlStatus": sleTunnelIfControlStatus,
       "sleTunnelIfControlTimer": sleTunnelIfControlTimer,
       "sleTunnelIfControlTimeStamp": sleTunnelIfControlTimeStamp,
       "sleTunnelIfControlReqResult": sleTunnelIfControlReqResult,
       "sleTunnelIfControlIndex": sleTunnelIfControlIndex,
       "sleTunnelIfControlLocalAddress": sleTunnelIfControlLocalAddress,
       "sleTunnelIfControlRemoteAddress": sleTunnelIfControlRemoteAddress,
       "sleTunnelIfControlMode": sleTunnelIfControlMode,
       "sleTunnelIfControlTTL": sleTunnelIfControlTTL,
       "sleTunneIflControlDscpMode": sleTunneIflControlDscpMode,
       "sleTunneIflControlDscp": sleTunneIflControlDscp,
       "sleTunnelIfControlKeepaliveInterval": sleTunnelIfControlKeepaliveInterval,
       "sleTunneIflControlKeepaliveRetry": sleTunneIflControlKeepaliveRetry,
       "sleTunnelIfControlPathMtuDiscovery": sleTunnelIfControlPathMtuDiscovery,
       "sleTunnelIfControlVRFName": sleTunnelIfControlVRFName,
       "sleTunnelIfControlLocalAddress6": sleTunnelIfControlLocalAddress6,
       "sleTunnelIfControlRemoteAddress6": sleTunnelIfControlRemoteAddress6,
       "sleTunnelIfControlChecksum": sleTunnelIfControlChecksum,
       "sleTunnelIfControlDmac": sleTunnelIfControlDmac,
       "sleTunnelIfControlTos": sleTunnelIfControlTos,
       "sleTunnelIfNotification": sleTunnelIfNotification,
       "sleTunnelIfCreated": sleTunnelIfCreated,
       "sleTunnelIfDeleted": sleTunnelIfDeleted,
       "sleTunnelIfLocalAddressChanged": sleTunnelIfLocalAddressChanged,
       "sleTunnelIfRemoteAddressChanged": sleTunnelIfRemoteAddressChanged,
       "sleTunnelIfModeChanged": sleTunnelIfModeChanged,
       "sleTunnelIfTTLChanged": sleTunnelIfTTLChanged,
       "sleTunnelIfDscpChanged": sleTunnelIfDscpChanged,
       "sleTunnelIfKeepaliveChanged": sleTunnelIfKeepaliveChanged,
       "sleTunnelIfPathMtuDiscoveryChanged": sleTunnelIfPathMtuDiscoveryChanged,
       "sleTunnelIfVRFNameSet": sleTunnelIfVRFNameSet,
       "sleTunnelIfVRFNameUnset": sleTunnelIfVRFNameUnset,
       "sleTunnelIfLocalAddress6Changed": sleTunnelIfLocalAddress6Changed,
       "sleTunnelIfRemoteAddress6Changed": sleTunnelIfRemoteAddress6Changed,
       "sleTunnelAddressTable": sleTunnelAddressTable,
       "sleTunnelAddressEntry": sleTunnelAddressEntry,
       "sleTunnelAddressValue": sleTunnelAddressValue,
       "sleTunnelAddressMask": sleTunnelAddressMask,
       "sleTunnelIpAddrBcast": sleTunnelIpAddrBcast,
       "sleTunnelAddressFlag": sleTunnelAddressFlag,
       "sleTunnelAddressScope": sleTunnelAddressScope,
       "sleTunnelAddressUnnumIfIndex": sleTunnelAddressUnnumIfIndex,
       "sleTunnelAddressUnnumIpIndex": sleTunnelAddressUnnumIpIndex,
       "sleTunnelAddressControl": sleTunnelAddressControl,
       "sleTunnelAddressControlRequest": sleTunnelAddressControlRequest,
       "sleTunnelAddressControlStatus": sleTunnelAddressControlStatus,
       "sleTunnelAddressControlTimer": sleTunnelAddressControlTimer,
       "sleTunnelAddressControlTimeStamp": sleTunnelAddressControlTimeStamp,
       "sleTunnelAddressControlReqResult": sleTunnelAddressControlReqResult,
       "sleTunnelAddressControlTunnelIfIndex": sleTunnelAddressControlTunnelIfIndex,
       "sleTunnelAddressControlValue": sleTunnelAddressControlValue,
       "sleTunnelAddressControlMask": sleTunnelAddressControlMask,
       "sleTunnelAddressControlFlag": sleTunnelAddressControlFlag,
       "sleTunnelAddressControlScope": sleTunnelAddressControlScope,
       "sleTunnelAddressControlUnnumIfIndex": sleTunnelAddressControlUnnumIfIndex,
       "sleTunnelAddressControlUnnumIpIndex": sleTunnelAddressControlUnnumIpIndex,
       "sleTunnelAddressNotification": sleTunnelAddressNotification,
       "sleTunnelAddressCreated": sleTunnelAddressCreated,
       "sleTunnelAddressDeleted": sleTunnelAddressDeleted,
       "sleTunnelAddressUnnumChanged": sleTunnelAddressUnnumChanged,
       "sleTunnelAddressUnnumDeleted": sleTunnelAddressUnnumDeleted,
       "sleIpVRF": sleIpVRF,
       "sleIpVRFTable": sleIpVRFTable,
       "sleIpVRFEntry": sleIpVRFEntry,
       "sleIpVRFIndex": sleIpVRFIndex,
       "sleIpVRFName": sleIpVRFName,
       "sleIpVRFDesignatedPorts": sleIpVRFDesignatedPorts,
       "sleIpVRFRouterId": sleIpVRFRouterId,
       "sleIpVRFDescription": sleIpVRFDescription,
       "sleIpVRFControl": sleIpVRFControl,
       "sleIpVRFControlRequest": sleIpVRFControlRequest,
       "sleIpVRFControlStatus": sleIpVRFControlStatus,
       "sleIpVRFControlTimer": sleIpVRFControlTimer,
       "sleIpVRFControlTimeStamp": sleIpVRFControlTimeStamp,
       "sleIpVRFControlReqResult": sleIpVRFControlReqResult,
       "sleIpVRFControlName": sleIpVRFControlName,
       "sleIpVRFControlDesignatedPorts": sleIpVRFControlDesignatedPorts,
       "sleIpVRFControlRouterId": sleIpVRFControlRouterId,
       "sleIpVRFControlDescription": sleIpVRFControlDescription,
       "sleIpVRFNotification": sleIpVRFNotification,
       "sleIpVRFCreated": sleIpVRFCreated,
       "sleIpVRFDeleted": sleIpVRFDeleted,
       "sleIpVRFDesignatedPortsSet": sleIpVRFDesignatedPortsSet,
       "sleIpVRFDesignatedPortsUnset": sleIpVRFDesignatedPortsUnset,
       "sleIpVRFRouterIdChanged": sleIpVRFRouterIdChanged,
       "sleIpVRFDescriptionChanged": sleIpVRFDescriptionChanged,
       "sleIpVRFSelectionSourceTable": sleIpVRFSelectionSourceTable,
       "sleIpVRFSelectionSourceEntry": sleIpVRFSelectionSourceEntry,
       "sleIpVRFSelectionSrcIndex": sleIpVRFSelectionSrcIndex,
       "sleIpVRFSelectionSrcAddr": sleIpVRFSelectionSrcAddr,
       "sleIpVRFSelectionSrcMask": sleIpVRFSelectionSrcMask,
       "sleIpVRFSelectionSrcVRFName": sleIpVRFSelectionSrcVRFName,
       "sleIpVRFSelectionSourceControl": sleIpVRFSelectionSourceControl,
       "sleIpVRFSelectionSrcControlRequest": sleIpVRFSelectionSrcControlRequest,
       "sleIpVRFSelectionSrcControlStatus": sleIpVRFSelectionSrcControlStatus,
       "sleIpVRFSelectionSrcControlTimer": sleIpVRFSelectionSrcControlTimer,
       "sleIpVRFSelectionSrcControlTimeStamp": sleIpVRFSelectionSrcControlTimeStamp,
       "sleIpVRFSelectionSrcControlReqResult": sleIpVRFSelectionSrcControlReqResult,
       "sleIpVRFSelectionSrcControlAddr": sleIpVRFSelectionSrcControlAddr,
       "sleIpVRFSelectionSrcControlMask": sleIpVRFSelectionSrcControlMask,
       "sleIpVRFSelectionSrcControlVRFName": sleIpVRFSelectionSrcControlVRFName,
       "sleIpVRFSelectionSourceNotification": sleIpVRFSelectionSourceNotification,
       "sleIpVRFSelectionSrcSet": sleIpVRFSelectionSrcSet,
       "sleIpVRFSelectionSrcUnset": sleIpVRFSelectionSrcUnset,
       "sleBFD": sleBFD,
       "sleBFDBase": sleBFDBase,
       "sleBFDBaseInfo": sleBFDBaseInfo,
       "sleBFDEnable": sleBFDEnable,
       "sleBFDEchoEnable": sleBFDEchoEnable,
       "sleBFDSlowTimer": sleBFDSlowTimer,
       "sleBFDBaseControl": sleBFDBaseControl,
       "sleBFDControlRequest": sleBFDControlRequest,
       "sleBFDControlStatus": sleBFDControlStatus,
       "sleBFDControlTimer": sleBFDControlTimer,
       "sleBFDControlTimeStamp": sleBFDControlTimeStamp,
       "sleBFDControlReqResult": sleBFDControlReqResult,
       "sleBFDControlEnable": sleBFDControlEnable,
       "sleBFDControlEchoEnable": sleBFDControlEchoEnable,
       "sleBFDControlSlowTimer": sleBFDControlSlowTimer,
       "sleBFDBaseNotification": sleBFDBaseNotification,
       "sleBFDBaseProfileChanged": sleBFDBaseProfileChanged,
       "sleBFDInterface": sleBFDInterface,
       "sleBFDInterfaceTable": sleBFDInterfaceTable,
       "sleBFDInterfaceEntry": sleBFDInterfaceEntry,
       "sleBFDIfRxInterval": sleBFDIfRxInterval,
       "sleBFDIfTxInterval": sleBFDIfTxInterval,
       "sleBFDIfDetectMulti": sleBFDIfDetectMulti,
       "sleBFDIfRxIntervalIPv6": sleBFDIfRxIntervalIPv6,
       "sleBFDIfTxIntervalIJPv6": sleBFDIfTxIntervalIJPv6,
       "sleBFDIfDetectMultiIPv6": sleBFDIfDetectMultiIPv6,
       "sleBFDInterfaceControl": sleBFDInterfaceControl,
       "sleBFDIfControlRequest": sleBFDIfControlRequest,
       "sleBFDIfControlStatus": sleBFDIfControlStatus,
       "sleBFDIfControlTimer": sleBFDIfControlTimer,
       "sleBFDIfControlTimeStamp": sleBFDIfControlTimeStamp,
       "sleBFDIfControlReqResult": sleBFDIfControlReqResult,
       "sleBFDIfControlNetIfIndex": sleBFDIfControlNetIfIndex,
       "sleBFDIfControlRxInterval": sleBFDIfControlRxInterval,
       "sleBFDIfControlTxInterval": sleBFDIfControlTxInterval,
       "sleBFDIfControlDetectMulti": sleBFDIfControlDetectMulti,
       "sleBFDIfControlRxIntervalIPv6": sleBFDIfControlRxIntervalIPv6,
       "sleBFDIfControlTxIntervalIPv6": sleBFDIfControlTxIntervalIPv6,
       "sleBFDIfControlDetectMultiIPv6": sleBFDIfControlDetectMultiIPv6,
       "sleBFDInterfaceNotification": sleBFDInterfaceNotification,
       "sleBFDIfProfileChanged": sleBFDIfProfileChanged,
       "sleBFDSession": sleBFDSession,
       "sleBFDSessionInfo": sleBFDSessionInfo,
       "sleBFDSessionInfoTable": sleBFDSessionInfoTable,
       "sleBFDSessionInfoEntry": sleBFDSessionInfoEntry,
       "sleBFDSessionNeighAddrType": sleBFDSessionNeighAddrType,
       "sleBFDSessionNeighAddrValue": sleBFDSessionNeighAddrValue,
       "sleBFDSessionRegProtocols": sleBFDSessionRegProtocols,
       "sleBFDSessionLocalDiscr": sleBFDSessionLocalDiscr,
       "sleBFDSessionRemoteDiscr": sleBFDSessionRemoteDiscr,
       "sleBFDSessionDetecMultiplier": sleBFDSessionDetecMultiplier,
       "sleBFDSessionStatus": sleBFDSessionStatus,
       "sleBFDSessionEchoUsage": sleBFDSessionEchoUsage,
       "sleBFDSessionUptime": sleBFDSessionUptime,
       "sleBFDSessionStats": sleBFDSessionStats,
       "sleBFDSessionStatsTable": sleBFDSessionStatsTable,
       "sleBFDSessionStatsEntry": sleBFDSessionStatsEntry,
       "sleBFDSessionStatsHolddownTime": sleBFDSessionStatsHolddownTime,
       "sleBFDSessionStatsHolddownExpires": sleBFDSessionStatsHolddownExpires,
       "sleBFDSessionStatsHolddownHitCount": sleBFDSessionStatsHolddownHitCount,
       "sleBFDSessionStatsHelloTime": sleBFDSessionStatsHelloTime,
       "sleBFDSessionStatsHelloHitCount": sleBFDSessionStatsHelloHitCount,
       "sleBFDSessionStatsRxCount": sleBFDSessionStatsRxCount,
       "sleBFDSessionStatsRxAvgInterval": sleBFDSessionStatsRxAvgInterval,
       "sleBFDSessionStatsRxMinInterval": sleBFDSessionStatsRxMinInterval,
       "sleBFDSessionStatsRxMaxInterval": sleBFDSessionStatsRxMaxInterval,
       "sleBFDSessionStatsTxCount": sleBFDSessionStatsTxCount,
       "sleBFDSessionStatsTxAvgInterval": sleBFDSessionStatsTxAvgInterval,
       "sleBFDSessionStatsTxMinInterval": sleBFDSessionStatsTxMinInterval,
       "sleBFDSessionStatsTxMaxInterval": sleBFDSessionStatsTxMaxInterval,
       "sleBFDSessionStatsEchoRxCount": sleBFDSessionStatsEchoRxCount,
       "sleBFDSessionStatsEchoRxAvgInterval": sleBFDSessionStatsEchoRxAvgInterval,
       "sleBFDSessionStatsEchoRxMinInterval": sleBFDSessionStatsEchoRxMinInterval,
       "sleBFDSessionStatsEchoRxMaxInterval": sleBFDSessionStatsEchoRxMaxInterval,
       "sleBFDSessionStatsEchoTxCount": sleBFDSessionStatsEchoTxCount,
       "sleBFDSessionStatsEchoTxAvgInterval": sleBFDSessionStatsEchoTxAvgInterval,
       "sleBFDSessionStatsEchoTxMinInterva": sleBFDSessionStatsEchoTxMinInterva,
       "sleBFDSessionStatsEchoTxMaxInterval": sleBFDSessionStatsEchoTxMaxInterval,
       "sleBFDSessionLocal": sleBFDSessionLocal,
       "sleBFDSessionLocalTable": sleBFDSessionLocalTable,
       "sleBFDSessionLocalEntry": sleBFDSessionLocalEntry,
       "sleBFDSessionLocalDiag": sleBFDSessionLocalDiag,
       "sleBFDSessionLocalState": sleBFDSessionLocalState,
       "sleBFDSessionLocalFlags": sleBFDSessionLocalFlags,
       "sleBFDSessionLocalMultiplier": sleBFDSessionLocalMultiplier,
       "sleBFDSessionLocalMinTxInterval": sleBFDSessionLocalMinTxInterval,
       "sleBFDSessionLocalMinRxInterval": sleBFDSessionLocalMinRxInterval,
       "sleBFDSessionLocalMinEchoInterval": sleBFDSessionLocalMinEchoInterval,
       "sleBFDSessionRemote": sleBFDSessionRemote,
       "sleBFDSessionRemoteTable": sleBFDSessionRemoteTable,
       "sleBFDSessionRemoteEntry": sleBFDSessionRemoteEntry,
       "sleBFDSessionRemoteDiag": sleBFDSessionRemoteDiag,
       "sleBFDSessionRemoteState": sleBFDSessionRemoteState,
       "sleBFDSessionremoteFlags": sleBFDSessionremoteFlags,
       "sleBFDSessionRemoteMultiplier": sleBFDSessionRemoteMultiplier,
       "sleBFDSessionRemoteMinTxInterval": sleBFDSessionRemoteMinTxInterval,
       "sleBFDSessionRemoteMinRxInterval": sleBFDSessionRemoteMinRxInterval,
       "sleBFDSessionRemoteMinEchoInterval": sleBFDSessionRemoteMinEchoInterval,
       "sleBFDStaticGw": sleBFDStaticGw,
       "sleBFDStaticGwTable": sleBFDStaticGwTable,
       "sleBFDStaticGwEntry": sleBFDStaticGwEntry,
       "sleBFDStaticGwAddrType": sleBFDStaticGwAddrType,
       "sleBFDStaticGwAddr": sleBFDStaticGwAddr,
       "sleBFDStaticGwControl": sleBFDStaticGwControl,
       "sleBFDStaticGwControlRequest": sleBFDStaticGwControlRequest,
       "sleBFDStaticGwControlStatus": sleBFDStaticGwControlStatus,
       "sleBFDStaticGwControlTimer": sleBFDStaticGwControlTimer,
       "sleBFDStaticGwControlTimeStamp": sleBFDStaticGwControlTimeStamp,
       "sleBFDStaticGwControlReqResult": sleBFDStaticGwControlReqResult,
       "sleBFDStaticGwControlNetIfIndex": sleBFDStaticGwControlNetIfIndex,
       "sleBFDStaticGwControlGwAddrType": sleBFDStaticGwControlGwAddrType,
       "sleBFDStaticGwControlGwAddr": sleBFDStaticGwControlGwAddr,
       "sleBFDStaticGwNotification": sleBFDStaticGwNotification,
       "sleBFDStaticGwAdded": sleBFDStaticGwAdded,
       "sleBFDStaticGwDeleted": sleBFDStaticGwDeleted,
       "sleNetworkGroup": sleNetworkGroup,
       "sleNetworkNotificationGroup": sleNetworkNotificationGroup}
)
