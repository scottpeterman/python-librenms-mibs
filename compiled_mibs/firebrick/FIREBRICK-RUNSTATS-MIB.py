# SNMP MIB module (FIREBRICK-RUNSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\firebrick\FIREBRICK-RUNSTATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:39 2025
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

(firebrickNewStyle,) = mibBuilder.importSymbols(
    "FIREBRICK-MIB",
    "firebrickNewStyle")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fbRunMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 3)
)
if mibBuilder.loadTexts:
    fbRunMib.setRevisions(
        ("2020-06-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbRunStatsTable_Object = MibTable
fbRunStatsTable = _FbRunStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 3, 1)
)
if mibBuilder.loadTexts:
    fbRunStatsTable.setStatus("current")
_FbRunStatsEntry_Object = MibTableRow
fbRunStatsEntry = _FbRunStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1)
)
fbRunStatsEntry.setIndexNames(
    (0, "FIREBRICK-RUNSTATS-MIB", "fbRunCore"),
)
if mibBuilder.loadTexts:
    fbRunStatsEntry.setStatus("current")
_FbRunBuffers_Type = Gauge32
_FbRunBuffers_Object = MibTableColumn
fbRunBuffers = _FbRunBuffers_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 1),
    _FbRunBuffers_Type()
)
fbRunBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbRunBuffers.setStatus("current")
_FbRunCore_Type = Integer32
_FbRunCore_Object = MibTableColumn
fbRunCore = _FbRunCore_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 2),
    _FbRunCore_Type()
)
fbRunCore.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbRunCore.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-RUNSTATS-MIB",
    **{"fbRunMib": fbRunMib,
       "fbRunStatsTable": fbRunStatsTable,
       "fbRunStatsEntry": fbRunStatsEntry,
       "fbRunBuffers": fbRunBuffers,
       "fbRunCore": fbRunCore}
)
