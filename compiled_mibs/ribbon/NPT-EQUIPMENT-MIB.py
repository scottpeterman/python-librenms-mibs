# SNMP MIB module (NPT-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ribbon\NPT-EQUIPMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:18 2025
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

(eciNpti,) = mibBuilder.importSymbols(
    "NPT-ROOT-MIB",
    "eciNpti")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

equipmentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    equipmentMIB.setRevisions(
        ("2006-12-08 20:08",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Npt1800_ObjectIdentity = ObjectIdentity
npt1800 = _Npt1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    npt1800.setStatus("current")
_Npt1200i_ObjectIdentity = ObjectIdentity
npt1200i = _Npt1200i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    npt1200i.setStatus("current")
_Npt1050i_ObjectIdentity = ObjectIdentity
npt1050i = _Npt1050i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    npt1050i.setStatus("current")
_Npt1300_ObjectIdentity = ObjectIdentity
npt1300 = _Npt1300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    npt1300.setStatus("current")
_Npt1022_ObjectIdentity = ObjectIdentity
npt1022 = _Npt1022_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    npt1022.setStatus("current")
_Npt1250_ObjectIdentity = ObjectIdentity
npt1250 = _Npt1250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    npt1250.setStatus("current")
_Npt1100_ObjectIdentity = ObjectIdentity
npt1100 = _Npt1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    npt1100.setStatus("current")
_Npt2100A_ObjectIdentity = ObjectIdentity
npt2100A = _Npt2100A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 19)
)
if mibBuilder.loadTexts:
    npt2100A.setStatus("current")
_Npt2300_ObjectIdentity = ObjectIdentity
npt2300 = _Npt2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 20)
)
if mibBuilder.loadTexts:
    npt2300.setStatus("current")
_Npt2700_ObjectIdentity = ObjectIdentity
npt2700 = _Npt2700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    npt2700.setStatus("current")
_Npt1022B_ObjectIdentity = ObjectIdentity
npt1022B = _Npt1022B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    npt1022B.setStatus("current")
_Npt1012D_ObjectIdentity = ObjectIdentity
npt1012D = _Npt1012D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 23)
)
if mibBuilder.loadTexts:
    npt1012D.setStatus("current")
_Npt2400A_ObjectIdentity = ObjectIdentity
npt2400A = _Npt2400A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 24)
)
if mibBuilder.loadTexts:
    npt2400A.setStatus("current")
_Npt2507A_ObjectIdentity = ObjectIdentity
npt2507A = _Npt2507A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 25)
)
if mibBuilder.loadTexts:
    npt2507A.setStatus("current")
_Npt2714A_ObjectIdentity = ObjectIdentity
npt2714A = _Npt2714A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 1, 26)
)
if mibBuilder.loadTexts:
    npt2714A.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NPT-EQUIPMENT-MIB",
    **{"equipmentMIB": equipmentMIB,
       "npt1800": npt1800,
       "npt1200i": npt1200i,
       "npt1050i": npt1050i,
       "npt1300": npt1300,
       "npt1022": npt1022,
       "npt1250": npt1250,
       "npt1100": npt1100,
       "npt2100A": npt2100A,
       "npt2300": npt2300,
       "npt2700": npt2700,
       "npt1022B": npt1022B,
       "npt1012D": npt1012D,
       "npt2400A": npt2400A,
       "npt2507A": npt2507A,
       "npt2714A": npt2714A}
)
