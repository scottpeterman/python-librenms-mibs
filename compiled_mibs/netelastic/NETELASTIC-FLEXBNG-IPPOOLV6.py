# SNMP MIB module (NETELASTIC-FLEXBNG-IPPOOLV6) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\netelastic\NETELASTIC-FLEXBNG-IPPOOLV6
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:44 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(bras,) = mibBuilder.importSymbols(
    "NETELASTIC-FLEXBNG-MIB",
    "bras")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ippoolv6Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ippoolv6Mib.setRevisions(
        ("2016-12-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class V6pool_status(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 0),
          ("lock", 1))
    )



# MIB Managed Objects in the order of their OIDs

_DelegationPoolTable_Object = MibTable
delegationPoolTable = _DelegationPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    delegationPoolTable.setStatus("current")
_DelegationPoolEntry_Object = MibTableRow
delegationPoolEntry = _DelegationPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 1, 1)
)
delegationPoolEntry.setIndexNames(
    (0, "NETELASTIC-FLEXBNG-IPPOOLV6", "delegationGroupName"),
)
if mibBuilder.loadTexts:
    delegationPoolEntry.setStatus("current")
_DelegationGroupName_Type = String
_DelegationGroupName_Object = MibTableColumn
delegationGroupName = _DelegationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 1, 1, 1),
    _DelegationGroupName_Type()
)
delegationGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delegationGroupName.setStatus("current")
_PrefixAllocatePercent_Type = Unsigned32
_PrefixAllocatePercent_Object = MibTableColumn
prefixAllocatePercent = _PrefixAllocatePercent_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 1, 1, 2),
    _PrefixAllocatePercent_Type()
)
prefixAllocatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prefixAllocatePercent.setStatus("current")
_AddrPoolTable_Object = MibTable
addrPoolTable = _AddrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    addrPoolTable.setStatus("current")
_AddrPoolEntry_Object = MibTableRow
addrPoolEntry = _AddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 2, 1)
)
addrPoolEntry.setIndexNames(
    (0, "NETELASTIC-FLEXBNG-IPPOOLV6", "addrGroupName"),
)
if mibBuilder.loadTexts:
    addrPoolEntry.setStatus("current")
_AddrGroupName_Type = String
_AddrGroupName_Object = MibTableColumn
addrGroupName = _AddrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 2, 1, 1),
    _AddrGroupName_Type()
)
addrGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrGroupName.setStatus("current")
_VrfName_Type = String
_VrfName_Object = MibTableColumn
vrfName = _VrfName_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 2, 1, 2),
    _VrfName_Type()
)
vrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrfName.setStatus("current")
_RangeTable_Object = MibTable
rangeTable = _RangeTable_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rangeTable.setStatus("current")
_RangeEntry_Object = MibTableRow
rangeEntry = _RangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 3, 1)
)
rangeEntry.setIndexNames(
    (0, "NETELASTIC-FLEXBNG-IPPOOLV6", "addrGroupName"),
    (0, "NETELASTIC-FLEXBNG-IPPOOLV6", "startIPv6"),
    (0, "NETELASTIC-FLEXBNG-IPPOOLV6", "endIPv6"),
)
if mibBuilder.loadTexts:
    rangeEntry.setStatus("current")
_StartIPv6_Type = Ipv6Address
_StartIPv6_Object = MibTableColumn
startIPv6 = _StartIPv6_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 3, 1, 1),
    _StartIPv6_Type()
)
startIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startIPv6.setStatus("current")
_EndIPv6_Type = Ipv6Address
_EndIPv6_Object = MibTableColumn
endIPv6 = _EndIPv6_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 3, 1, 2),
    _EndIPv6_Type()
)
endIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endIPv6.setStatus("current")
_AddrAllocatePercent_Type = Unsigned32
_AddrAllocatePercent_Object = MibTableColumn
addrAllocatePercent = _AddrAllocatePercent_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 3, 3, 1, 3),
    _AddrAllocatePercent_Type()
)
addrAllocatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrAllocatePercent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETELASTIC-FLEXBNG-IPPOOLV6",
    **{"ConfdString": ConfdString,
       "String": String,
       "V6pool-status": V6pool_status,
       "ippoolv6Mib": ippoolv6Mib,
       "delegationPoolTable": delegationPoolTable,
       "delegationPoolEntry": delegationPoolEntry,
       "delegationGroupName": delegationGroupName,
       "prefixAllocatePercent": prefixAllocatePercent,
       "addrPoolTable": addrPoolTable,
       "addrPoolEntry": addrPoolEntry,
       "addrGroupName": addrGroupName,
       "vrfName": vrfName,
       "rangeTable": rangeTable,
       "rangeEntry": rangeEntry,
       "startIPv6": startIPv6,
       "endIPv6": endIPv6,
       "addrAllocatePercent": addrAllocatePercent}
)
