# SNMP MIB module (ALU-SAR-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALU-SAR-GLOBAL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:37 2025
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

(tmnxBasedProducts,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "tmnxBasedProducts")


# MODULE-IDENTITY

aluSARGlobalMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aluSARGlobalMIBModule.setRevisions(
        ("1911-12-06 10:00",
         "1911-12-06 00:00",
         "1910-12-20 00:00",
         "1910-08-13 00:00",
         "1908-01-23 00:00",
         "1908-08-27 00:00",
         "1908-06-03 00:00",
         "1908-01-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluServiceAggrRouters_ObjectIdentity = ObjectIdentity
aluServiceAggrRouters = _AluServiceAggrRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1)
)
_AluSARRegistry_ObjectIdentity = ObjectIdentity
aluSARRegistry = _AluSARRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1)
)
_AluSARModules_ObjectIdentity = ObjectIdentity
aluSARModules = _AluSARModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1)
)
_AluSARMIBModules_ObjectIdentity = ObjectIdentity
aluSARMIBModules = _AluSARMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3)
)
_AluSARCapabilityModule_ObjectIdentity = ObjectIdentity
aluSARCapabilityModule = _AluSARCapabilityModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 4)
)
_AluSAR7705CapModule_ObjectIdentity = ObjectIdentity
aluSAR7705CapModule = _AluSAR7705CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 4, 1)
)
_AluSAR7705ServiceAggrRouters_ObjectIdentity = ObjectIdentity
aluSAR7705ServiceAggrRouters = _AluSAR7705ServiceAggrRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2)
)
_AluSARModel7705SAR8Reg_ObjectIdentity = ObjectIdentity
aluSARModel7705SAR8Reg = _AluSARModel7705SAR8Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aluSARModel7705SAR8Reg.setStatus("current")
_AluSARModel7705SARfReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARfReg = _AluSARModel7705SARfReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARfReg.setStatus("current")
_AluSARModel7705SAR18Reg_ObjectIdentity = ObjectIdentity
aluSARModel7705SAR18Reg = _AluSARModel7705SAR18Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aluSARModel7705SAR18Reg.setStatus("current")
_AluSARModel7705SARmReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARmReg = _AluSARModel7705SARmReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARmReg.setStatus("current")
_AluSARModel7705SARmeReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARmeReg = _AluSARModel7705SARmeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARmeReg.setStatus("current")
_AluSARModel7705SARmlAReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARmlAReg = _AluSARModel7705SARmlAReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARmlAReg.setStatus("current")
_AluSARModel7705SARmlBReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARmlBReg = _AluSARModel7705SARmlBReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARmlBReg.setStatus("current")
_AluSARModel7705SARmlCReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARmlCReg = _AluSARModel7705SARmlCReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARmlCReg.setStatus("current")
_AluSARModel7705SARmlDReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARmlDReg = _AluSARModel7705SARmlDReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARmlDReg.setStatus("current")
_AluSARModel7705SARmlEReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARmlEReg = _AluSARModel7705SARmlEReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARmlEReg.setStatus("current")
_AluSARModel7705SARHReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARHReg = _AluSARModel7705SARHReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARHReg.setStatus("current")
_AluSARModel7705SARHCReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARHCReg = _AluSARModel7705SARHCReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARHCReg.setStatus("current")
_AluSARModel7705SARWxAReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxAReg = _AluSARModel7705SARWxAReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxAReg.setStatus("current")
_AluSARModel7705SARWxBReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxBReg = _AluSARModel7705SARWxBReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxBReg.setStatus("current")
_AluSARModel7705SARWxCReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxCReg = _AluSARModel7705SARWxCReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxCReg.setStatus("current")
_AluSARModel7705SARWxDReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxDReg = _AluSARModel7705SARWxDReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxDReg.setStatus("current")
_AluSARModel7705SARWxEReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxEReg = _AluSARModel7705SARWxEReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 17)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxEReg.setStatus("current")
_AluSARModel7705SARWxFReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxFReg = _AluSARModel7705SARWxFReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 18)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxFReg.setStatus("current")
_AluSARModel7705SARXReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARXReg = _AluSARModel7705SARXReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 19)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARXReg.setStatus("current")
_AluSARModel7705SARWxGReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxGReg = _AluSARModel7705SARWxGReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 20)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxGReg.setStatus("current")
_AluSARModel7705SARWxHReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxHReg = _AluSARModel7705SARWxHReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 21)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxHReg.setStatus("current")
_AluSARModel7705SARWxIReg_ObjectIdentity = ObjectIdentity
aluSARModel7705SARWxIReg = _AluSARModel7705SARWxIReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 2, 22)
)
if mibBuilder.loadTexts:
    aluSARModel7705SARWxIReg.setStatus("current")
_AluSARMIB_ObjectIdentity = ObjectIdentity
aluSARMIB = _AluSARMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2)
)
_AluSARConfs_ObjectIdentity = ObjectIdentity
aluSARConfs = _AluSARConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1)
)
_AluSARObjs_ObjectIdentity = ObjectIdentity
aluSARObjs = _AluSARObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2)
)
_AluSARNotifyPrefix_ObjectIdentity = ObjectIdentity
aluSARNotifyPrefix = _AluSARNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3)
)
_AluSARProductCapability_ObjectIdentity = ObjectIdentity
aluSARProductCapability = _AluSARProductCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3)
)
_AluSAR7705Capability_ObjectIdentity = ObjectIdentity
aluSAR7705Capability = _AluSAR7705Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1)
)
_AluSAR7705V1v0_ObjectIdentity = ObjectIdentity
aluSAR7705V1v0 = _AluSAR7705V1v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 1)
)
_AluSAR7705V1v1_ObjectIdentity = ObjectIdentity
aluSAR7705V1v1 = _AluSAR7705V1v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 2)
)
_AluSAR7705V2v0_ObjectIdentity = ObjectIdentity
aluSAR7705V2v0 = _AluSAR7705V2v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 3)
)
_AluSAR7705V2v1_ObjectIdentity = ObjectIdentity
aluSAR7705V2v1 = _AluSAR7705V2v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 4)
)
_AluSAR7705V3v0_ObjectIdentity = ObjectIdentity
aluSAR7705V3v0 = _AluSAR7705V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 5)
)
_AluSAR7705V4v0_ObjectIdentity = ObjectIdentity
aluSAR7705V4v0 = _AluSAR7705V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 6)
)
_AluSAR7705V5v0_ObjectIdentity = ObjectIdentity
aluSAR7705V5v0 = _AluSAR7705V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 7)
)
_AluSAR7705V6v0_ObjectIdentity = ObjectIdentity
aluSAR7705V6v0 = _AluSAR7705V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 8)
)
_AluSAR7705V6v1_ObjectIdentity = ObjectIdentity
aluSAR7705V6v1 = _AluSAR7705V6v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 9)
)
_AluSAR7705V7v0_ObjectIdentity = ObjectIdentity
aluSAR7705V7v0 = _AluSAR7705V7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 3, 1, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-SAR-GLOBAL-MIB",
    **{"aluServiceAggrRouters": aluServiceAggrRouters,
       "aluSARRegistry": aluSARRegistry,
       "aluSARModules": aluSARModules,
       "aluSARGlobalMIBModule": aluSARGlobalMIBModule,
       "aluSARMIBModules": aluSARMIBModules,
       "aluSARCapabilityModule": aluSARCapabilityModule,
       "aluSAR7705CapModule": aluSAR7705CapModule,
       "aluSAR7705ServiceAggrRouters": aluSAR7705ServiceAggrRouters,
       "aluSARModel7705SAR8Reg": aluSARModel7705SAR8Reg,
       "aluSARModel7705SARfReg": aluSARModel7705SARfReg,
       "aluSARModel7705SAR18Reg": aluSARModel7705SAR18Reg,
       "aluSARModel7705SARmReg": aluSARModel7705SARmReg,
       "aluSARModel7705SARmeReg": aluSARModel7705SARmeReg,
       "aluSARModel7705SARmlAReg": aluSARModel7705SARmlAReg,
       "aluSARModel7705SARmlBReg": aluSARModel7705SARmlBReg,
       "aluSARModel7705SARmlCReg": aluSARModel7705SARmlCReg,
       "aluSARModel7705SARmlDReg": aluSARModel7705SARmlDReg,
       "aluSARModel7705SARmlEReg": aluSARModel7705SARmlEReg,
       "aluSARModel7705SARHReg": aluSARModel7705SARHReg,
       "aluSARModel7705SARHCReg": aluSARModel7705SARHCReg,
       "aluSARModel7705SARWxAReg": aluSARModel7705SARWxAReg,
       "aluSARModel7705SARWxBReg": aluSARModel7705SARWxBReg,
       "aluSARModel7705SARWxCReg": aluSARModel7705SARWxCReg,
       "aluSARModel7705SARWxDReg": aluSARModel7705SARWxDReg,
       "aluSARModel7705SARWxEReg": aluSARModel7705SARWxEReg,
       "aluSARModel7705SARWxFReg": aluSARModel7705SARWxFReg,
       "aluSARModel7705SARXReg": aluSARModel7705SARXReg,
       "aluSARModel7705SARWxGReg": aluSARModel7705SARWxGReg,
       "aluSARModel7705SARWxHReg": aluSARModel7705SARWxHReg,
       "aluSARModel7705SARWxIReg": aluSARModel7705SARWxIReg,
       "aluSARMIB": aluSARMIB,
       "aluSARConfs": aluSARConfs,
       "aluSARObjs": aluSARObjs,
       "aluSARNotifyPrefix": aluSARNotifyPrefix,
       "aluSARProductCapability": aluSARProductCapability,
       "aluSAR7705Capability": aluSAR7705Capability,
       "aluSAR7705V1v0": aluSAR7705V1v0,
       "aluSAR7705V1v1": aluSAR7705V1v1,
       "aluSAR7705V2v0": aluSAR7705V2v0,
       "aluSAR7705V2v1": aluSAR7705V2v1,
       "aluSAR7705V3v0": aluSAR7705V3v0,
       "aluSAR7705V4v0": aluSAR7705V4v0,
       "aluSAR7705V5v0": aluSAR7705V5v0,
       "aluSAR7705V6v0": aluSAR7705V6v0,
       "aluSAR7705V6v1": aluSAR7705V6v1,
       "aluSAR7705V7v0": aluSAR7705V7v0}
)
