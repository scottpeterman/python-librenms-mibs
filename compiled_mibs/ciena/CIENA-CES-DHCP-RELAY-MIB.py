# SNMP MIB module (CIENA-CES-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:33 2025
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

(cienaCesStatistics,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesStatistics")

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

cienaCesDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6)
)
if mibBuilder.loadTexts:
    cienaCesDhcpRelayMIB.setRevisions(
        ("2017-06-07 00:00",
         "2015-09-09 00:00",
         "2013-03-05 00:00",
         "2010-07-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DhcpLiType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("subPort", 1),
          ("pbt-service", 2),
          ("mplsVc", 3),
          ("unknown", 99))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesDhcpRelayAgent_ObjectIdentity = ObjectIdentity
cienaCesDhcpRelayAgent = _CienaCesDhcpRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1)
)
_CienaCesDhcpRelayAgentGlobalAttrs_ObjectIdentity = ObjectIdentity
cienaCesDhcpRelayAgentGlobalAttrs = _CienaCesDhcpRelayAgentGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 1)
)


class _CienaCesDhcpRelayAgentCircuitId_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentCircuitId based on Integer32"""
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
        *(("li", 1),
          ("port", 2),
          ("cidString", 3),
          ("liVs", 4))
    )


_CienaCesDhcpRelayAgentCircuitId_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentCircuitId_Object = MibScalar
cienaCesDhcpRelayAgentCircuitId = _CienaCesDhcpRelayAgentCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 1, 1),
    _CienaCesDhcpRelayAgentCircuitId_Type()
)
cienaCesDhcpRelayAgentCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentCircuitId.setStatus("current")


class _CienaCesDhcpRelayAgentRemoteId_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentRemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("hostName", 2),
          ("ridString", 3))
    )


_CienaCesDhcpRelayAgentRemoteId_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentRemoteId_Object = MibScalar
cienaCesDhcpRelayAgentRemoteId = _CienaCesDhcpRelayAgentRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 1, 2),
    _CienaCesDhcpRelayAgentRemoteId_Type()
)
cienaCesDhcpRelayAgentRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentRemoteId.setStatus("current")


class _CienaCesDhcpRelayAgentL2State_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentL2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCesDhcpRelayAgentL2State_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentL2State_Object = MibScalar
cienaCesDhcpRelayAgentL2State = _CienaCesDhcpRelayAgentL2State_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 1, 3),
    _CienaCesDhcpRelayAgentL2State_Type()
)
cienaCesDhcpRelayAgentL2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2State.setStatus("current")


class _CienaCesDhcpRelayAgentReplaceOption82_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentReplaceOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CienaCesDhcpRelayAgentReplaceOption82_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentReplaceOption82_Object = MibScalar
cienaCesDhcpRelayAgentReplaceOption82 = _CienaCesDhcpRelayAgentReplaceOption82_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 1, 4),
    _CienaCesDhcpRelayAgentReplaceOption82_Type()
)
cienaCesDhcpRelayAgentReplaceOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentReplaceOption82.setStatus("current")
_CienaCesDhcpRelayAgentL2StateTable_Object = MibTable
cienaCesDhcpRelayAgentL2StateTable = _CienaCesDhcpRelayAgentL2StateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2StateTable.setStatus("current")
_CienaCesDhcpRelayAgentL2StateEntry_Object = MibTableRow
cienaCesDhcpRelayAgentL2StateEntry = _CienaCesDhcpRelayAgentL2StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2, 1)
)
cienaCesDhcpRelayAgentL2StateEntry.setIndexNames(
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentVsIndex"),
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentRlan"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2StateEntry.setStatus("current")


class _CienaCesDhcpRelayAgentVsIndex_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentVsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_CienaCesDhcpRelayAgentVsIndex_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentVsIndex_Object = MibTableColumn
cienaCesDhcpRelayAgentVsIndex = _CienaCesDhcpRelayAgentVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2, 1, 1),
    _CienaCesDhcpRelayAgentVsIndex_Type()
)
cienaCesDhcpRelayAgentVsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentVsIndex.setStatus("current")


class _CienaCesDhcpRelayAgentRlan_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentRlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CienaCesDhcpRelayAgentRlan_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentRlan_Object = MibTableColumn
cienaCesDhcpRelayAgentRlan = _CienaCesDhcpRelayAgentRlan_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2, 1, 2),
    _CienaCesDhcpRelayAgentRlan_Type()
)
cienaCesDhcpRelayAgentRlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentRlan.setStatus("current")


class _CienaCesDhcpRelayAgentL2AdminState_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentL2AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCesDhcpRelayAgentL2AdminState_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentL2AdminState_Object = MibTableColumn
cienaCesDhcpRelayAgentL2AdminState = _CienaCesDhcpRelayAgentL2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2, 1, 3),
    _CienaCesDhcpRelayAgentL2AdminState_Type()
)
cienaCesDhcpRelayAgentL2AdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2AdminState.setStatus("current")


class _CienaCesDhcpRelayAgentL2OperState_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentL2OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCesDhcpRelayAgentL2OperState_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentL2OperState_Object = MibTableColumn
cienaCesDhcpRelayAgentL2OperState = _CienaCesDhcpRelayAgentL2OperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2, 1, 4),
    _CienaCesDhcpRelayAgentL2OperState_Type()
)
cienaCesDhcpRelayAgentL2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2OperState.setStatus("current")
_CienaCesDhcpRelayAgentL2StatsClear_Type = TruthValue
_CienaCesDhcpRelayAgentL2StatsClear_Object = MibTableColumn
cienaCesDhcpRelayAgentL2StatsClear = _CienaCesDhcpRelayAgentL2StatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2, 1, 5),
    _CienaCesDhcpRelayAgentL2StatsClear_Type()
)
cienaCesDhcpRelayAgentL2StatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2StatsClear.setStatus("current")
_CienaCesDhcpRelayAgentL2RowStatus_Type = RowStatus
_CienaCesDhcpRelayAgentL2RowStatus_Object = MibTableColumn
cienaCesDhcpRelayAgentL2RowStatus = _CienaCesDhcpRelayAgentL2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 2, 1, 6),
    _CienaCesDhcpRelayAgentL2RowStatus_Type()
)
cienaCesDhcpRelayAgentL2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2RowStatus.setStatus("current")
_CienaCesDhcpRelayAgentTrustTable_Object = MibTable
cienaCesDhcpRelayAgentTrustTable = _CienaCesDhcpRelayAgentTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentTrustTable.setStatus("current")
_CienaCesDhcpRelayAgentTrustEntry_Object = MibTableRow
cienaCesDhcpRelayAgentTrustEntry = _CienaCesDhcpRelayAgentTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 5, 1)
)
cienaCesDhcpRelayAgentTrustEntry.setIndexNames(
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentVsIndex"),
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentRlan"),
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentTrustedLiType"),
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentTrustedLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentTrustEntry.setStatus("current")
_CienaCesDhcpRelayAgentTrustedLiType_Type = DhcpLiType
_CienaCesDhcpRelayAgentTrustedLiType_Object = MibTableColumn
cienaCesDhcpRelayAgentTrustedLiType = _CienaCesDhcpRelayAgentTrustedLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 5, 1, 1),
    _CienaCesDhcpRelayAgentTrustedLiType_Type()
)
cienaCesDhcpRelayAgentTrustedLiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentTrustedLiType.setStatus("current")


class _CienaCesDhcpRelayAgentTrustedLiIndex_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentTrustedLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesDhcpRelayAgentTrustedLiIndex_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentTrustedLiIndex_Object = MibTableColumn
cienaCesDhcpRelayAgentTrustedLiIndex = _CienaCesDhcpRelayAgentTrustedLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 5, 1, 2),
    _CienaCesDhcpRelayAgentTrustedLiIndex_Type()
)
cienaCesDhcpRelayAgentTrustedLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentTrustedLiIndex.setStatus("current")


class _CienaCesDhcpRelayAgentTrustMode_Type(Integer32):
    """Custom type cienaCesDhcpRelayAgentTrustMode based on Integer32"""
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
        *(("clientTrust", 1),
          ("serverTrust", 2),
          ("dualRoleTrust", 3),
          ("unTrust", 4))
    )


_CienaCesDhcpRelayAgentTrustMode_Type.__name__ = "Integer32"
_CienaCesDhcpRelayAgentTrustMode_Object = MibTableColumn
cienaCesDhcpRelayAgentTrustMode = _CienaCesDhcpRelayAgentTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 5, 1, 3),
    _CienaCesDhcpRelayAgentTrustMode_Type()
)
cienaCesDhcpRelayAgentTrustMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentTrustMode.setStatus("current")


class _CienaCesDhcpRelayAgentCidString_Type(DisplayString):
    """Custom type cienaCesDhcpRelayAgentCidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpRelayAgentCidString_Type.__name__ = "DisplayString"
_CienaCesDhcpRelayAgentCidString_Object = MibTableColumn
cienaCesDhcpRelayAgentCidString = _CienaCesDhcpRelayAgentCidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 5, 1, 4),
    _CienaCesDhcpRelayAgentCidString_Type()
)
cienaCesDhcpRelayAgentCidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentCidString.setStatus("current")


class _CienaCesDhcpRelayAgentRidString_Type(DisplayString):
    """Custom type cienaCesDhcpRelayAgentRidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpRelayAgentRidString_Type.__name__ = "DisplayString"
_CienaCesDhcpRelayAgentRidString_Object = MibTableColumn
cienaCesDhcpRelayAgentRidString = _CienaCesDhcpRelayAgentRidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 5, 1, 5),
    _CienaCesDhcpRelayAgentRidString_Type()
)
cienaCesDhcpRelayAgentRidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentRidString.setStatus("current")
_CienaCesDhcpRelayAgentL2StatsTable_Object = MibTable
cienaCesDhcpRelayAgentL2StatsTable = _CienaCesDhcpRelayAgentL2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2StatsTable.setStatus("current")
_CienaCesDhcpRelayAgentL2StatsEntry_Object = MibTableRow
cienaCesDhcpRelayAgentL2StatsEntry = _CienaCesDhcpRelayAgentL2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1)
)
cienaCesDhcpRelayAgentL2StatsEntry.setIndexNames(
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentVsIndex"),
    (0, "CIENA-CES-DHCP-RELAY-MIB", "cienaCesDhcpRelayAgentRlan"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2StatsEntry.setStatus("current")
_CienaCesDhcpRelayAgentL2IpSecHeaders_Type = Counter32
_CienaCesDhcpRelayAgentL2IpSecHeaders_Object = MibTableColumn
cienaCesDhcpRelayAgentL2IpSecHeaders = _CienaCesDhcpRelayAgentL2IpSecHeaders_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 1),
    _CienaCesDhcpRelayAgentL2IpSecHeaders_Type()
)
cienaCesDhcpRelayAgentL2IpSecHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2IpSecHeaders.setStatus("current")
_CienaCesDhcpRelayAgentL2Option82Added_Type = Counter32
_CienaCesDhcpRelayAgentL2Option82Added_Object = MibTableColumn
cienaCesDhcpRelayAgentL2Option82Added = _CienaCesDhcpRelayAgentL2Option82Added_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 2),
    _CienaCesDhcpRelayAgentL2Option82Added_Type()
)
cienaCesDhcpRelayAgentL2Option82Added.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2Option82Added.setStatus("current")
_CienaCesDhcpRelayAgentL2Option82Removed_Type = Counter32
_CienaCesDhcpRelayAgentL2Option82Removed_Object = MibTableColumn
cienaCesDhcpRelayAgentL2Option82Removed = _CienaCesDhcpRelayAgentL2Option82Removed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 3),
    _CienaCesDhcpRelayAgentL2Option82Removed_Type()
)
cienaCesDhcpRelayAgentL2Option82Removed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2Option82Removed.setStatus("current")
_CienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx_Type = Counter32
_CienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx_Object = MibTableColumn
cienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx = _CienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 4),
    _CienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx_Type()
)
cienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx.setStatus("current")
_CienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx_Type = Counter32
_CienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx_Object = MibTableColumn
cienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx = _CienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 5),
    _CienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx_Type()
)
cienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx.setStatus("current")
_CienaCesDhcpRelayAgentL2SpoofedDhcpPkts_Type = Counter32
_CienaCesDhcpRelayAgentL2SpoofedDhcpPkts_Object = MibTableColumn
cienaCesDhcpRelayAgentL2SpoofedDhcpPkts = _CienaCesDhcpRelayAgentL2SpoofedDhcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 6),
    _CienaCesDhcpRelayAgentL2SpoofedDhcpPkts_Type()
)
cienaCesDhcpRelayAgentL2SpoofedDhcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2SpoofedDhcpPkts.setStatus("current")
_CienaCesDhcpRelayAgentL2Option82ExceedMTU_Type = Counter32
_CienaCesDhcpRelayAgentL2Option82ExceedMTU_Object = MibTableColumn
cienaCesDhcpRelayAgentL2Option82ExceedMTU = _CienaCesDhcpRelayAgentL2Option82ExceedMTU_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 7),
    _CienaCesDhcpRelayAgentL2Option82ExceedMTU_Type()
)
cienaCesDhcpRelayAgentL2Option82ExceedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2Option82ExceedMTU.setStatus("current")
_CienaCesDhcpRelayAgentL2NoTrustedServerPktDrop_Type = Counter32
_CienaCesDhcpRelayAgentL2NoTrustedServerPktDrop_Object = MibTableColumn
cienaCesDhcpRelayAgentL2NoTrustedServerPktDrop = _CienaCesDhcpRelayAgentL2NoTrustedServerPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 8),
    _CienaCesDhcpRelayAgentL2NoTrustedServerPktDrop_Type()
)
cienaCesDhcpRelayAgentL2NoTrustedServerPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2NoTrustedServerPktDrop.setStatus("current")
_CienaCesDhcpRelayAgentL2NoTrustedClientPktDrop_Type = Counter32
_CienaCesDhcpRelayAgentL2NoTrustedClientPktDrop_Object = MibTableColumn
cienaCesDhcpRelayAgentL2NoTrustedClientPktDrop = _CienaCesDhcpRelayAgentL2NoTrustedClientPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 9),
    _CienaCesDhcpRelayAgentL2NoTrustedClientPktDrop_Type()
)
cienaCesDhcpRelayAgentL2NoTrustedClientPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2NoTrustedClientPktDrop.setStatus("current")
_CienaCesDhcpRelayAgentL2InvalidConfigPktDrop_Type = Counter32
_CienaCesDhcpRelayAgentL2InvalidConfigPktDrop_Object = MibTableColumn
cienaCesDhcpRelayAgentL2InvalidConfigPktDrop = _CienaCesDhcpRelayAgentL2InvalidConfigPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 10),
    _CienaCesDhcpRelayAgentL2InvalidConfigPktDrop_Type()
)
cienaCesDhcpRelayAgentL2InvalidConfigPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2InvalidConfigPktDrop.setStatus("current")
_CienaCesDhcpRelayAgentL2GeneralErrors_Type = Counter32
_CienaCesDhcpRelayAgentL2GeneralErrors_Object = MibTableColumn
cienaCesDhcpRelayAgentL2GeneralErrors = _CienaCesDhcpRelayAgentL2GeneralErrors_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 11),
    _CienaCesDhcpRelayAgentL2GeneralErrors_Type()
)
cienaCesDhcpRelayAgentL2GeneralErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2GeneralErrors.setStatus("current")
_CienaCesDhcpRelayAgentL2Option82Replaced_Type = Counter32
_CienaCesDhcpRelayAgentL2Option82Replaced_Object = MibTableColumn
cienaCesDhcpRelayAgentL2Option82Replaced = _CienaCesDhcpRelayAgentL2Option82Replaced_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 12),
    _CienaCesDhcpRelayAgentL2Option82Replaced_Type()
)
cienaCesDhcpRelayAgentL2Option82Replaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2Option82Replaced.setStatus("current")
_CienaCesDhcpRelayAgentL2ForRelay_Type = Counter32
_CienaCesDhcpRelayAgentL2ForRelay_Object = MibTableColumn
cienaCesDhcpRelayAgentL2ForRelay = _CienaCesDhcpRelayAgentL2ForRelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 13),
    _CienaCesDhcpRelayAgentL2ForRelay_Type()
)
cienaCesDhcpRelayAgentL2ForRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2ForRelay.setStatus("current")
_CienaCesDhcpRelayAgentL2ClientRelayed_Type = Counter32
_CienaCesDhcpRelayAgentL2ClientRelayed_Object = MibTableColumn
cienaCesDhcpRelayAgentL2ClientRelayed = _CienaCesDhcpRelayAgentL2ClientRelayed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 14),
    _CienaCesDhcpRelayAgentL2ClientRelayed_Type()
)
cienaCesDhcpRelayAgentL2ClientRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2ClientRelayed.setStatus("current")
_CienaCesDhcpRelayAgentL2ServerRelayed_Type = Counter32
_CienaCesDhcpRelayAgentL2ServerRelayed_Object = MibTableColumn
cienaCesDhcpRelayAgentL2ServerRelayed = _CienaCesDhcpRelayAgentL2ServerRelayed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 6, 1, 15),
    _CienaCesDhcpRelayAgentL2ServerRelayed_Type()
)
cienaCesDhcpRelayAgentL2ServerRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2ServerRelayed.setStatus("current")
_CienaCesDhcpRelayAgentGlobalStats_ObjectIdentity = ObjectIdentity
cienaCesDhcpRelayAgentGlobalStats = _CienaCesDhcpRelayAgentGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 7)
)
_CienaCesDhcpRelayAgentL2GlobalStatsClear_Type = TruthValue
_CienaCesDhcpRelayAgentL2GlobalStatsClear_Object = MibScalar
cienaCesDhcpRelayAgentL2GlobalStatsClear = _CienaCesDhcpRelayAgentL2GlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 7, 1),
    _CienaCesDhcpRelayAgentL2GlobalStatsClear_Type()
)
cienaCesDhcpRelayAgentL2GlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2GlobalStatsClear.setStatus("current")
_CienaCesDhcpRelayAgentL2Relayed_Type = Counter32
_CienaCesDhcpRelayAgentL2Relayed_Object = MibScalar
cienaCesDhcpRelayAgentL2Relayed = _CienaCesDhcpRelayAgentL2Relayed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 7, 2),
    _CienaCesDhcpRelayAgentL2Relayed_Type()
)
cienaCesDhcpRelayAgentL2Relayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2Relayed.setStatus("current")
_CienaCesDhcpRelayAgentL2Dropped_Type = Counter32
_CienaCesDhcpRelayAgentL2Dropped_Object = MibScalar
cienaCesDhcpRelayAgentL2Dropped = _CienaCesDhcpRelayAgentL2Dropped_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 7, 3),
    _CienaCesDhcpRelayAgentL2Dropped_Type()
)
cienaCesDhcpRelayAgentL2Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2Dropped.setStatus("current")
_CienaCesDhcpRelayAgentL2Forwarded_Type = Counter32
_CienaCesDhcpRelayAgentL2Forwarded_Object = MibScalar
cienaCesDhcpRelayAgentL2Forwarded = _CienaCesDhcpRelayAgentL2Forwarded_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 7, 4),
    _CienaCesDhcpRelayAgentL2Forwarded_Type()
)
cienaCesDhcpRelayAgentL2Forwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2Forwarded.setStatus("current")
_CienaCesDhcpRelayAgentL2NotForRelay_Type = Counter32
_CienaCesDhcpRelayAgentL2NotForRelay_Object = MibScalar
cienaCesDhcpRelayAgentL2NotForRelay = _CienaCesDhcpRelayAgentL2NotForRelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 6, 1, 7, 5),
    _CienaCesDhcpRelayAgentL2NotForRelay_Type()
)
cienaCesDhcpRelayAgentL2NotForRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpRelayAgentL2NotForRelay.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-DHCP-RELAY-MIB",
    **{"DhcpLiType": DhcpLiType,
       "cienaCesDhcpRelayMIB": cienaCesDhcpRelayMIB,
       "cienaCesDhcpRelayAgent": cienaCesDhcpRelayAgent,
       "cienaCesDhcpRelayAgentGlobalAttrs": cienaCesDhcpRelayAgentGlobalAttrs,
       "cienaCesDhcpRelayAgentCircuitId": cienaCesDhcpRelayAgentCircuitId,
       "cienaCesDhcpRelayAgentRemoteId": cienaCesDhcpRelayAgentRemoteId,
       "cienaCesDhcpRelayAgentL2State": cienaCesDhcpRelayAgentL2State,
       "cienaCesDhcpRelayAgentReplaceOption82": cienaCesDhcpRelayAgentReplaceOption82,
       "cienaCesDhcpRelayAgentL2StateTable": cienaCesDhcpRelayAgentL2StateTable,
       "cienaCesDhcpRelayAgentL2StateEntry": cienaCesDhcpRelayAgentL2StateEntry,
       "cienaCesDhcpRelayAgentVsIndex": cienaCesDhcpRelayAgentVsIndex,
       "cienaCesDhcpRelayAgentRlan": cienaCesDhcpRelayAgentRlan,
       "cienaCesDhcpRelayAgentL2AdminState": cienaCesDhcpRelayAgentL2AdminState,
       "cienaCesDhcpRelayAgentL2OperState": cienaCesDhcpRelayAgentL2OperState,
       "cienaCesDhcpRelayAgentL2StatsClear": cienaCesDhcpRelayAgentL2StatsClear,
       "cienaCesDhcpRelayAgentL2RowStatus": cienaCesDhcpRelayAgentL2RowStatus,
       "cienaCesDhcpRelayAgentTrustTable": cienaCesDhcpRelayAgentTrustTable,
       "cienaCesDhcpRelayAgentTrustEntry": cienaCesDhcpRelayAgentTrustEntry,
       "cienaCesDhcpRelayAgentTrustedLiType": cienaCesDhcpRelayAgentTrustedLiType,
       "cienaCesDhcpRelayAgentTrustedLiIndex": cienaCesDhcpRelayAgentTrustedLiIndex,
       "cienaCesDhcpRelayAgentTrustMode": cienaCesDhcpRelayAgentTrustMode,
       "cienaCesDhcpRelayAgentCidString": cienaCesDhcpRelayAgentCidString,
       "cienaCesDhcpRelayAgentRidString": cienaCesDhcpRelayAgentRidString,
       "cienaCesDhcpRelayAgentL2StatsTable": cienaCesDhcpRelayAgentL2StatsTable,
       "cienaCesDhcpRelayAgentL2StatsEntry": cienaCesDhcpRelayAgentL2StatsEntry,
       "cienaCesDhcpRelayAgentL2IpSecHeaders": cienaCesDhcpRelayAgentL2IpSecHeaders,
       "cienaCesDhcpRelayAgentL2Option82Added": cienaCesDhcpRelayAgentL2Option82Added,
       "cienaCesDhcpRelayAgentL2Option82Removed": cienaCesDhcpRelayAgentL2Option82Removed,
       "cienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx": cienaCesDhcpRelayAgentL2UntrustedClientPortPktsRx,
       "cienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx": cienaCesDhcpRelayAgentL2UntrustedServerPortPktsRx,
       "cienaCesDhcpRelayAgentL2SpoofedDhcpPkts": cienaCesDhcpRelayAgentL2SpoofedDhcpPkts,
       "cienaCesDhcpRelayAgentL2Option82ExceedMTU": cienaCesDhcpRelayAgentL2Option82ExceedMTU,
       "cienaCesDhcpRelayAgentL2NoTrustedServerPktDrop": cienaCesDhcpRelayAgentL2NoTrustedServerPktDrop,
       "cienaCesDhcpRelayAgentL2NoTrustedClientPktDrop": cienaCesDhcpRelayAgentL2NoTrustedClientPktDrop,
       "cienaCesDhcpRelayAgentL2InvalidConfigPktDrop": cienaCesDhcpRelayAgentL2InvalidConfigPktDrop,
       "cienaCesDhcpRelayAgentL2GeneralErrors": cienaCesDhcpRelayAgentL2GeneralErrors,
       "cienaCesDhcpRelayAgentL2Option82Replaced": cienaCesDhcpRelayAgentL2Option82Replaced,
       "cienaCesDhcpRelayAgentL2ForRelay": cienaCesDhcpRelayAgentL2ForRelay,
       "cienaCesDhcpRelayAgentL2ClientRelayed": cienaCesDhcpRelayAgentL2ClientRelayed,
       "cienaCesDhcpRelayAgentL2ServerRelayed": cienaCesDhcpRelayAgentL2ServerRelayed,
       "cienaCesDhcpRelayAgentGlobalStats": cienaCesDhcpRelayAgentGlobalStats,
       "cienaCesDhcpRelayAgentL2GlobalStatsClear": cienaCesDhcpRelayAgentL2GlobalStatsClear,
       "cienaCesDhcpRelayAgentL2Relayed": cienaCesDhcpRelayAgentL2Relayed,
       "cienaCesDhcpRelayAgentL2Dropped": cienaCesDhcpRelayAgentL2Dropped,
       "cienaCesDhcpRelayAgentL2Forwarded": cienaCesDhcpRelayAgentL2Forwarded,
       "cienaCesDhcpRelayAgentL2NotForRelay": cienaCesDhcpRelayAgentL2NotForRelay}
)
