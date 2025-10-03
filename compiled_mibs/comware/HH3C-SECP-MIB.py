# SNMP MIB module (HH3C-SECP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SECP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:51 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSecp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166)
)
if mibBuilder.loadTexts:
    hh3cSecp.setRevisions(
        ("2016-12-19 16:05",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSecpObjects_ObjectIdentity = ObjectIdentity
hh3cSecpObjects = _Hh3cSecpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166, 1)
)
_Hh3cSecpRunningInfoTable_Object = MibTable
hh3cSecpRunningInfoTable = _Hh3cSecpRunningInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSecpRunningInfoTable.setStatus("current")
_Hh3cSecpRunningInfoEntry_Object = MibTableRow
hh3cSecpRunningInfoEntry = _Hh3cSecpRunningInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166, 1, 1, 1)
)
hh3cSecpRunningInfoEntry.setIndexNames(
    (0, "HH3C-SECP-MIB", "hh3cSecpIPVersion"),
    (0, "HH3C-SECP-MIB", "hh3cSecpRuleID"),
)
if mibBuilder.loadTexts:
    hh3cSecpRunningInfoEntry.setStatus("current")


class _Hh3cSecpIPVersion_Type(Integer32):
    """Custom type hh3cSecpIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_Hh3cSecpIPVersion_Type.__name__ = "Integer32"
_Hh3cSecpIPVersion_Object = MibTableColumn
hh3cSecpIPVersion = _Hh3cSecpIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166, 1, 1, 1, 1),
    _Hh3cSecpIPVersion_Type()
)
hh3cSecpIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSecpIPVersion.setStatus("current")


class _Hh3cSecpRuleID_Type(Unsigned32):
    """Custom type hh3cSecpRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cSecpRuleID_Type.__name__ = "Unsigned32"
_Hh3cSecpRuleID_Object = MibTableColumn
hh3cSecpRuleID = _Hh3cSecpRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166, 1, 1, 1, 2),
    _Hh3cSecpRuleID_Type()
)
hh3cSecpRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSecpRuleID.setStatus("current")
_Hh3cSecpMatchPacketCount_Type = Counter64
_Hh3cSecpMatchPacketCount_Object = MibTableColumn
hh3cSecpMatchPacketCount = _Hh3cSecpMatchPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166, 1, 1, 1, 3),
    _Hh3cSecpMatchPacketCount_Type()
)
hh3cSecpMatchPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSecpMatchPacketCount.setStatus("current")
_Hh3cSecpLastMatchTime_Type = Unsigned32
_Hh3cSecpLastMatchTime_Object = MibTableColumn
hh3cSecpLastMatchTime = _Hh3cSecpLastMatchTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 166, 1, 1, 1, 4),
    _Hh3cSecpLastMatchTime_Type()
)
hh3cSecpLastMatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSecpLastMatchTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SECP-MIB",
    **{"hh3cSecp": hh3cSecp,
       "hh3cSecpObjects": hh3cSecpObjects,
       "hh3cSecpRunningInfoTable": hh3cSecpRunningInfoTable,
       "hh3cSecpRunningInfoEntry": hh3cSecpRunningInfoEntry,
       "hh3cSecpIPVersion": hh3cSecpIPVersion,
       "hh3cSecpRuleID": hh3cSecpRuleID,
       "hh3cSecpMatchPacketCount": hh3cSecpMatchPacketCount,
       "hh3cSecpLastMatchTime": hh3cSecpLastMatchTime}
)
