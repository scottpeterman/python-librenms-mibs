# SNMP MIB module (SIAE-UNITYPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-UNITYPE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:50 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

unitTypeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 506)
)
if mibBuilder.loadTexts:
    unitTypeMib.setRevisions(
        ("2016-10-14 00:00",
         "2016-07-19 00:00",
         "2016-04-05 00:00",
         "2015-03-04 00:00",
         "2014-12-01 00:00",
         "2014-03-19 00:00",
         "2014-02-07 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UnitType_ObjectIdentity = ObjectIdentity
unitType = _UnitType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3)
)
_UnitTypeUnequipped_ObjectIdentity = ObjectIdentity
unitTypeUnequipped = _UnitTypeUnequipped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1)
)
if mibBuilder.loadTexts:
    unitTypeUnequipped.setStatus("current")
_UnitTypeODU_ObjectIdentity = ObjectIdentity
unitTypeODU = _UnitTypeODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 5)
)
if mibBuilder.loadTexts:
    unitTypeODU.setStatus("current")
_UnitTypeALFO80HD_ObjectIdentity = ObjectIdentity
unitTypeALFO80HD = _UnitTypeALFO80HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 200)
)
if mibBuilder.loadTexts:
    unitTypeALFO80HD.setStatus("current")
_UnitTypeALFO80HDelectrical_ObjectIdentity = ObjectIdentity
unitTypeALFO80HDelectrical = _UnitTypeALFO80HDelectrical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 201)
)
if mibBuilder.loadTexts:
    unitTypeALFO80HDelectrical.setStatus("current")
_UnitTypeALFO80HDelectricalOptical_ObjectIdentity = ObjectIdentity
unitTypeALFO80HDelectricalOptical = _UnitTypeALFO80HDelectricalOptical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 202)
)
if mibBuilder.loadTexts:
    unitTypeALFO80HDelectricalOptical.setStatus("current")
_UnitTypeALFO80HDoptical_ObjectIdentity = ObjectIdentity
unitTypeALFO80HDoptical = _UnitTypeALFO80HDoptical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 203)
)
if mibBuilder.loadTexts:
    unitTypeALFO80HDoptical.setStatus("current")
_UnitTypeAGS20ARI1_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI1 = _UnitTypeAGS20ARI1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 210)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI1.setStatus("current")
_UnitTypeAGS20ARI2_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2 = _UnitTypeAGS20ARI2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 211)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2.setStatus("current")
_UnitTypeAGS20ARI4_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI4 = _UnitTypeAGS20ARI4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 212)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI4.setStatus("current")
_UnitTypeAGS20DRI4_ObjectIdentity = ObjectIdentity
unitTypeAGS20DRI4 = _UnitTypeAGS20DRI4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 213)
)
if mibBuilder.loadTexts:
    unitTypeAGS20DRI4.setStatus("current")
_UnitTypeAGS20ARI1TDM2_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI1TDM2 = _UnitTypeAGS20ARI1TDM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 214)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI1TDM2.setStatus("current")
_UnitTypeAGS20ARI1TDM3_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI1TDM3 = _UnitTypeAGS20ARI1TDM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 215)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI1TDM3.setStatus("current")
_UnitTypeAGS20ARI2TDM2_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2TDM2 = _UnitTypeAGS20ARI2TDM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 216)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2TDM2.setStatus("current")
_UnitTypeAGS20ARI2TDM3_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2TDM3 = _UnitTypeAGS20ARI2TDM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 217)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2TDM3.setStatus("current")
_UnitTypeAGS20ARI4TDM2_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI4TDM2 = _UnitTypeAGS20ARI4TDM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 218)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI4TDM2.setStatus("current")
_UnitTypeAGS20ARI4TDM3_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI4TDM3 = _UnitTypeAGS20ARI4TDM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 219)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI4TDM3.setStatus("current")
_UnitTypeAGS20DRI4TDM2_ObjectIdentity = ObjectIdentity
unitTypeAGS20DRI4TDM2 = _UnitTypeAGS20DRI4TDM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 220)
)
if mibBuilder.loadTexts:
    unitTypeAGS20DRI4TDM2.setStatus("current")
_UnitTypeAGS20DRI4TDM3_ObjectIdentity = ObjectIdentity
unitTypeAGS20DRI4TDM3 = _UnitTypeAGS20DRI4TDM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 221)
)
if mibBuilder.loadTexts:
    unitTypeAGS20DRI4TDM3.setStatus("current")
_UnitTypeAGS20CORE_ObjectIdentity = ObjectIdentity
unitTypeAGS20CORE = _UnitTypeAGS20CORE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 222)
)
if mibBuilder.loadTexts:
    unitTypeAGS20CORE.setStatus("current")
_UnitTypeAGS20ARI1DP_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI1DP = _UnitTypeAGS20ARI1DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 223)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI1DP.setStatus("current")
_UnitTypeAGS20ARI1TDM2DP_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI1TDM2DP = _UnitTypeAGS20ARI1TDM2DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 224)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI1TDM2DP.setStatus("current")
_UnitTypeAGS20ARI1TDM3DP_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI1TDM3DP = _UnitTypeAGS20ARI1TDM3DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 225)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI1TDM3DP.setStatus("current")
_UnitTypeALFOplus1_ObjectIdentity = ObjectIdentity
unitTypeALFOplus1 = _UnitTypeALFOplus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 229)
)
if mibBuilder.loadTexts:
    unitTypeALFOplus1.setStatus("current")
_UnitTypeALFOplus2_ObjectIdentity = ObjectIdentity
unitTypeALFOplus2 = _UnitTypeALFOplus2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 230)
)
if mibBuilder.loadTexts:
    unitTypeALFOplus2.setStatus("current")
_UnitTypeAGS20ODU_ObjectIdentity = ObjectIdentity
unitTypeAGS20ODU = _UnitTypeAGS20ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 231)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ODU.setStatus("current")
_UnitTypeAGS20ARI1TDM2LC_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI1TDM2LC = _UnitTypeAGS20ARI1TDM2LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 240)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI1TDM2LC.setStatus("current")
_UnitTypeAGS20ARI2XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2XG = _UnitTypeAGS20ARI2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 250)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2XG.setStatus("current")
_UnitTypeAGS20ARI2TDM2XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2TDM2XG = _UnitTypeAGS20ARI2TDM2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 251)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2TDM2XG.setStatus("current")
_UnitTypeAGS20ARI2TDM3XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2TDM3XG = _UnitTypeAGS20ARI2TDM3XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 252)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2TDM3XG.setStatus("current")
_UnitTypeAGS20ARI4XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI4XG = _UnitTypeAGS20ARI4XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 253)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI4XG.setStatus("current")
_UnitTypeAGS20ARI4TDM2XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI4TDM2XG = _UnitTypeAGS20ARI4TDM2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 254)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI4TDM2XG.setStatus("current")
_UnitTypeAGS20ARI4TDM3XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI4TDM3XG = _UnitTypeAGS20ARI4TDM3XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 255)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI4TDM3XG.setStatus("current")
_UnitTypeAGS20ARI2E_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2E = _UnitTypeAGS20ARI2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 260)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2E.setStatus("current")
_UnitTypeAGS20ARI2ETDM2_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2ETDM2 = _UnitTypeAGS20ARI2ETDM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 261)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2ETDM2.setStatus("current")
_UnitTypeAGS20ARI2ETDM3_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2ETDM3 = _UnitTypeAGS20ARI2ETDM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 262)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2ETDM3.setStatus("current")
_UnitTypeAGS20ARI2EXG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2EXG = _UnitTypeAGS20ARI2EXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 263)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2EXG.setStatus("current")
_UnitTypeAGS20ARI2ETDM2XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2ETDM2XG = _UnitTypeAGS20ARI2ETDM2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 264)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2ETDM2XG.setStatus("current")
_UnitTypeAGS20ARI2ETDM3XG_ObjectIdentity = ObjectIdentity
unitTypeAGS20ARI2ETDM3XG = _UnitTypeAGS20ARI2ETDM3XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 265)
)
if mibBuilder.loadTexts:
    unitTypeAGS20ARI2ETDM3XG.setStatus("current")
_UnitTypeALFO80HDx_ObjectIdentity = ObjectIdentity
unitTypeALFO80HDx = _UnitTypeALFO80HDx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 280)
)
if mibBuilder.loadTexts:
    unitTypeALFO80HDx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-UNITYPE-MIB",
    **{"unitType": unitType,
       "unitTypeUnequipped": unitTypeUnequipped,
       "unitTypeODU": unitTypeODU,
       "unitTypeALFO80HD": unitTypeALFO80HD,
       "unitTypeALFO80HDelectrical": unitTypeALFO80HDelectrical,
       "unitTypeALFO80HDelectricalOptical": unitTypeALFO80HDelectricalOptical,
       "unitTypeALFO80HDoptical": unitTypeALFO80HDoptical,
       "unitTypeAGS20ARI1": unitTypeAGS20ARI1,
       "unitTypeAGS20ARI2": unitTypeAGS20ARI2,
       "unitTypeAGS20ARI4": unitTypeAGS20ARI4,
       "unitTypeAGS20DRI4": unitTypeAGS20DRI4,
       "unitTypeAGS20ARI1TDM2": unitTypeAGS20ARI1TDM2,
       "unitTypeAGS20ARI1TDM3": unitTypeAGS20ARI1TDM3,
       "unitTypeAGS20ARI2TDM2": unitTypeAGS20ARI2TDM2,
       "unitTypeAGS20ARI2TDM3": unitTypeAGS20ARI2TDM3,
       "unitTypeAGS20ARI4TDM2": unitTypeAGS20ARI4TDM2,
       "unitTypeAGS20ARI4TDM3": unitTypeAGS20ARI4TDM3,
       "unitTypeAGS20DRI4TDM2": unitTypeAGS20DRI4TDM2,
       "unitTypeAGS20DRI4TDM3": unitTypeAGS20DRI4TDM3,
       "unitTypeAGS20CORE": unitTypeAGS20CORE,
       "unitTypeAGS20ARI1DP": unitTypeAGS20ARI1DP,
       "unitTypeAGS20ARI1TDM2DP": unitTypeAGS20ARI1TDM2DP,
       "unitTypeAGS20ARI1TDM3DP": unitTypeAGS20ARI1TDM3DP,
       "unitTypeALFOplus1": unitTypeALFOplus1,
       "unitTypeALFOplus2": unitTypeALFOplus2,
       "unitTypeAGS20ODU": unitTypeAGS20ODU,
       "unitTypeAGS20ARI1TDM2LC": unitTypeAGS20ARI1TDM2LC,
       "unitTypeAGS20ARI2XG": unitTypeAGS20ARI2XG,
       "unitTypeAGS20ARI2TDM2XG": unitTypeAGS20ARI2TDM2XG,
       "unitTypeAGS20ARI2TDM3XG": unitTypeAGS20ARI2TDM3XG,
       "unitTypeAGS20ARI4XG": unitTypeAGS20ARI4XG,
       "unitTypeAGS20ARI4TDM2XG": unitTypeAGS20ARI4TDM2XG,
       "unitTypeAGS20ARI4TDM3XG": unitTypeAGS20ARI4TDM3XG,
       "unitTypeAGS20ARI2E": unitTypeAGS20ARI2E,
       "unitTypeAGS20ARI2ETDM2": unitTypeAGS20ARI2ETDM2,
       "unitTypeAGS20ARI2ETDM3": unitTypeAGS20ARI2ETDM3,
       "unitTypeAGS20ARI2EXG": unitTypeAGS20ARI2EXG,
       "unitTypeAGS20ARI2ETDM2XG": unitTypeAGS20ARI2ETDM2XG,
       "unitTypeAGS20ARI2ETDM3XG": unitTypeAGS20ARI2ETDM3XG,
       "unitTypeALFO80HDx": unitTypeALFO80HDx,
       "unitTypeMib": unitTypeMib}
)
