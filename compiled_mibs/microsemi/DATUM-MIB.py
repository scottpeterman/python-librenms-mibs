# SNMP MIB module (DATUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsemi\DATUM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:31 2025
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

_Datum_ObjectIdentity = ObjectIdentity
datum = _Datum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601)
)
_Bancomm_ObjectIdentity = ObjectIdentity
bancomm = _Bancomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 1)
)
_Timing_ObjectIdentity = ObjectIdentity
timing = _Timing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 2)
)
_Austron_ObjectIdentity = ObjectIdentity
austron = _Austron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1)
)
_Ssu2000_ObjectIdentity = ObjectIdentity
ssu2000 = _Ssu2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1)
)
_Ot21_ObjectIdentity = ObjectIdentity
ot21 = _Ot21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 2)
)
_Fts_ObjectIdentity = ObjectIdentity
fts = _Fts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 4)
)
_Efratom_ObjectIdentity = ObjectIdentity
efratom = _Efratom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 5)
)
_Experiment_ObjectIdentity = ObjectIdentity
experiment = _Experiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 99)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATUM-MIB",
    **{"datum": datum,
       "bancomm": bancomm,
       "timing": timing,
       "austron": austron,
       "products": products,
       "ssu2000": ssu2000,
       "ot21": ot21,
       "fts": fts,
       "efratom": efratom,
       "experiment": experiment}
)
