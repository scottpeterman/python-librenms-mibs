# SNMP MIB module (WAYSTREAM-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\waystream\WAYSTREAM-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:01 2025
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

(wsModules,
 wsProduct) = mibBuilder.importSymbols(
    "WAYSTREAM-SMI",
    "wsModules",
    "wsProduct")


# MODULE-IDENTITY

wsProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 5, 2)
)
if mibBuilder.loadTexts:
    wsProductsMIB.setRevisions(
        ("2017-02-10 11:00",
         "2015-04-08 14:52",
         "2012-09-24 14:35",
         "2012-02-02 15:30",
         "2011-12-05 11:00",
         "2011-06-10 13:56",
         "2011-01-12 13:10",
         "2010-05-17 14:10",
         "2009-04-14 12:29",
         "2009-03-23 10:53",
         "2007-05-14 12:38",
         "2006-01-25 13:30",
         "2004-10-20 14:34",
         "2003-11-04 00:01")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asr_ObjectIdentity = ObjectIdentity
asr = _Asr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1)
)
if mibBuilder.loadTexts:
    asr.setStatus("current")
_Asr4108C_ObjectIdentity = ObjectIdentity
asr4108C = _Asr4108C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 1)
)
_Asr4116C_ObjectIdentity = ObjectIdentity
asr4116C = _Asr4116C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 2)
)
_Asr4124C_ObjectIdentity = ObjectIdentity
asr4124C = _Asr4124C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 3)
)
_Asr4208FM_ObjectIdentity = ObjectIdentity
asr4208FM = _Asr4208FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 4)
)
_Asr4216FM_ObjectIdentity = ObjectIdentity
asr4216FM = _Asr4216FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 5)
)
_Asr4224FM_ObjectIdentity = ObjectIdentity
asr4224FM = _Asr4224FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 6)
)
_Asr4308FV_ObjectIdentity = ObjectIdentity
asr4308FV = _Asr4308FV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 7)
)
_Asr4316FV_ObjectIdentity = ObjectIdentity
asr4316FV = _Asr4316FV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 8)
)
_Asr4324FV_ObjectIdentity = ObjectIdentity
asr4324FV = _Asr4324FV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 9)
)
_Asr4408SFV_ObjectIdentity = ObjectIdentity
asr4408SFV = _Asr4408SFV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 10)
)
_Asr4416SFV_ObjectIdentity = ObjectIdentity
asr4416SFV = _Asr4416SFV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 11)
)
_Asr4424SFV_ObjectIdentity = ObjectIdentity
asr4424SFV = _Asr4424SFV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 12)
)
_Asr4508SFM_ObjectIdentity = ObjectIdentity
asr4508SFM = _Asr4508SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 13)
)
_Asr4516SFM_ObjectIdentity = ObjectIdentity
asr4516SFM = _Asr4516SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 14)
)
_Asr4524SFM_ObjectIdentity = ObjectIdentity
asr4524SFM = _Asr4524SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 15)
)
_Asr4608SFS_ObjectIdentity = ObjectIdentity
asr4608SFS = _Asr4608SFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 16)
)
_Asr4616SFS_ObjectIdentity = ObjectIdentity
asr4616SFS = _Asr4616SFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 17)
)
_Asr4624SFS_ObjectIdentity = ObjectIdentity
asr4624SFS = _Asr4624SFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 18)
)
_Asr3108VDSL_ObjectIdentity = ObjectIdentity
asr3108VDSL = _Asr3108VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 19)
)
_Asr3116VDSL_ObjectIdentity = ObjectIdentity
asr3116VDSL = _Asr3116VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 20)
)
_Asr3124VDSL_ObjectIdentity = ObjectIdentity
asr3124VDSL = _Asr3124VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 21)
)
_Asr3208VDSL_ObjectIdentity = ObjectIdentity
asr3208VDSL = _Asr3208VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 22)
)
_Asr3216VDSL_ObjectIdentity = ObjectIdentity
asr3216VDSL = _Asr3216VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 23)
)
_Asr3224VDSL_ObjectIdentity = ObjectIdentity
asr3224VDSL = _Asr3224VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 24)
)
_Asr3308VDSL_ObjectIdentity = ObjectIdentity
asr3308VDSL = _Asr3308VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 25)
)
_Asr3316VDSL_ObjectIdentity = ObjectIdentity
asr3316VDSL = _Asr3316VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 26)
)
_Asr3324VDSL_ObjectIdentity = ObjectIdentity
asr3324VDSL = _Asr3324VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 27)
)
_Asr4708SFL_ObjectIdentity = ObjectIdentity
asr4708SFL = _Asr4708SFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 28)
)
_Asr4716SFL_ObjectIdentity = ObjectIdentity
asr4716SFL = _Asr4716SFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 29)
)
_Asr4724SFL_ObjectIdentity = ObjectIdentity
asr4724SFL = _Asr4724SFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 30)
)
_Asr4108Cco_ObjectIdentity = ObjectIdentity
asr4108Cco = _Asr4108Cco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 31)
)
_Asr4116Cco_ObjectIdentity = ObjectIdentity
asr4116Cco = _Asr4116Cco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 32)
)
_Asr4124Cco_ObjectIdentity = ObjectIdentity
asr4124Cco = _Asr4124Cco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 33)
)
_Asr4208FMco_ObjectIdentity = ObjectIdentity
asr4208FMco = _Asr4208FMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 34)
)
_Asr4216FMco_ObjectIdentity = ObjectIdentity
asr4216FMco = _Asr4216FMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 35)
)
_Asr4224FMco_ObjectIdentity = ObjectIdentity
asr4224FMco = _Asr4224FMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 36)
)
_Asr4308FVco_ObjectIdentity = ObjectIdentity
asr4308FVco = _Asr4308FVco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 37)
)
_Asr4316FVco_ObjectIdentity = ObjectIdentity
asr4316FVco = _Asr4316FVco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 38)
)
_Asr4324FVco_ObjectIdentity = ObjectIdentity
asr4324FVco = _Asr4324FVco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 39)
)
_Asr4508SFMco_ObjectIdentity = ObjectIdentity
asr4508SFMco = _Asr4508SFMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 40)
)
_Asr4516SFMco_ObjectIdentity = ObjectIdentity
asr4516SFMco = _Asr4516SFMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 41)
)
_Asr4524SFMco_ObjectIdentity = ObjectIdentity
asr4524SFMco = _Asr4524SFMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 42)
)
_Asr4608SFSco_ObjectIdentity = ObjectIdentity
asr4608SFSco = _Asr4608SFSco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 43)
)
_Asr4616SFSco_ObjectIdentity = ObjectIdentity
asr4616SFSco = _Asr4616SFSco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 44)
)
_Asr4624SFSco_ObjectIdentity = ObjectIdentity
asr4624SFSco = _Asr4624SFSco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 45)
)
_Asr4708SFLco_ObjectIdentity = ObjectIdentity
asr4708SFLco = _Asr4708SFLco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 46)
)
_Asr4716SFLco_ObjectIdentity = ObjectIdentity
asr4716SFLco = _Asr4716SFLco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 47)
)
_Asr4724SFLco_ObjectIdentity = ObjectIdentity
asr4724SFLco = _Asr4724SFLco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 48)
)
_Asr10132co_ObjectIdentity = ObjectIdentity
asr10132co = _Asr10132co_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 49)
)
_Asr5124Cacco_ObjectIdentity = ObjectIdentity
asr5124Cacco = _Asr5124Cacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 50)
)
_Asr5124Cdcco_ObjectIdentity = ObjectIdentity
asr5124Cdcco = _Asr5124Cdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 51)
)
_Asr5224FMacco_ObjectIdentity = ObjectIdentity
asr5224FMacco = _Asr5224FMacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 52)
)
_Asr5224FMdcco_ObjectIdentity = ObjectIdentity
asr5224FMdcco = _Asr5224FMdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 53)
)
_Asr5624FSacco_ObjectIdentity = ObjectIdentity
asr5624FSacco = _Asr5624FSacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 54)
)
_Asr5624FSdcco_ObjectIdentity = ObjectIdentity
asr5624FSdcco = _Asr5624FSdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 55)
)
_Asr5724FLacco_ObjectIdentity = ObjectIdentity
asr5724FLacco = _Asr5724FLacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 56)
)
_Asr5724FLdcco_ObjectIdentity = ObjectIdentity
asr5724FLdcco = _Asr5724FLdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 57)
)
_Se1_ObjectIdentity = ObjectIdentity
se1 = _Se1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 58)
)
_Se2_ObjectIdentity = ObjectIdentity
se2 = _Se2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 59)
)
_Asr6026ac_ObjectIdentity = ObjectIdentity
asr6026ac = _Asr6026ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 60)
)
_Asr6026dc_ObjectIdentity = ObjectIdentity
asr6026dc = _Asr6026dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 61)
)
_Asr6126ac_ObjectIdentity = ObjectIdentity
asr6126ac = _Asr6126ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 62)
)
_Asr6126dc_ObjectIdentity = ObjectIdentity
asr6126dc = _Asr6126dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 63)
)
_Ipd_ObjectIdentity = ObjectIdentity
ipd = _Ipd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 2)
)
if mibBuilder.loadTexts:
    ipd.setStatus("current")
_Ipd1116C_ObjectIdentity = ObjectIdentity
ipd1116C = _Ipd1116C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 2, 1)
)
_Legacy1_ObjectIdentity = ObjectIdentity
legacy1 = _Legacy1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3)
)
if mibBuilder.loadTexts:
    legacy1.setStatus("current")
_Ms_ObjectIdentity = ObjectIdentity
ms = _Ms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5)
)
if mibBuilder.loadTexts:
    ms.setStatus("current")
_Ms3028ac_ObjectIdentity = ObjectIdentity
ms3028ac = _Ms3028ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 3)
)
_Ms3028dc_ObjectIdentity = ObjectIdentity
ms3028dc = _Ms3028dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 4)
)
_Ms3128ac_ObjectIdentity = ObjectIdentity
ms3128ac = _Ms3128ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 5)
)
_Ms3128dc_ObjectIdentity = ObjectIdentity
ms3128dc = _Ms3128dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 6)
)
_Ms4026ac_ObjectIdentity = ObjectIdentity
ms4026ac = _Ms4026ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 64)
)
_Ms4026dc_ObjectIdentity = ObjectIdentity
ms4026dc = _Ms4026dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 65)
)
_Ms4126ac_ObjectIdentity = ObjectIdentity
ms4126ac = _Ms4126ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 66)
)
_Ms4126dc_ObjectIdentity = ObjectIdentity
ms4126dc = _Ms4126dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 67)
)
_Legacy2_ObjectIdentity = ObjectIdentity
legacy2 = _Legacy2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 6)
)
if mibBuilder.loadTexts:
    legacy2.setStatus("current")
_Mpc_ObjectIdentity = ObjectIdentity
mpc = _Mpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7)
)
if mibBuilder.loadTexts:
    mpc.setStatus("current")
_Mpc480se4818_ObjectIdentity = ObjectIdentity
mpc480se4818 = _Mpc480se4818_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 68)
)
_Mpc480se4818t_ObjectIdentity = ObjectIdentity
mpc480se4818t = _Mpc480se4818t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 69)
)
_Mpc480re4818_ObjectIdentity = ObjectIdentity
mpc480re4818 = _Mpc480re4818_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 70)
)
_Mpc480re4818t_ObjectIdentity = ObjectIdentity
mpc480re4818t = _Mpc480re4818t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 71)
)
_Mpc480me4818_ObjectIdentity = ObjectIdentity
mpc480me4818 = _Mpc480me4818_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 72)
)
_Mpc480me4818t_ObjectIdentity = ObjectIdentity
mpc480me4818t = _Mpc480me4818t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 73)
)
_Reserved1_ObjectIdentity = ObjectIdentity
reserved1 = _Reserved1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 74)
)
_Reserved2_ObjectIdentity = ObjectIdentity
reserved2 = _Reserved2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 75)
)
_Reserved3_ObjectIdentity = ObjectIdentity
reserved3 = _Reserved3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 76)
)
_Reserved4_ObjectIdentity = ObjectIdentity
reserved4 = _Reserved4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 7, 77)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAYSTREAM-PRODUCTS-MIB",
    **{"asr": asr,
       "asr4108C": asr4108C,
       "asr4116C": asr4116C,
       "asr4124C": asr4124C,
       "asr4208FM": asr4208FM,
       "asr4216FM": asr4216FM,
       "asr4224FM": asr4224FM,
       "asr4308FV": asr4308FV,
       "asr4316FV": asr4316FV,
       "asr4324FV": asr4324FV,
       "asr4408SFV": asr4408SFV,
       "asr4416SFV": asr4416SFV,
       "asr4424SFV": asr4424SFV,
       "asr4508SFM": asr4508SFM,
       "asr4516SFM": asr4516SFM,
       "asr4524SFM": asr4524SFM,
       "asr4608SFS": asr4608SFS,
       "asr4616SFS": asr4616SFS,
       "asr4624SFS": asr4624SFS,
       "asr3108VDSL": asr3108VDSL,
       "asr3116VDSL": asr3116VDSL,
       "asr3124VDSL": asr3124VDSL,
       "asr3208VDSL": asr3208VDSL,
       "asr3216VDSL": asr3216VDSL,
       "asr3224VDSL": asr3224VDSL,
       "asr3308VDSL": asr3308VDSL,
       "asr3316VDSL": asr3316VDSL,
       "asr3324VDSL": asr3324VDSL,
       "asr4708SFL": asr4708SFL,
       "asr4716SFL": asr4716SFL,
       "asr4724SFL": asr4724SFL,
       "asr4108Cco": asr4108Cco,
       "asr4116Cco": asr4116Cco,
       "asr4124Cco": asr4124Cco,
       "asr4208FMco": asr4208FMco,
       "asr4216FMco": asr4216FMco,
       "asr4224FMco": asr4224FMco,
       "asr4308FVco": asr4308FVco,
       "asr4316FVco": asr4316FVco,
       "asr4324FVco": asr4324FVco,
       "asr4508SFMco": asr4508SFMco,
       "asr4516SFMco": asr4516SFMco,
       "asr4524SFMco": asr4524SFMco,
       "asr4608SFSco": asr4608SFSco,
       "asr4616SFSco": asr4616SFSco,
       "asr4624SFSco": asr4624SFSco,
       "asr4708SFLco": asr4708SFLco,
       "asr4716SFLco": asr4716SFLco,
       "asr4724SFLco": asr4724SFLco,
       "asr10132co": asr10132co,
       "asr5124Cacco": asr5124Cacco,
       "asr5124Cdcco": asr5124Cdcco,
       "asr5224FMacco": asr5224FMacco,
       "asr5224FMdcco": asr5224FMdcco,
       "asr5624FSacco": asr5624FSacco,
       "asr5624FSdcco": asr5624FSdcco,
       "asr5724FLacco": asr5724FLacco,
       "asr5724FLdcco": asr5724FLdcco,
       "se1": se1,
       "se2": se2,
       "asr6026ac": asr6026ac,
       "asr6026dc": asr6026dc,
       "asr6126ac": asr6126ac,
       "asr6126dc": asr6126dc,
       "ipd": ipd,
       "ipd1116C": ipd1116C,
       "legacy1": legacy1,
       "ms": ms,
       "ms3028ac": ms3028ac,
       "ms3028dc": ms3028dc,
       "ms3128ac": ms3128ac,
       "ms3128dc": ms3128dc,
       "ms4026ac": ms4026ac,
       "ms4026dc": ms4026dc,
       "ms4126ac": ms4126ac,
       "ms4126dc": ms4126dc,
       "legacy2": legacy2,
       "mpc": mpc,
       "mpc480se4818": mpc480se4818,
       "mpc480se4818t": mpc480se4818t,
       "mpc480re4818": mpc480re4818,
       "mpc480re4818t": mpc480re4818t,
       "mpc480me4818": mpc480me4818,
       "mpc480me4818t": mpc480me4818t,
       "reserved1": reserved1,
       "reserved2": reserved2,
       "reserved3": reserved3,
       "reserved4": reserved4,
       "wsProductsMIB": wsProductsMIB}
)
