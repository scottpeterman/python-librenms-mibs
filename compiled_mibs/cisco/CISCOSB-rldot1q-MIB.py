# SNMP MIB module (CISCOSB-rldot1q-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-rldot1q-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:36 2025
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

(rlpBridgeMIBObjects,) = mibBuilder.importSymbols(
    "CISCOSB-BRIDGEMIBOBJECTS-MIB",
    "rlpBridgeMIBObjects")

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,
 dot1qStaticUnicastEntry,
 dot1qTpFdbEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qStaticUnicastEntry",
    "dot1qTpFdbEntry")

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

rlq_bridge_mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rldot1q_ObjectIdentity = ObjectIdentity
rldot1q = _Rldot1q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8)
)
_Rldot1qStaticUnicastTable_Object = MibTable
rldot1qStaticUnicastTable = _Rldot1qStaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 1)
)
if mibBuilder.loadTexts:
    rldot1qStaticUnicastTable.setStatus("current")
_Rldot1qStaticUnicastEntry_Object = MibTableRow
rldot1qStaticUnicastEntry = _Rldot1qStaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 1, 1)
)
if mibBuilder.loadTexts:
    rldot1qStaticUnicastEntry.setStatus("current")


class _Rldot1qStaticUnicastAddressOwner_Type(Integer32):
    """Custom type rldot1qStaticUnicastAddressOwner based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("learned", 2))
    )


_Rldot1qStaticUnicastAddressOwner_Type.__name__ = "Integer32"
_Rldot1qStaticUnicastAddressOwner_Object = MibTableColumn
rldot1qStaticUnicastAddressOwner = _Rldot1qStaticUnicastAddressOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 1, 1, 1),
    _Rldot1qStaticUnicastAddressOwner_Type()
)
rldot1qStaticUnicastAddressOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qStaticUnicastAddressOwner.setStatus("current")
_Rldot1qTpFdbTable_Object = MibTable
rldot1qTpFdbTable = _Rldot1qTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 2)
)
if mibBuilder.loadTexts:
    rldot1qTpFdbTable.setStatus("current")
_Rldot1qTpFdbEntry_Object = MibTableRow
rldot1qTpFdbEntry = _Rldot1qTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 2, 1)
)
if mibBuilder.loadTexts:
    rldot1qTpFdbEntry.setStatus("current")


class _Rldot1qTpFdbSubStatus_Type(Integer32):
    """Custom type rldot1qTpFdbSubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dynamic-static", 2))
    )


_Rldot1qTpFdbSubStatus_Type.__name__ = "Integer32"
_Rldot1qTpFdbSubStatus_Object = MibTableColumn
rldot1qTpFdbSubStatus = _Rldot1qTpFdbSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 2, 1, 1),
    _Rldot1qTpFdbSubStatus_Type()
)
rldot1qTpFdbSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1qTpFdbSubStatus.setStatus("current")
_Rldot1qTpFdbCountTable_Object = MibTable
rldot1qTpFdbCountTable = _Rldot1qTpFdbCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 3)
)
if mibBuilder.loadTexts:
    rldot1qTpFdbCountTable.setStatus("current")
_Rldot1qTpFdbCountEntry_Object = MibTableRow
rldot1qTpFdbCountEntry = _Rldot1qTpFdbCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 3, 1)
)
rldot1qTpFdbCountEntry.setIndexNames(
    (0, "CISCOSB-rldot1q-MIB", "rldot1qTpFdbCountVlanTag"),
    (0, "CISCOSB-rldot1q-MIB", "rldot1qTpFdbCountPort"),
    (0, "CISCOSB-rldot1q-MIB", "rldot1qTpFdbCountType"),
)
if mibBuilder.loadTexts:
    rldot1qTpFdbCountEntry.setStatus("current")


class _Rldot1qTpFdbCountVlanTag_Type(Integer32):
    """Custom type rldot1qTpFdbCountVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Rldot1qTpFdbCountVlanTag_Type.__name__ = "Integer32"
_Rldot1qTpFdbCountVlanTag_Object = MibTableColumn
rldot1qTpFdbCountVlanTag = _Rldot1qTpFdbCountVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 3, 1, 1),
    _Rldot1qTpFdbCountVlanTag_Type()
)
rldot1qTpFdbCountVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1qTpFdbCountVlanTag.setStatus("current")
_Rldot1qTpFdbCountPort_Type = Integer32
_Rldot1qTpFdbCountPort_Object = MibTableColumn
rldot1qTpFdbCountPort = _Rldot1qTpFdbCountPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 3, 1, 2),
    _Rldot1qTpFdbCountPort_Type()
)
rldot1qTpFdbCountPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1qTpFdbCountPort.setStatus("current")


class _Rldot1qTpFdbCountType_Type(Integer32):
    """Custom type rldot1qTpFdbCountType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5),
          ("multicast", 6),
          ("ipv4Host", 7),
          ("ipv6Host", 8))
    )


_Rldot1qTpFdbCountType_Type.__name__ = "Integer32"
_Rldot1qTpFdbCountType_Object = MibTableColumn
rldot1qTpFdbCountType = _Rldot1qTpFdbCountType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 3, 1, 3),
    _Rldot1qTpFdbCountType_Type()
)
rldot1qTpFdbCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1qTpFdbCountType.setStatus("current")
_Rldot1qTpFdbCountCount_Type = Integer32
_Rldot1qTpFdbCountCount_Object = MibTableColumn
rldot1qTpFdbCountCount = _Rldot1qTpFdbCountCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 8, 3, 1, 4),
    _Rldot1qTpFdbCountCount_Type()
)
rldot1qTpFdbCountCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1qTpFdbCountCount.setStatus("current")
dot1qStaticUnicastEntry.registerAugmentions(
    ("CISCOSB-rldot1q-MIB",
     "rldot1qStaticUnicastEntry")
)
rldot1qStaticUnicastEntry.setIndexNames(*dot1qStaticUnicastEntry.getIndexNames())
dot1qTpFdbEntry.registerAugmentions(
    ("CISCOSB-rldot1q-MIB",
     "rldot1qTpFdbEntry")
)
rldot1qTpFdbEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-rldot1q-MIB",
    **{"rlq-bridge-mib": rlq_bridge_mib,
       "rldot1q": rldot1q,
       "rldot1qStaticUnicastTable": rldot1qStaticUnicastTable,
       "rldot1qStaticUnicastEntry": rldot1qStaticUnicastEntry,
       "rldot1qStaticUnicastAddressOwner": rldot1qStaticUnicastAddressOwner,
       "rldot1qTpFdbTable": rldot1qTpFdbTable,
       "rldot1qTpFdbEntry": rldot1qTpFdbEntry,
       "rldot1qTpFdbSubStatus": rldot1qTpFdbSubStatus,
       "rldot1qTpFdbCountTable": rldot1qTpFdbCountTable,
       "rldot1qTpFdbCountEntry": rldot1qTpFdbCountEntry,
       "rldot1qTpFdbCountVlanTag": rldot1qTpFdbCountVlanTag,
       "rldot1qTpFdbCountPort": rldot1qTpFdbCountPort,
       "rldot1qTpFdbCountType": rldot1qTpFdbCountType,
       "rldot1qTpFdbCountCount": rldot1qTpFdbCountCount}
)
