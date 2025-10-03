# SNMP MIB module (TERRA-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\terra\TERRA-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:13 2025
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

(terraRoot,) = mibBuilder.importSymbols(
    "TERRA-SMI",
    "terraRoot")


# MODULE-IDENTITY

terraProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1)
)
if mibBuilder.loadTexts:
    terraProducts.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TerraOD120_ObjectIdentity = ObjectIdentity
terraOD120 = _TerraOD120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 1)
)
_TerraMO411_ObjectIdentity = ObjectIdentity
terraMO411 = _TerraMO411_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 2)
)
_TerraMO4x8_ObjectIdentity = ObjectIdentity
terraMO4x8 = _TerraMO4x8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 3)
)
_TerraUC412_ObjectIdentity = ObjectIdentity
terraUC412 = _TerraUC412_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 4)
)
_Terra_sda410C_ObjectIdentity = ObjectIdentity
terra_sda410C = _Terra_sda410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 5)
)
_Terra_sta410C_ObjectIdentity = ObjectIdentity
terra_sta410C = _Terra_sta410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 6)
)
_Terra_saa410C_ObjectIdentity = ObjectIdentity
terra_saa410C = _Terra_saa410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 7)
)
_Terra_sdi410C_ObjectIdentity = ObjectIdentity
terra_sdi410C = _Terra_sdi410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8)
)
_Terra_sti410C_ObjectIdentity = ObjectIdentity
terra_sti410C = _Terra_sti410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 9)
)
_Terra_sai410C_ObjectIdentity = ObjectIdentity
terra_sai410C = _Terra_sai410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 10)
)
_Terra_S2C16_ObjectIdentity = ObjectIdentity
terra_S2C16 = _Terra_S2C16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 11)
)
_TerraOT001M_ObjectIdentity = ObjectIdentity
terraOT001M = _TerraOT001M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 12)
)
_Terra_S2C16P_ObjectIdentity = ObjectIdentity
terra_S2C16P = _Terra_S2C16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 13)
)
_Terra_ttd440_ObjectIdentity = ObjectIdentity
terra_ttd440 = _Terra_ttd440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 14)
)
_Terra_ttx410C_ObjectIdentity = ObjectIdentity
terra_ttx410C = _Terra_ttx410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 15)
)
_Terra_tdx410C_ObjectIdentity = ObjectIdentity
terra_tdx410C = _Terra_tdx410C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 16)
)
_Terra_sdi480_ObjectIdentity = ObjectIdentity
terra_sdi480 = _Terra_sdi480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17)
)
_Terra_sti440_ObjectIdentity = ObjectIdentity
terra_sti440 = _Terra_sti440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18)
)
_Terra_ttq440_ObjectIdentity = ObjectIdentity
terra_ttq440 = _Terra_ttq440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 19)
)
_Terra_OAD514_ObjectIdentity = ObjectIdentity
terra_OAD514 = _Terra_OAD514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 20)
)
_Terra_ttq420C_ObjectIdentity = ObjectIdentity
terra_ttq420C = _Terra_ttq420C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 21)
)
_Terra_tdq420C_ObjectIdentity = ObjectIdentity
terra_tdq420C = _Terra_tdq420C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 22)
)
_Terra_ttx420C_ObjectIdentity = ObjectIdentity
terra_ttx420C = _Terra_ttx420C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 23)
)
_Terra_tdx420C_ObjectIdentity = ObjectIdentity
terra_tdx420C = _Terra_tdx420C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 24)
)
_Terra_ttq420_ObjectIdentity = ObjectIdentity
terra_ttq420 = _Terra_ttq420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 25)
)
_Terra_tdq420_ObjectIdentity = ObjectIdentity
terra_tdq420 = _Terra_tdq420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 26)
)
_Terra_ttx420_ObjectIdentity = ObjectIdentity
terra_ttx420 = _Terra_ttx420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 27)
)
_Terra_tdx420_ObjectIdentity = ObjectIdentity
terra_tdx420 = _Terra_tdx420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 28)
)
_Terra_mhi430_ObjectIdentity = ObjectIdentity
terra_mhi430 = _Terra_mhi430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 29)
)
_Terra_mix440_ObjectIdentity = ObjectIdentity
terra_mix440 = _Terra_mix440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 30)
)
_Terra_miq440_ObjectIdentity = ObjectIdentity
terra_miq440 = _Terra_miq440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 31)
)
_Terra_mid420_ObjectIdentity = ObjectIdentity
terra_mid420 = _Terra_mid420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 32)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERRA-PRODUCTS-MIB",
    **{"terraProducts": terraProducts,
       "terraOD120": terraOD120,
       "terraMO411": terraMO411,
       "terraMO4x8": terraMO4x8,
       "terraUC412": terraUC412,
       "terra-sda410C": terra_sda410C,
       "terra-sta410C": terra_sta410C,
       "terra-saa410C": terra_saa410C,
       "terra-sdi410C": terra_sdi410C,
       "terra-sti410C": terra_sti410C,
       "terra-sai410C": terra_sai410C,
       "terra-S2C16": terra_S2C16,
       "terraOT001M": terraOT001M,
       "terra-S2C16P": terra_S2C16P,
       "terra-ttd440": terra_ttd440,
       "terra-ttx410C": terra_ttx410C,
       "terra-tdx410C": terra_tdx410C,
       "terra-sdi480": terra_sdi480,
       "terra-sti440": terra_sti440,
       "terra-ttq440": terra_ttq440,
       "terra-OAD514": terra_OAD514,
       "terra-ttq420C": terra_ttq420C,
       "terra-tdq420C": terra_tdq420C,
       "terra-ttx420C": terra_ttx420C,
       "terra-tdx420C": terra_tdx420C,
       "terra-ttq420": terra_ttq420,
       "terra-tdq420": terra_tdq420,
       "terra-ttx420": terra_ttx420,
       "terra-tdx420": terra_tdx420,
       "terra-mhi430": terra_mhi430,
       "terra-mix440": terra_mix440,
       "terra-miq440": terra_miq440,
       "terra-mid420": terra_mid420}
)
