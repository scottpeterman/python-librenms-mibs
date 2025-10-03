# SNMP MIB module (CISCOSB-IPSTDACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-IPSTDACL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:53 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rlIpStdAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207)
)
if mibBuilder.loadTexts:
    rlIpStdAcl.setRevisions(
        ("2011-05-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlIpStdAclActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("permit", 2))
    )



class RlIpStdAclStdClassificationType(TextualConvention, Integer32):
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
        *(("any", 1),
          ("ipv4", 2),
          ("ipv6any", 3),
          ("ipv6", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RlIpStdAclTable_Object = MibTable
rlIpStdAclTable = _RlIpStdAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1)
)
if mibBuilder.loadTexts:
    rlIpStdAclTable.setStatus("current")
_RlIpStdAclEntry_Object = MibTableRow
rlIpStdAclEntry = _RlIpStdAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1)
)
rlIpStdAclEntry.setIndexNames(
    (0, "CISCOSB-IPSTDACL-MIB", "rlIpStdAclAclName"),
    (0, "CISCOSB-IPSTDACL-MIB", "rlIpStdAclAceIndex"),
)
if mibBuilder.loadTexts:
    rlIpStdAclEntry.setStatus("current")


class _RlIpStdAclAclName_Type(DisplayString):
    """Custom type rlIpStdAclAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlIpStdAclAclName_Type.__name__ = "DisplayString"
_RlIpStdAclAclName_Object = MibTableColumn
rlIpStdAclAclName = _RlIpStdAclAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 1),
    _RlIpStdAclAclName_Type()
)
rlIpStdAclAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpStdAclAclName.setStatus("current")
_RlIpStdAclAceIndex_Type = Integer32
_RlIpStdAclAceIndex_Object = MibTableColumn
rlIpStdAclAceIndex = _RlIpStdAclAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 2),
    _RlIpStdAclAceIndex_Type()
)
rlIpStdAclAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpStdAclAceIndex.setStatus("current")
_RlIpStdAclSrcClassificationType_Type = RlIpStdAclStdClassificationType
_RlIpStdAclSrcClassificationType_Object = MibTableColumn
rlIpStdAclSrcClassificationType = _RlIpStdAclSrcClassificationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 3),
    _RlIpStdAclSrcClassificationType_Type()
)
rlIpStdAclSrcClassificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclSrcClassificationType.setStatus("current")
_RlIpStdAclSrcIpAddrType_Type = InetAddressType
_RlIpStdAclSrcIpAddrType_Object = MibTableColumn
rlIpStdAclSrcIpAddrType = _RlIpStdAclSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 4),
    _RlIpStdAclSrcIpAddrType_Type()
)
rlIpStdAclSrcIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclSrcIpAddrType.setStatus("current")
_RlIpStdAclSrcIpAddr_Type = InetAddress
_RlIpStdAclSrcIpAddr_Object = MibTableColumn
rlIpStdAclSrcIpAddr = _RlIpStdAclSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 5),
    _RlIpStdAclSrcIpAddr_Type()
)
rlIpStdAclSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclSrcIpAddr.setStatus("current")


class _RlIpStdAclSrcPrefLen_Type(InetAddressPrefixLength):
    """Custom type rlIpStdAclSrcPrefLen based on InetAddressPrefixLength"""
    defaultValue = 32


_RlIpStdAclSrcPrefLen_Type.__name__ = "InetAddressPrefixLength"
_RlIpStdAclSrcPrefLen_Object = MibTableColumn
rlIpStdAclSrcPrefLen = _RlIpStdAclSrcPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 6),
    _RlIpStdAclSrcPrefLen_Type()
)
rlIpStdAclSrcPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclSrcPrefLen.setStatus("current")
_RlIpStdAclDstClassificationType_Type = RlIpStdAclStdClassificationType
_RlIpStdAclDstClassificationType_Object = MibTableColumn
rlIpStdAclDstClassificationType = _RlIpStdAclDstClassificationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 7),
    _RlIpStdAclDstClassificationType_Type()
)
rlIpStdAclDstClassificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclDstClassificationType.setStatus("current")
_RlIpStdAclDstIpAddrType_Type = InetAddressType
_RlIpStdAclDstIpAddrType_Object = MibTableColumn
rlIpStdAclDstIpAddrType = _RlIpStdAclDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 8),
    _RlIpStdAclDstIpAddrType_Type()
)
rlIpStdAclDstIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclDstIpAddrType.setStatus("current")
_RlIpStdAclDstIpAddr_Type = InetAddress
_RlIpStdAclDstIpAddr_Object = MibTableColumn
rlIpStdAclDstIpAddr = _RlIpStdAclDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 9),
    _RlIpStdAclDstIpAddr_Type()
)
rlIpStdAclDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclDstIpAddr.setStatus("current")


class _RlIpStdAclDstPrefLen_Type(InetAddressPrefixLength):
    """Custom type rlIpStdAclDstPrefLen based on InetAddressPrefixLength"""
    defaultValue = 32


_RlIpStdAclDstPrefLen_Type.__name__ = "InetAddressPrefixLength"
_RlIpStdAclDstPrefLen_Object = MibTableColumn
rlIpStdAclDstPrefLen = _RlIpStdAclDstPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 10),
    _RlIpStdAclDstPrefLen_Type()
)
rlIpStdAclDstPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclDstPrefLen.setStatus("current")


class _RlIpStdAclAction_Type(RlIpStdAclActionType):
    """Custom type rlIpStdAclAction based on RlIpStdAclActionType"""
    defaultValue = 2


_RlIpStdAclAction_Type.__name__ = "RlIpStdAclActionType"
_RlIpStdAclAction_Object = MibTableColumn
rlIpStdAclAction = _RlIpStdAclAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 11),
    _RlIpStdAclAction_Type()
)
rlIpStdAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclAction.setStatus("current")
_RlIpStdAclRowStatus_Type = RowStatus
_RlIpStdAclRowStatus_Object = MibTableColumn
rlIpStdAclRowStatus = _RlIpStdAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 1, 1, 12),
    _RlIpStdAclRowStatus_Type()
)
rlIpStdAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdAclRowStatus.setStatus("current")
_RlIpStdAclFreeAceIndex_Type = Integer32
_RlIpStdAclFreeAceIndex_Object = MibScalar
rlIpStdAclFreeAceIndex = _RlIpStdAclFreeAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 2),
    _RlIpStdAclFreeAceIndex_Type()
)
rlIpStdAclFreeAceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStdAclFreeAceIndex.setStatus("current")
_RlIpStdAclNameToIndexTable_Object = MibTable
rlIpStdAclNameToIndexTable = _RlIpStdAclNameToIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 3)
)
if mibBuilder.loadTexts:
    rlIpStdAclNameToIndexTable.setStatus("current")
_RlIpStdAclNameToIndexEntry_Object = MibTableRow
rlIpStdAclNameToIndexEntry = _RlIpStdAclNameToIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 3, 1)
)
rlIpStdAclNameToIndexEntry.setIndexNames(
    (0, "CISCOSB-IPSTDACL-MIB", "rlIpStdAclNameToIndexName"),
)
if mibBuilder.loadTexts:
    rlIpStdAclNameToIndexEntry.setStatus("current")


class _RlIpStdAclNameToIndexName_Type(DisplayString):
    """Custom type rlIpStdAclNameToIndexName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlIpStdAclNameToIndexName_Type.__name__ = "DisplayString"
_RlIpStdAclNameToIndexName_Object = MibTableColumn
rlIpStdAclNameToIndexName = _RlIpStdAclNameToIndexName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 3, 1, 1),
    _RlIpStdAclNameToIndexName_Type()
)
rlIpStdAclNameToIndexName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpStdAclNameToIndexName.setStatus("current")
_RlIpStdAclNameToIndexIndex_Type = Integer32
_RlIpStdAclNameToIndexIndex_Object = MibTableColumn
rlIpStdAclNameToIndexIndex = _RlIpStdAclNameToIndexIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 3, 1, 2),
    _RlIpStdAclNameToIndexIndex_Type()
)
rlIpStdAclNameToIndexIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStdAclNameToIndexIndex.setStatus("current")
_RlIpStdPairAclTable_Object = MibTable
rlIpStdPairAclTable = _RlIpStdPairAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4)
)
if mibBuilder.loadTexts:
    rlIpStdPairAclTable.setStatus("current")
_RlIpStdPairAclEntry_Object = MibTableRow
rlIpStdPairAclEntry = _RlIpStdPairAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1)
)
rlIpStdPairAclEntry.setIndexNames(
    (0, "CISCOSB-IPSTDACL-MIB", "rlIpStdPairAclAclName"),
    (0, "CISCOSB-IPSTDACL-MIB", "rlIpStdPairAclAceIndex"),
)
if mibBuilder.loadTexts:
    rlIpStdPairAclEntry.setStatus("current")


class _RlIpStdPairAclAclName_Type(DisplayString):
    """Custom type rlIpStdPairAclAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlIpStdPairAclAclName_Type.__name__ = "DisplayString"
_RlIpStdPairAclAclName_Object = MibTableColumn
rlIpStdPairAclAclName = _RlIpStdPairAclAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 1),
    _RlIpStdPairAclAclName_Type()
)
rlIpStdPairAclAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpStdPairAclAclName.setStatus("current")
_RlIpStdPairAclAceIndex_Type = Integer32
_RlIpStdPairAclAceIndex_Object = MibTableColumn
rlIpStdPairAclAceIndex = _RlIpStdPairAclAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 2),
    _RlIpStdPairAclAceIndex_Type()
)
rlIpStdPairAclAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpStdPairAclAceIndex.setStatus("current")
_RlIpStdPairAclSrcIpAddrType_Type = InetAddressType
_RlIpStdPairAclSrcIpAddrType_Object = MibTableColumn
rlIpStdPairAclSrcIpAddrType = _RlIpStdPairAclSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 3),
    _RlIpStdPairAclSrcIpAddrType_Type()
)
rlIpStdPairAclSrcIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclSrcIpAddrType.setStatus("current")
_RlIpStdPairAclSrcIpAddr_Type = InetAddress
_RlIpStdPairAclSrcIpAddr_Object = MibTableColumn
rlIpStdPairAclSrcIpAddr = _RlIpStdPairAclSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 4),
    _RlIpStdPairAclSrcIpAddr_Type()
)
rlIpStdPairAclSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclSrcIpAddr.setStatus("current")


class _RlIpStdPairAclSrcPrefLen_Type(InetAddressPrefixLength):
    """Custom type rlIpStdPairAclSrcPrefLen based on InetAddressPrefixLength"""
    defaultValue = 32


_RlIpStdPairAclSrcPrefLen_Type.__name__ = "InetAddressPrefixLength"
_RlIpStdPairAclSrcPrefLen_Object = MibTableColumn
rlIpStdPairAclSrcPrefLen = _RlIpStdPairAclSrcPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 5),
    _RlIpStdPairAclSrcPrefLen_Type()
)
rlIpStdPairAclSrcPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclSrcPrefLen.setStatus("current")
_RlIpStdPairAclDstIpAddrType_Type = InetAddressType
_RlIpStdPairAclDstIpAddrType_Object = MibTableColumn
rlIpStdPairAclDstIpAddrType = _RlIpStdPairAclDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 6),
    _RlIpStdPairAclDstIpAddrType_Type()
)
rlIpStdPairAclDstIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclDstIpAddrType.setStatus("current")
_RlIpStdPairAclDstIpAddr_Type = InetAddress
_RlIpStdPairAclDstIpAddr_Object = MibTableColumn
rlIpStdPairAclDstIpAddr = _RlIpStdPairAclDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 7),
    _RlIpStdPairAclDstIpAddr_Type()
)
rlIpStdPairAclDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclDstIpAddr.setStatus("current")


class _RlIpStdPairAclDstPrefLen_Type(InetAddressPrefixLength):
    """Custom type rlIpStdPairAclDstPrefLen based on InetAddressPrefixLength"""
    defaultValue = 32


_RlIpStdPairAclDstPrefLen_Type.__name__ = "InetAddressPrefixLength"
_RlIpStdPairAclDstPrefLen_Object = MibTableColumn
rlIpStdPairAclDstPrefLen = _RlIpStdPairAclDstPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 8),
    _RlIpStdPairAclDstPrefLen_Type()
)
rlIpStdPairAclDstPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclDstPrefLen.setStatus("current")


class _RlIpStdPairAclAction_Type(RlIpStdAclActionType):
    """Custom type rlIpStdPairAclAction based on RlIpStdAclActionType"""
    defaultValue = 2


_RlIpStdPairAclAction_Type.__name__ = "RlIpStdAclActionType"
_RlIpStdPairAclAction_Object = MibTableColumn
rlIpStdPairAclAction = _RlIpStdPairAclAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 9),
    _RlIpStdPairAclAction_Type()
)
rlIpStdPairAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclAction.setStatus("current")
_RlIpStdPairAclRowStatus_Type = RowStatus
_RlIpStdPairAclRowStatus_Object = MibTableColumn
rlIpStdPairAclRowStatus = _RlIpStdPairAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207, 4, 1, 10),
    _RlIpStdPairAclRowStatus_Type()
)
rlIpStdPairAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStdPairAclRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-IPSTDACL-MIB",
    **{"RlIpStdAclActionType": RlIpStdAclActionType,
       "RlIpStdAclStdClassificationType": RlIpStdAclStdClassificationType,
       "rlIpStdAcl": rlIpStdAcl,
       "rlIpStdAclTable": rlIpStdAclTable,
       "rlIpStdAclEntry": rlIpStdAclEntry,
       "rlIpStdAclAclName": rlIpStdAclAclName,
       "rlIpStdAclAceIndex": rlIpStdAclAceIndex,
       "rlIpStdAclSrcClassificationType": rlIpStdAclSrcClassificationType,
       "rlIpStdAclSrcIpAddrType": rlIpStdAclSrcIpAddrType,
       "rlIpStdAclSrcIpAddr": rlIpStdAclSrcIpAddr,
       "rlIpStdAclSrcPrefLen": rlIpStdAclSrcPrefLen,
       "rlIpStdAclDstClassificationType": rlIpStdAclDstClassificationType,
       "rlIpStdAclDstIpAddrType": rlIpStdAclDstIpAddrType,
       "rlIpStdAclDstIpAddr": rlIpStdAclDstIpAddr,
       "rlIpStdAclDstPrefLen": rlIpStdAclDstPrefLen,
       "rlIpStdAclAction": rlIpStdAclAction,
       "rlIpStdAclRowStatus": rlIpStdAclRowStatus,
       "rlIpStdAclFreeAceIndex": rlIpStdAclFreeAceIndex,
       "rlIpStdAclNameToIndexTable": rlIpStdAclNameToIndexTable,
       "rlIpStdAclNameToIndexEntry": rlIpStdAclNameToIndexEntry,
       "rlIpStdAclNameToIndexName": rlIpStdAclNameToIndexName,
       "rlIpStdAclNameToIndexIndex": rlIpStdAclNameToIndexIndex,
       "rlIpStdPairAclTable": rlIpStdPairAclTable,
       "rlIpStdPairAclEntry": rlIpStdPairAclEntry,
       "rlIpStdPairAclAclName": rlIpStdPairAclAclName,
       "rlIpStdPairAclAceIndex": rlIpStdPairAclAceIndex,
       "rlIpStdPairAclSrcIpAddrType": rlIpStdPairAclSrcIpAddrType,
       "rlIpStdPairAclSrcIpAddr": rlIpStdPairAclSrcIpAddr,
       "rlIpStdPairAclSrcPrefLen": rlIpStdPairAclSrcPrefLen,
       "rlIpStdPairAclDstIpAddrType": rlIpStdPairAclDstIpAddrType,
       "rlIpStdPairAclDstIpAddr": rlIpStdPairAclDstIpAddr,
       "rlIpStdPairAclDstPrefLen": rlIpStdPairAclDstPrefLen,
       "rlIpStdPairAclAction": rlIpStdPairAclAction,
       "rlIpStdPairAclRowStatus": rlIpStdPairAclRowStatus}
)
