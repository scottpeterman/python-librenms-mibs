# SNMP MIB module (BROCADE-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\brocade\BROCADE-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:15 2025
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

(bcsiReg,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiReg")

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

brocadeProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3)
)
if mibBuilder.loadTexts:
    brocadeProductsMIB.setRevisions(
        ("2012-02-03 00:00",
         "2013-11-21 00:00",
         "2013-09-25 13:00",
         "2014-10-07 14:05",
         "2015-08-11 13:05")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrocadeProducts_ObjectIdentity = ObjectIdentity
brocadeProducts = _BrocadeProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1)
)
_Vdx6740_ObjectIdentity = ObjectIdentity
vdx6740 = _Vdx6740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 131)
)
_Vdx6740T_ObjectIdentity = ObjectIdentity
vdx6740T = _Vdx6740T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 137)
)
_Vdx2740_ObjectIdentity = ObjectIdentity
vdx2740 = _Vdx2740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 138)
)
_Vdx6740T1G_ObjectIdentity = ObjectIdentity
vdx6740T1G = _Vdx6740T1G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 151)
)
_Vdx6940Q36_ObjectIdentity = ObjectIdentity
vdx6940Q36 = _Vdx6940Q36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 153)
)
_Vdx6940S144_ObjectIdentity = ObjectIdentity
vdx6940S144 = _Vdx6940S144_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 164)
)
_Vdx8770S4_ObjectIdentity = ObjectIdentity
vdx8770S4 = _Vdx8770S4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1000)
)
_Vdx8770S8_ObjectIdentity = ObjectIdentity
vdx8770S8 = _Vdx8770S8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1001)
)
_Vdx8770S16_ObjectIdentity = ObjectIdentity
vdx8770S16 = _Vdx8770S16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1002)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-PRODUCTS-MIB",
    **{"brocadeProductsMIB": brocadeProductsMIB,
       "brocadeProducts": brocadeProducts,
       "vdx6740": vdx6740,
       "vdx6740T": vdx6740T,
       "vdx2740": vdx2740,
       "vdx6740T1G": vdx6740T1G,
       "vdx6940Q36": vdx6940Q36,
       "vdx6940S144": vdx6940S144,
       "vdx8770S4": vdx8770S4,
       "vdx8770S8": vdx8770S8,
       "vdx8770S16": vdx8770S16}
)
