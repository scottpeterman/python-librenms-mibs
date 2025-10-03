# SNMP MIB module (WISI-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wisi\WISI-ROOT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:17 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wisi_ObjectIdentity = ObjectIdentity
wisi = _Wisi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465)
)
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 1)
)
_Devices_ObjectIdentity = ObjectIdentity
devices = _Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2)
)
_Hfc_ObjectIdentity = ObjectIdentity
hfc = _Hfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 1)
)
_Transponders_ObjectIdentity = ObjectIdentity
transponders = _Transponders_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 2)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 3)
)
_IoBoards_ObjectIdentity = ObjectIdentity
ioBoards = _IoBoards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 4)
)
_Compact_ObjectIdentity = ObjectIdentity
compact = _Compact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 5)
)
_Headend_ObjectIdentity = ObjectIdentity
headend = _Headend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 6)
)
_Scrambler_ObjectIdentity = ObjectIdentity
scrambler = _Scrambler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 7)
)
_Remultiplexer_ObjectIdentity = ObjectIdentity
remultiplexer = _Remultiplexer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 8)
)
_Tangram_ObjectIdentity = ObjectIdentity
tangram = _Tangram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WISI-ROOT-MIB",
    **{"wisi": wisi,
       "equipment": equipment,
       "common": common,
       "devices": devices,
       "hfc": hfc,
       "transponders": transponders,
       "configuration": configuration,
       "ioBoards": ioBoards,
       "compact": compact,
       "headend": headend,
       "scrambler": scrambler,
       "remultiplexer": remultiplexer,
       "tangram": tangram}
)
